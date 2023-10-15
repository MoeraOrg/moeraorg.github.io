---
layout: administration
title: Installation
up: installation
subtitle: Logrotate
---

# Logrotate

Use this configuration for `logrotate` to rotate NGINX logs.

```
/srv/moera.blog/log/access.log /srv/moera.blog/log/error.log {
        daily
        missingok
        rotate 20
        compress
        delaycompress
        notifempty
        sharedscripts
        prerotate
                if [ -d /etc/logrotate.d/httpd-prerotate ]; then \
                        run-parts /etc/logrotate.d/httpd-prerotate; \
                fi \
        endscript
        postrotate
                /usr/sbin/nginx -s reload
        endscript
}
```
