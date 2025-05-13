---
layout: development
title: Development Environment
---

# Development Environment

To start working with Moera, you need at least three components. You don't need
to build and install all of them — you may use those that are publicly available 
until you plan to make changes to the code. These components are:

1. **Naming service.** By default, [naming-dev.moera.org][7] is used. For
   development, build and run [moera-naming][1] (see [README.md][2] for
   details).
2. **Node.** You may get one from [moera.blog][9] provider. For
   development, build and run [moera-node][3] (see [README.md][4] for
   details).
3. **Client.** By default, [web.moera.org][10] client is used. For development,
   build and run [moera-client-react][5] (see [README.md][6] for details).

For local installation of naming and node servers, you need to have Java
17+ and PostgreSQL 9.6+ installed. In all major Linux distributions, you
can install them from the main package repository. For development, you can use
one PostgreSQL instance for both node and naming servers.

If you install several components on the same host, note to choose
different port numbers for them. By default, they are 8080, 8081 and
3000 for naming, node and client respectively.

#### Note about HTTPS

If a page is served over HTTPS, modern browsers do not allow it to fetch
unencrypted content by HTTP (see [mixed active content][8]). Since we
strongly recommend Moera nodes to serve all content over HTTPS, the
client code must also be served over HTTPS; otherwise the browser will not
allow it to be injected into the page. It is also not possible to access
a naming server by HTTP and to connect the home node by HTTP.

You need to take this into account when building a development
environment. If you run a development server that serves
[moera-client-react][5] over HTTP, you will not be able to open HTTPS
nodes with it. Using a local HTTP node for development will solve the
problem.

[1]: https://github.com/MoeraOrg/moera-naming
[2]: https://github.com/MoeraOrg/moera-naming/blob/master/README.md
[3]: https://github.com/MoeraOrg/moera-node
[4]: https://github.com/MoeraOrg/moera-node/blob/master/README.md
[5]: https://github.com/MoeraOrg/moera-client-react
[6]: https://github.com/MoeraOrg/moera-client-react/blob/master/README.md
[7]: http://naming-dev.moera.org/
[8]: https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content
[9]: https://moera.blog
[10]: https://web.moera.org
