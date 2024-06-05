---
layout: administration
title: Installation
---

# Installation

The simplest way to install the Moera server software (`moera-node`) is as follows:

1. Download a prebuilt WAR file [from the GitHub repository][1].
2. Place the WAR file in a directory on your server.
3. Create a subdirectory to store media files. The directory must be
   readable and writable by `moera-node` process.
4. Create a [PostgreSQL database][2].
5. Create a [configuration file][3].
6. [Run][4] the server.
7. Configure [NGINX as a reverse proxy][5].
8. _(recommended)_ Configure [direct serving of media files][6].
9. _(optional)_ Configure a [watchdog][7].
10. _(optional)_ Configure [logrotate][8].


[1]: https://github.com/MoeraOrg/moera-node/releases
[2]: /administration/installation/create-db.html
[3]: /administration/installation/config.html
[4]: /administration/installation/running.html
[5]: /administration/installation/nginx.html
[6]: /administration/installation/direct-serving.html
[7]: /administration/installation/watchdog.html
[8]: /administration/installation/logrotate.html
