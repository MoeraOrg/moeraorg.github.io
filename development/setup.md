---
layout: development
title: Development Environment
body_class: body-pink
---

# Development Environment

As prerequisites you need to have OpenJDK 8+ and PostgreSQL 10+
installed. In all major Linux distributions you can install them from
the main package repository.

For development purposes, you can use one PostgreSQL instance for both
node and naming servers.

To setup:

1. Build and install [moera-commons][1] (see [README.md][2] for
   details). 
2. Choose separate port numbers for naming server, node and client.
   These ports must be free on your development machine.
3. Build and run [moera-naming][3] (see [README.md][4] for details).
4. Build and run [moera-node][5] (see [README.md][6] for details).
5. Build and run [moera-client][7] (see [README.md][8] for details).
6. Build and install [moera-browser-extension][9] (see [README.md][10]
   for details).
7. Open the main page of the node in your browser.

[1]: https://github.com/MoeraOrg/moera-commons
[2]: https://github.com/MoeraOrg/moera-commons/blob/master/README.md
[3]: https://github.com/MoeraOrg/moera-naming
[4]: https://github.com/MoeraOrg/moera-naming/blob/master/README.md
[5]: https://github.com/MoeraOrg/moera-node
[6]: https://github.com/MoeraOrg/moera-node/blob/master/README.md
[7]: https://github.com/MoeraOrg/moera-client
[8]: https://github.com/MoeraOrg/moera-client/blob/master/README.md
[9]: https://github.com/MoeraOrg/moera-browser-extension
[10]: https://github.com/MoeraOrg/moera-browser-extension/blob/master/README.md
