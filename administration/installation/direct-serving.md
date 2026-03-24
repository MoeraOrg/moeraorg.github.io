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

To activate direct serving, set `node.media.direct-serve.source` option to
`filesystem` in the Moera node [configuration file][2] and define the secret
key:

```yaml
node:
  media:
    direct-serve:
      source: filesystem
      secret: "A long and random string"
```

After that, restart `moera-node`.

Direct serving from the filesystem uses the **presigned URLs** approach.
REST API calls for postings and comments return direct URLs to the media files
signed by the secret key. The signature is generated using the `hmac-sha256`
algorithm. The URLs contain a timestamp and are valid for a limited period of
time. 

When the media file is requested, NGINX validates the signature and
the timestamp before serving the file.

## Configure NGINX

Signature validation is written in NJS, so you need to install and enable
[ngx_http_js_module][3] in NGINX. Download the verification script from
[GitHub][4] and place it in `/etc/nginx/njs`.

For security reasons, it is not recommended to put the secret key in the
configuration file. Create a file `/etc/nginx/secrets/my-node.conf` and put
the secret key there:

```
set $secure_link_secret "A long and random string";
```

Make sure that the key is the same as defined in the node configuration file.
Set the file permissions to `0600` and change its owner to `root:root`.

The final step, to serve the files from the filesystem, add the following
snippet to your NGINX configuration:

```
server {
    location ~ ^/moera/media/([^/]+)\.([^/]+)$ {
        if ($request_method = OPTIONS) {
            add_header Access-Control-Allow-Headers "authorization, content-type, x-accept-moera, client-id";
            add_header Access-Control-Expose-Headers "x-moera";
            add_header Access-Control-Allow-Methods "GET";
            add_header Access-Control-Allow-Origin "*";
            add_header Access-Control-Max-Age 86400;
            add_header Allow "GET, HEAD, OPTIONS";
            add_header Strict-Transport-Security "max-age=63072000; includeSubdomains;" always;
            return 200;
        }

        js_import sec from "/etc/nginx/njs/secure-link.js";
        include /etc/nginx/secrets/my-node.conf;
        set $id $1;
        js_set $valid sec.secure_link;
        if ($valid = bad) {
            return 403;
        }
        if ($valid = expired) {
            return 410;
        }

        alias /srv/moera.blog/media/$1.$2;
        add_header Access-Control-Allow-Origin "*";
        if ($arg_download) {
            add_header Content-Disposition "attachment; filename=$1.$2";
        }
        expires max;
    }
}

```

This configuration uses `/srv/blog.moera.org/media` as a media directory for
`moera-node`. Change this to your media directory.

[1]: nginx.html
[2]: config.html
[3]: https://nginx.org/en/docs/http/ngx_http_js_module.html
[4]: https://github.com/MoeraOrg/moera-node/blob/master/nginx/secure-link.js
