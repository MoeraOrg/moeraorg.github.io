---
layout: administration
title: Installation
up: installation
subtitle: Direct Serving Of Media Files
---

# Direct Serving Of Media Files

To speed up the serving of media files to the client, it is recommended
to configure the server to serve images directly from the local file system,
without accessing the node. As a prerequisite, you need to [configure a web
server][1] (like NGINX) as a reverse proxy for `moera-node`.

## Configure the node

To activate direct serving, turn `node.media.direct-serve` option on in the
Moera node [configuration file][2]:

```yaml
node:
  media:
    direct-serve: true
```

After that, restart `moera-node`. The node will detect the option and will
create `public/` and `private/` subdirectories in your media directory (see
`node.media.path` option). These subdirectories will be populated with symlinks
to public and private media files respectively. The private media files get
a random name that periodically changes to prevent unauthorized access.

The process of creating symlinks will take some time, but you do not need to
wait till it finishes. The media files that do not have a symlink yet will be
served normally through the node.

## Configure NGINX

To serve the files from the filesystem, add the following snippets to your NGINX
configuration:

```
server {
    location /moera/media/public/ {
        if ($request_method = OPTIONS) {
            add_header Access-Control-Allow-Headers "authorization, content-type, x-accept-moera";
            add_header Access-Control-Expose-Headers "x-moera";
            add_header Access-Control-Allow-Methods "GET";
            add_header Access-Control-Allow-Origin "*";
            add_header Access-Control-Max-Age 86400;
            add_header Allow "GET, HEAD, OPTIONS";
            add_header Strict-Transport-Security "max-age=63072000; includeSubdomains;" always;
            return 200;
        }
        rewrite /([\w-]+)=\.(\w+)$ /$1.$2 permanent;
        alias /srv/moera.blog/media/public/;
        add_header Access-Control-Allow-Origin "*";
        expires max;
    }

    location ~ ^/moera/media/private/([^/]+_[^/]+)$ {
        if ($request_method = OPTIONS) {
            add_header Access-Control-Allow-Headers "authorization, content-type, x-accept-moera";
            add_header Access-Control-Expose-Headers "x-moera";
            add_header Access-Control-Allow-Methods "GET";
            add_header Access-Control-Allow-Origin "*";
            add_header Access-Control-Max-Age 86400;
            add_header Allow "GET, HEAD, OPTIONS";
            add_header Strict-Transport-Security "max-age=63072000; includeSubdomains;" always;
            return 200;
        }
        alias /srv/moera.blog/media/private/$1;
        add_header Access-Control-Allow-Origin "*";
        if ($arg_download) {
                add_header Content-Disposition "attachment";
        }
        expires max;
    }
}

```

This configuration uses `/srv/blog.moera.org/media` as a media directory for
`moera-node`. Change this to your media directory.

[1]: nginx.html
[2]: config.html
