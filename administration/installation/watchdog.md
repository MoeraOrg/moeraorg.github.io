---
layout: administration
title: Installation
up: installation
subtitle: Watchdog
---

# Watchdog

[Monit][1] is a simple watchdog that can be used to monitor the `moera-node` process
and restart it, if needed. For example, it may periodically check that some post
in a blog is accessible.

Here is an example configuration:

```
check process moera-blog matching "java.*moera.blog/moera-node"
  start program = "/bin/systemctl start moera-blog.service"
  stop program = "/bin/systemctl stop moera-blog.service"
  restart program = "/bin/systemctl restart moera-blog.service"
  if failed
    port 443
    protocol https
    http headers [Host: lamed.moera.blog]
    request "/post/f6ee6a75-c9d9-4216-f50b-b2e65eb00442"
    status = 200
    for 2 cycles
  then restart
  alert balu@moera.org
```

Change it for your server as needed.

[1]: https://mmonit.com/monit/
