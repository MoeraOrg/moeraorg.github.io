---
layout: development
title: Development Environment
body_class: body-pink
---

# Development Environment

To work with Moera, you need four components. You don't need to build
and install all of them - you may use those that are publicly available,
until you plan to make changes to the code. These components are:

1. **Naming service.** By default, [naming.moera.org][11] is used. For
   development, build and run [moera-naming][3] (see [README.md][4] for
   details).
2. **Node.** You may get one from [moera.blog][16] provider. For
   development, build and run [moera-node][5] (see [README.md][6] for
   details).
3. **Client.** If you have the browser extension installed (see below),
   it uses the client at [client.moera.org][12] by default. Without the
   browser extension you can use [web.moera.org][17] standalone client.
   For development, build and run [moera-client-react][7] (see
   [README.md][8] for details).
4. (Optional) **Browser extension.** Install from the [Firefox][13] or
   [Chrome][15] store. For development, build and install
   [moera-browser-extension][9] (see [README.md][10] for details).

Naming service and node use [moera-commons][1] package. By default, it
is downloaded from GitHub Maven repository, but you can build and
install it, if you need to modify it (see [README.md][2] for details).

For local installation of naming and node servers you need to have Java
11+ and PostgreSQL 9.6+ installed. In all major Linux distributions you
can install them from the main package repository. For development
purposes, you can use one PostgreSQL instance for both node and naming
servers.

If you install several components on the same host, note to choose
different port numbers for them. By default, they are 8080, 8081 and
3000 for naming, node and client respectively.

#### Note about HTTPS

If a page is served over HTTPS, modern browsers do not allow it to fetch
unencrypted content by HTTP (see [mixed active content][14]). Since we
strongly recommend Moera nodes to serve all content over HTTPS, the
client code must also be served over HTTPS, otherwise browser will not
allow it to be injected into the page. It is also not possible to access
a naming server by HTTP and to connect to home node by HTTP.

You need to take this into account when building a development
environment. If you run a development server that serves
[moera-client-react][7] over HTTP, you will not be able to open HTTPS
nodes with it. Using a local HTTP node for development will solve the
problem.

[1]: https://github.com/MoeraOrg/moera-commons
[2]: https://github.com/MoeraOrg/moera-commons/blob/master/README.md
[3]: https://github.com/MoeraOrg/moera-naming
[4]: https://github.com/MoeraOrg/moera-naming/blob/master/README.md
[5]: https://github.com/MoeraOrg/moera-node
[6]: https://github.com/MoeraOrg/moera-node/blob/master/README.md
[7]: https://github.com/MoeraOrg/moera-client-react
[8]: https://github.com/MoeraOrg/moera-client-react/blob/master/README.md
[9]: https://github.com/MoeraOrg/moera-browser-extension
[10]: https://github.com/MoeraOrg/moera-browser-extension/blob/master/README.md
[11]: http://naming.moera.org/
[12]: https://client.moera.org/
[13]: https://addons.mozilla.org/en-US/firefox/addon/moera/
[14]: https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content
[15]: https://chrome.google.com/webstore/detail/moera/endpkknmpgamhhlojbgifimfcleeeghb
[16]: https://moera.blog
[17]: https://web.moera.org
