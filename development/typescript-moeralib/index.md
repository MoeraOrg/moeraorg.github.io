---
layout: development
title: TypeScript Library
---

# TypeScript Library

`moeralib` ([GitHub][1]) is a library that allows TypeScript (or JavaScript)
applications for Node.js to easily interact with the Moera network.

The easiest way to install the library is from [npm repository][2]:

```
npm install moeralib
```

## Naming API

<code><a href="naming.html">moeralib/naming</a></code> module contains classes and
routines for interacting with Moera naming service. To access a naming server, create
`MoeraNaming` class and pass the naming server URL in the parameters. There are
constants for two well-known servers: `MAIN_NAMING_SERVER` and `DEV_NAMING_SERVER`.
The first one is used by default by `MoeraNaming`.

```typescript
import { MoeraNaming, DEV_NAMING_SERVER } from 'moeralib/naming';

const naming = new MoeraNaming(DEV_NAMING_SERVER);
const info = naming.getCurrent('balu-dev', 0);
console.log(info.nodeUri);
```

A shortcut function `resolve()` simplifies resolving of names.

```typescript
import { resolve, DEV_NAMING_SERVER } from 'moeralib/naming'; 

console.log(resolve('balu-dev_0', DEV_NAMING_SERVER));
```

## Node API

<code><a href="node.html">moeralib/node</a></code> module contains classes and
routines for accessing Moera nodes. Just create `MoeraNode` class with the URL of
the node, and call the methods you need.

```typescript
import { resolve } from 'moeralib/naming';
import { MoeraNode } from 'moeralib/node'; 

const node = new MoeraNode(resolve('Alice'));
console.log(node.whoAmI().fullName);
```

The library automatically parses JSON structures coming from the node and
converts them to JavaScript objects. The corresponding types are defined in
`moeralib/naming/types` and `moeralib/node/types` submodules.

```typescript
const attrs: DomainAttributes = {
    name: 'dave.moera.club',
    nodeId: DAVE_NODE_ID
};
```

## Authentication

_[Read more about authentication][3] in the Node API reference._

To perform an authenticated request, you need to put the root secret, token, or carte
into `MoeraNode` and activate the corresponding authentication mode. Use
`rootSecret()`, `token()`, and `carte()` methods to set the root secret, token, and
carte correspondingly. The authentication mode is activated by generic
`authMethod()`, or by shortcut methods `noAuth()`, `auth()`, `authAdmin()`,
`authRootAdmin()`. After that, all API requests will be authenticated with
the selected method, if needed. You can switch to a different method at any time.

```typescript
import { resolve } from 'moeralib/naming';
import { MoeraNode } from 'moeralib/node';

const node = new MoeraNode(resolve('Alice'));
node.token('putthetokenhere');
node.authAdmin();
console.log(node.getProfile().email);
```

## Managing cartes

`MoeraCarteSource` class simplifies managing authentication cartes. It obtains cartes
from a home node, caches them, supplies valid cartes for authentication, and requests
new ones when old ones expire.

```typescript
import { resolve } from 'moeralib/naming';
import { MoeraCarteSource, MoeraNode } from 'moeralib/node';

const home = new MoeraNode(resolve('Alice'));
home.token('putthetokenhere');
home.authAdmin();

const node = new MoeraNode(resolve('Bob'));
node.carteSource(new MoeraCarteSource(home));
node.auth();
const slice = node.getFeedSlice('timeline');
for (const story of slice.stories) {
    if (story.posting != null) {
        console.log(story.posting.operations.view, story.posting.heading);
    }
}
```

## Universal URLs

<code><a href="universal_location.html">moeralib/universal-location</a></code>
module contains classes and routines for creating and parsing Moera universal
URLs.

To parse a universal URL, pass it to `parse()` function. It returns a
`UniversalLocation` instance containing the result of parsing.

```typescript
import { parse } from 'moeralib/universal-location';

const uni = parse('https://moera.page/@Alice/alice.moera.blog/post/69a403ef-b72d-43e0-967e-eab5e8dce9d3');
console.log(uni.nodeName, uni.authority, uni.path, uni.toString());
```

To build a universal URL from parts, use `redirectTo()` function.

```typescript
import { redirectTo } from 'moeralib/universal-location';

console.log(redirectTo(
    'Alice_0',
    'https://alice.moera.blog/',
    '/post/69a403ef-b72d-43e0-967e-eab5e8dce9d3'
));
```

`redirectToUrl()` function converts URL of a page on a node to a corresponding
universal URL.

```typescript
import { redirectToUrl } from 'moeralib/universal-location';

console.log(redirectToUrl(
    'Alice_0',
    'https://alice.moera.blog/moera/post/69a403ef-b72d-43e0-967e-eab5e8dce9d3'
));
```

[1]: https://github.com/MoeraOrg/typescript-moeralib
[2]: https://www.npmjs.com/package/moeralib
[3]: /development/node-api/authentication.html
