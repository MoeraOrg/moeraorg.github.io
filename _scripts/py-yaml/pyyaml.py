import sys
from typing import Any, List, Tuple

import yaml
from camel_converter import to_snake

PY_TYPES = {
    'String': 'str',
    'String[]': 'List[str]',
    'int': 'int',
    'float': 'float',
    'boolean': 'bool',
    'timestamp': 'Timestamp',
    'byte[]': 'bytes',
    'UUID': 'str',
    'String -> int': 'Mapping[str, int]'
}


def to_py_type(api_type: str) -> str:
    py_type = PY_TYPES.get(api_type)
    if py_type is None:
        print('Unrecognized field type: ' + api_type)
        exit(1)
    return py_type


def to_py_doc(s: str) -> str:
    return (s.replace('<code>null</code>', '<code>None</code>')
             .replace('<code>true</code>', '<code>True</code>')
             .replace('<code>false</code>', '<code>False</code>'))


def read_node_api(datadir: str) -> Tuple[Any, Any]:
    with open(datadir + '/node_api.yml', 'r') as ifile:
        api = yaml.safe_load(ifile)
    with open(datadir + '/py_node_classes.yml', 'r') as ifile:
        classes = yaml.safe_load(ifile)
    return api, classes


def method_params(params: List[Any]) -> str:
    names = []
    for param in params:
        if param.get('optional', False):
            if param['name'].startswith('with_'):
                names.append(f'{param["name"]}=False')
            else:
                names.append(f'{param["name"]}=None')
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
        param['name'] = to_snake(param['name'])
        if 'flags' in param:
            for flag in param['flags']:
                tail_params.append({
                    'name': f'with_{flag["name"]}',
                    'type': 'bool',
                    'description': 'include ' + to_py_doc(flag.get('description', '')),
                    'optional': True
                })
        else:
            if 'enum' not in param:
                param['type'] = to_py_type(param['type'])
            param['description'] = to_py_doc(param.get('description', ''))
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
                {'name': 'file', 'type': 'IO'},
                {'name': 'file_type', 'type': 'str', 'description': 'content-type of <code>file</code>'}
            ]
        else:
            if 'name' not in inp:
                print('Missing name of body of the request "{method} {url}"'
                      .format(method=request['type'], url=request['url']))
                exit(1)
            param = {
                'name': to_snake(inp['name']),
                'struct': inp['struct']
            }
            if inp.get('array', False):
                param['array'] = True
            params.append(param)
    params += tail_params

    request['function'] = to_snake(request['function']) + '(' + method_params(params) + ')'
    request['params'] = params
    request['description'] = to_py_doc(request['description'])
    del request['type']
    del request['url']


def convert_structure(struct: Any) -> None:
    fields = []
    for field in struct['fields']:
        field['name'] = to_snake(field['name'])
        if 'type' in field:
            if field['type'] == 'any':
                continue
            field['type'] = to_py_type(field['type'])
        if 'description' in field:
            field['description'] = to_py_doc(field['description'])
        fields.append(field)
    struct['fields'] = fields


def convert_operations(operations: Any) -> None:
    for field in operations['fields']:
        field['name'] = to_snake(field['name'])
        if 'description' in field:
            field['description'] = to_py_doc(field['description'])


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
    for operations in api['operations']:
        convert_operations(operations)


def write_node_api(api: Any, datadir: str) -> None:
    with open(datadir + '/py_node_api.yml', 'w+') as ofile:
        yaml.safe_dump(api, ofile, default_flow_style=False)


if len(sys.argv) < 2 or sys.argv[1] == '':
    print("Usage: py-yaml <directory>")
    exit(1)

datadir = sys.argv[1]
api, classes = read_node_api(datadir)
convert_node_api(api, classes)
write_node_api(api, datadir)
