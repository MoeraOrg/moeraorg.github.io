---
layout: development
title: Python Library
---

# Python Library

`moeralib` ([GitHub][1]) is a library that allows Python applications to easily
interact with the Moera network.

The easiest way to install the library is from [PyPI repository][2]:

```
pip install moeralib
```

## Naming API

<code><a href="naming.html">moeralib.naming</a></code> module contains classes and
routines for interacting with Moera naming service. To access a naming server, create
`MoeraNaming` class and pass the naming server URL in the parameters. There are
constants for two well-known servers: `MAIN_SERVER` and `DEV_SERVER`. The first one
is used by default by `MoeraNaming`.

```python
from moeralib.naming import MoeraNaming, DEV_SERVER

naming = MoeraNaming(DEV_SERVER)
info = naming.get_current('balu-dev', 0)
print(info.node_uri)
```

A shortcut function `resolve()` simplifies resolving of names.

```python
from moeralib.naming import resolve, DEV_SERVER

print(resolve('balu-dev_0', naming_server=DEV_SERVER))
```

## Node API

<code><a href="node.html">moeralib.node</a></code> module contains classes and
routines for accessing Moera nodes. Just create `MoeraNode` class with the URL of
the node, and call the methods you need.

```python
from moeralib.naming import resolve
from moeralib.node import MoeraNode

node = MoeraNode(resolve('Alice'))
print(node.who_am_i().full_name)
```

The library automatically parses JSON structures coming from the node and converts
them to Python objects derived from `Structure` class. If some field is not present
in JSON, the corresponding field in Python is set to `None`.

## Structures

Inputs and outputs of API calls are represented as plain Python classes derived from
`Structure` class. All structures have a constructor with keyword parameters that
correspond to fields of the structure. You can use the constructor to initialize
a structure. These code snippets are equivalent:

```python
attrs = DomainAttributes()
attrs.name = 'dave.moera.club'
attrs.node_id = DAVE_NODE_ID
```
```python
attrs = DomainAttributes(
    name='dave.moera.club',
    node_id=DAVE_NODE_ID
)
```

There are two more methods designed to be used internally.

`from_json()` method creates a structure object from a JSON object represented as
a `dict` (as returned from `json.load()`). The method automatically converts field
names from camel case to snake case (if needed) and creates nested structures in
accordance with fields' type specifications.

`json()` method converts the structure back to a `dict` representing a JSON structure,
converting all field names to camel case.

## Authentication

_[Read more about authentication][3] in the Node API reference._

To perform an authenticated request, you need to put the root secret, token, or carte
into `MoeraNode` and activate the corresponding authentication mode. Use
`root_secret()`, `token()`, and `carte()` methods to set the root secret, token, and
carte correspondingly. The authentication mode is activated by generic
`auth_method()`, or by shortcut methods `no_auth()`, `auth()`, `auth_admin()`,
`auth_root_admin()`. After that, all API requests will be authenticated with
the selected method, if needed. You can switch to a different method at any time.

```python
from moeralib.naming import resolve
from moeralib.node import MoeraNode

node = MoeraNode(resolve('Alice'))
node.token('putthetokenhere')
node.auth_admin()
print(node.get_profile().email)
```

## Managing cartes

`MoeraCarteSource` class simplifies managing authentication cartes. It obtains cartes
from a home node, caches them, supplies valid cartes for authentication, and requests
new ones when old ones expire.

```python
from moeralib.naming import resolve
from moeralib.node import MoeraCarteSource, MoeraNode

home = MoeraNode(resolve('Alice'))
home.token('putthetokenhere')
home.auth_admin()

node = MoeraNode(resolve('Bob'))
node.carte_source(MoeraCarteSource(home))
node.auth()
slice = node.get_feed_slice('timeline')
for story in slice.stories:
    if story.posting is not None:
        print(story.posting.operations.view, story.posting.heading)
```

## Generating cartes

`generate_carte()` function generates a carte with the given parameters and signs
it with the provided private signing key.

```python
import time

from moeralib.crypto import raw_to_private_key
from moeralib.node import generate_carte

signing_key = raw_to_private_key(
    bytes.fromhex('72d0817beaf1800c5448841e490139b680f134a56e140bdb4f33aeb2c43e3c48')
)
carte = generate_carte('app0_0', signing_key, int(time.time()), node_name='Alice')
```

## Universal URLs

<code><a href="universal_location.html">moeralib.universal_location</a></code>
module contains classes and routines for creating and parsing Moera universal
URLs.

To parse a universal URL, pass it to `parse()` function. It returns a
`UniversalLocation` instance containing the result of parsing.

```python
from moeralib.universal_location import parse

uni = parse('https://moera.page/@Alice/alice.moera.blog/post/69a403ef-b72d-43e0-967e-eab5e8dce9d3')
print(uni.node_name, uni.authority, uni.path)
```

To build a universal URL from parts, use `redirect_to()` function.

```python
from moeralib.universal_location import redirect_to

print(redirect_to(
    node_name='Alice_0',
    root_url='https://alice.moera.blog/',
    path='/post/69a403ef-b72d-43e0-967e-eab5e8dce9d3'
))
```

`redirect_to_url()` function converts URL of a page on a node to a corresponding
universal URL.

```python
from moeralib.universal_location import redirect_to_url

print(redirect_to_url(
    'Alice_0',
    'https://alice.moera.blog/moera/post/69a403ef-b72d-43e0-967e-eab5e8dce9d3'
))
```

## Cryptography

<code><a href="crypto.html">moeralib.crypto</a></code> module provides utilities
for generation of cryptographic keys, signing
<a href="../cryptography/fingerprint.html">fingerprints</a> and validating
signatures. These functions are wrappers around
<code><a href="https://pypi.org/project/cryptography/">cryptography</a></code>
library using the <a href="../cryptography/algorithms.html">algorithms</a>
defined in the Moera protocol.

Functions for building fingerprints for various objects are defined in
<code><a href="naming-fingerprints.html">moeralib.naming.fingerprints</a></code>
and <code><a href="node-fingerprints.html">moeralib.node.fingerprints</a></code>
modules. (The functions may have several versions for different versions of
the fingerprint.)

The following code changes a node URL on the naming server.
(The user should provide mnemonic of the updating key.)

```python
from moeralib import naming
from moeralib.crypto import sign_fingerprint, mnemonic_to_private_key
from moeralib.naming.fingerprints import create_put_call_fingerprint0

private_updating_key = mnemonic_to_private_key(mnemonic)

srv = naming.MoeraNaming()
info = srv.get_current(name, generation)

fingerprint = create_put_call_fingerprint0(
    name, generation, info.updating_key, new_node_uri, info.signing_key,
    info.valid_from, info.digest
)
signature = sign_fingerprint(fingerprint, private_updating_key)

srv.put(name, generation, None, new_node_uri, None, None, info.digest, signature)
```

[1]: https://github.com/MoeraOrg/python-moeralib
[2]: https://pypi.org/project/moeralib/
[3]: /development/node-api/authentication.html
