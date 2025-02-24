import sys
from typing import Any, List, Tuple

import yaml

TS_TYPES = {
    'String': 'string',
    'String[]': 'string[]',
    'short': 'number',
    'int': 'number',
    'long': 'number',
    'float': 'number',
    'boolean': 'boolean',
    'timestamp': 'number',
    'byte[]': 'string',
    'UUID': 'string',
    'String -> int': 'Partial<Record<string, number>>'
}


def to_ts_type(api_type: str) -> str:
    ts_type = TS_TYPES.get(api_type)
    if ts_type is None:
        print('Unrecognized field type: ' + api_type)
        exit(1)
    return ts_type


def read_node_api(datadir: str) -> Tuple[Any, Any]:
    with open(datadir + '/node_api.yml', 'r') as ifile:
        api = yaml.safe_load(ifile)
    with open(datadir + '/ts_node_classes.yml', 'r') as ifile:
        classes = yaml.safe_load(ifile)
    return api, classes


def method_params(params: List[Any]) -> str:
    names = []
    for param in params:
        if param.get('optional', False):
            if param['name'].startswith('with_'):
                names.append(f'{param["name"]}=false')
            else:
                names.append(f'{param["name"]}=null')
        else:
            names.append(param["name"])
    return ', '.join(names)


def convert_request(request: Any) -> None:
    params = []
    tail_params = []
    for param in request.get('params', []) + request.get('query', []):
        if 'name' not in param:
            print('Missing name of parameter of the request "{method} {url}"'
                  .format(method=request['type'], url=request['url']))
            exit(1)
        if 'flags' in param:
            for flag in param['flags']:
                tail_params.append({
                    'name': f'with{flag["name"].capitalize()}',
                    'type': 'boolean',
                    'description': 'include ' + flag.get('description', ''),
                    'optional': True
                })
        else:
            if 'enum' not in param:
                param['type'] = to_ts_type(param['type'])
            if param.get('optional', False):
                tail_params.append(param)
            else:
                params.append(param)
    if 'query' in request:
        del request['query']

    if 'in' in request:
        inp = request['in']
        del request['in']
        if 'type' in inp:
            if inp['type'] != 'blob':
                print('Unrecognised type "{type}" of the input body of the request "{method} {url}"'
                      .format(type=inp['type'], method=request['type'], url=request['url']))
                exit(1)
            params += [
                {'name': 'body', 'type': 'Buffer'},
                {'name': 'contentType', 'type': 'string', 'description': 'content-type of <code>body</code>'}
            ]
        else:
            if 'name' not in inp:
                print('Missing name of body of the request "{method} {url}"'
                      .format(method=request['type'], url=request['url']))
                exit(1)
            param = {
                'name': inp['name'],
                'struct': inp['struct']
            }
            if inp.get('array', False):
                param['array'] = True
            params.append(param)
    params += tail_params

    request['function'] = request['function'] + '(' + method_params(params) + ')'
    request['params'] = params
    del request['type']
    del request['url']


def convert_structure(struct: Any) -> None:
    fields = []
    for field in struct['fields']:
        if 'type' in field:
            if field['type'] == 'any':
                continue
            field['type'] = to_ts_type(field['type'])
        fields.append(field)
    struct['fields'] = fields


def convert_node_api(api: Any, classes: Any) -> None:
    del api['http-codes']
    for object in api['objects']:
        if 'requests' not in object:
            continue
        object['requests'] = [r for r in object['requests'] if 'function' in r]
        for request in object['requests']:
            convert_request(request)
    api['objects'] = classes['objects'] + api['objects']
    for struct in api['structures']:
        convert_structure(struct)


def write_node_api(api: Any, datadir: str) -> None:
    with open(datadir + '/ts_node_api.yml', 'w+') as ofile:
        yaml.safe_dump(api, ofile, default_flow_style=False)


def read_naming_api(datadir: str) -> Any:
    with open(datadir + '/naming_api.yml', 'r') as ifile:
        return yaml.safe_load(ifile)


def convert_call(call: Any) -> None:
    for param in call.get('params', []):
        param['type'] = to_ts_type(param['type'])
    if 'returns' in call:
        if 'type' in call['returns']:
            call['returns']['type'] = to_ts_type(call['returns']['type'])
    if 'fingerprint' in call:
        del call['fingerprint']


def convert_naming_api(api: Any) -> None:
    for call in api['calls']:
        convert_call(call)
    for struct in api['structures']:
        convert_structure(struct)
    del api['errors']


def write_naming_api(api: Any, datadir: str) -> None:
    with open(datadir + '/ts_naming_api.yml', 'w+') as ofile:
        yaml.safe_dump(api, ofile, default_flow_style=False)


TS_FP_TYPES = {
    'String': 'string',
    'InetAddress': 'string',
    'int': 'number',
    'long': 'number',
    'timestamp': 'number',
    'byte': 'number',
    'byte[]': 'Buffer',
    'boolean': 'boolean'
}


def read_node_fingerprints(datadir: str) -> Any:
    with open(datadir + '/node_api_fingerprints.yml', 'r') as ifile:
        return yaml.safe_load(ifile)


def write_node_fingerprints(fp: Any, datadir: str) -> None:
    with open(datadir + '/ts_node_api_fingerprints.yml', 'w+') as ofile:
        yaml.safe_dump(fp, ofile, default_flow_style=False)


def read_naming_fingerprints(datadir: str) -> Any:
    with open(datadir + '/naming_api_fingerprints.yml', 'r') as ifile:
        return yaml.safe_load(ifile)


def write_naming_fingerprints(fp: Any, datadir: str) -> None:
    with open(datadir + '/ts_naming_api_fingerprints.yml', 'w+') as ofile:
        yaml.safe_dump(fp, ofile, default_flow_style=False)


def convert_fingerprints(fp: Any) -> None:
    for object in fp['objects']:
        for schema in object['versions']:
            for field in schema['fingerprint']:
                if 'type' in field:
                    field_type = TS_FP_TYPES[field['type']]
                else:
                    field_type = 'Buffer'
                if field.get('array', False):
                    field_type = f'{field_type}[]'
                field['type'] = field_type
                field.pop('digest', None)
                field.pop('array', None)
            schema['fingerprint'] = [field for field in schema['fingerprint'] if field['field'] != 'object_type']


if len(sys.argv) < 2 or sys.argv[1] == '':
    print("Usage: ts-yaml <directory>")
    exit(1)

datadir = sys.argv[1]

api, classes = read_node_api(datadir)
convert_node_api(api, classes)
write_node_api(api, datadir)

api = read_naming_api(datadir)
convert_naming_api(api)
write_naming_api(api, datadir)

fp = read_node_fingerprints(datadir)
convert_fingerprints(fp)
write_node_fingerprints(fp, datadir)

fp = read_naming_fingerprints(datadir)
convert_fingerprints(fp)
write_naming_fingerprints(fp, datadir)
