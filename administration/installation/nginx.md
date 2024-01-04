---
layout: administration
title: Installation
up: installation
subtitle: NGINX
---

# NGINX

## Single node

Here is an example configuration of NGINX to be used as reverse proxy for
`moera-node` in a single node configuration:

```
server {
	listen 443 ssl http2; # managed by Certbot
	listen [::]:443 ssl http2; # managed by Certbot

	server_name blog.moera.org;

	ssl_certificate /etc/letsencrypt/live/blog.moera.org/fullchain.pem; # managed by Certbot
	ssl_certificate_key /etc/letsencrypt/live/blog.moera.org/privkey.pem; # managed by Certbot
	include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
	ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

	root /srv/blog.moera.org/public_html/;
	charset utf-8;
	add_header Strict-Transport-Security "max-age=63072000; includeSubdomains;" always;

    location / {
        if ($request_method = OPTIONS) {
            add_header Access-Control-Allow-Headers "authorization, content-type, x-accept-moera";
            add_header Access-Control-Expose-Headers "x-moera";
            add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE";
            add_header Access-Control-Allow-Origin "*";
            add_header Access-Control-Max-Age 86400;
            add_header Allow "GET, HEAD, POST, PUT, DELETE, OPTIONS, PATCH";
            add_header Strict-Transport-Security "max-age=63072000; includeSubdomains;" always;
            return 200;
        }

    	proxy_set_header X-Forwarded-Proto https;
		proxy_set_header X-Forwarded-Host $host;
		proxy_set_header X-Forwarded-Port 443;
		proxy_set_header X-Forwarded-For $remote_addr;
		proxy_pass http://localhost:8082/;
		client_max_body_size 5m;
	}

	location /moera/api/push/ {
		proxy_pass http://localhost:8082/moera/api/push/;
		proxy_http_version 1.1;
    	proxy_set_header X-Forwarded-Proto https;
		proxy_set_header X-Forwarded-Host $host;
		proxy_set_header X-Forwarded-Port 443;
		proxy_set_header X-Forwarded-For $remote_addr;
		proxy_set_header Connection keep-alive;
		proxy_buffering off;
		proxy_cache off;
		chunked_transfer_encoding off;
		proxy_read_timeout 1h;
		keepalive_timeout 1h;
	}

	location /moera/api/events {
		proxy_pass http://localhost:8082/moera/api/events;
		proxy_http_version 1.1;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection "upgrade";
		proxy_pass_request_headers on;
	}

	location /mediafile/ {
  		internal;
  		alias /srv/moera.blog/media/;
	}

	location /.well-known {
	}

	gzip on;
	gzip_types text/css application/javascript application/json;
	gzip_min_length 10240;

	access_log /srv/blog.moera.org/log/access.log;
	error_log /srv/blog.moera.org/log/error.log warn;
}

server {
	listen 80;
	listen [::]:80;
	server_name blog.moera.org;

	location / {
		return 301 https://web.moera.org;
	}

	location /.well-known {
		root /srv/blog.moera.org/public_html/;
	}
}
```

This configuration uses `blog.moera.org` as a domain name and `/srv/blog.moera.org`
as working directory for `moera-node`. Change this to your domain name and working
directory. 

The configuration is ready for [Let's Encrypt][1] SSL certificates. Use [Certbot][2] 
to download the certificates for your server.

Note `X-Forwarded-*` headers passed to `moera-node`. They are mandatory.

Change `client_max_body_size` to the maximal size of media files you want to upload
to your node. Don't forget to change the `moera-node` [configuration file][3]
accordingly.

`$request_method = OPTIONS` branch is for handling CORS requests. This block is
optional, because `moera-node` can handle CORS requests as well, but handling them
in NGINX is much faster. 

`/moera/api/push/` location is used to serve a stream of push messages.

`/moera/api/events` location is used for WebSockets connection.

`/mediafile/` location is for serving media files from the media directory.
The directory should be made readable by the NGINX process. Don't forget to change
the `moera-node` [configuration file][3] to activate `accel` protocol of serving
media files and to use `/mediafile/` prefix.

## Multiple nodes

Here is an example configuration of NGINX to be used as reverse proxy for
`moera-node` in a multiple node configuration:

```
server {
	listen 80;
	listen [::]:80;
	server_name moera.blog www.moera.blog;

	location / {
		return 301 https://web.moera.org;
	}

	location /.well-known {
		root /srv/moera.blog/public_html/;
	}
}

server {
	listen 443 ssl;
	listen [::]:443 ssl;
	server_name moera.blog www.moera.blog;

	ssl_certificate /etc/letsencrypt/live/moera.blog/fullchain.pem; # managed by Certbot
	ssl_certificate_key /etc/letsencrypt/live/moera.blog/privkey.pem; # managed by Certbot
	include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
	ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

	location / {
		return 301 https://web.moera.org;
	}

	location /.well-known {
		root /srv/moera.blog/public_html/;
	}
}

server {
	listen 443 ssl http2; # managed by Certbot
	listen [::]:443 ssl http2; # managed by Certbot

	server_name *.moera.blog;

	ssl_certificate /etc/letsencrypt/live/moera.blog/fullchain.pem; # managed by Certbot
	ssl_certificate_key /etc/letsencrypt/live/moera.blog/privkey.pem; # managed by Certbot
	include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
	ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

	root /srv/moera.blog/public_html/;
	charset utf-8;
	add_header Strict-Transport-Security "max-age=63072000; includeSubdomains;" always;

	location / {
        if ($request_method = OPTIONS) {
            add_header Access-Control-Allow-Headers "authorization, content-type, x-accept-moera";
            add_header Access-Control-Expose-Headers "x-moera";
            add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE";
            add_header Access-Control-Allow-Origin "*";
            add_header Access-Control-Max-Age 86400;
            add_header Allow "GET, HEAD, POST, PUT, DELETE, OPTIONS, PATCH";
            add_header Strict-Transport-Security "max-age=63072000; includeSubdomains;" always;
            return 200;
        }

    	proxy_set_header X-Forwarded-Proto https;
		proxy_set_header X-Forwarded-Host $host;
		proxy_set_header X-Forwarded-Port 443;
		proxy_set_header X-Forwarded-For $remote_addr;
		proxy_pass http://localhost:8082/;
		client_max_body_size 5m;
	}

	location /moera/api/push/ {
		proxy_pass http://localhost:8082/moera/api/push/;
		proxy_http_version 1.1;
    	proxy_set_header X-Forwarded-Proto https;
		proxy_set_header X-Forwarded-Host $host;
		proxy_set_header X-Forwarded-Port 443;
		proxy_set_header X-Forwarded-For $remote_addr;
		proxy_set_header Connection keep-alive;
		proxy_buffering off;
		proxy_cache off;
		chunked_transfer_encoding off;
		proxy_read_timeout 1h;
		keepalive_timeout 1h;
	}

	location /moera/api/events {
		proxy_pass http://localhost:8082/moera/api/events;
		proxy_http_version 1.1;
		proxy_set_header X-Forwarded-For $remote_addr;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection "upgrade";
		proxy_pass_request_headers on;
	}

	location /mediafile/ {
  		internal;
  		alias /srv/moera.blog/media/;
	}

	location /.well-known {
	}

	gzip on;
	gzip_types text/css application/javascript application/json;
	gzip_min_length 10240;

	access_log /srv/moera.blog/log/access.log;
	error_log /srv/moera.blog/log/error.log warn;
}

server {
	listen 80;
	listen [::]:80;
	server_name *.moera.blog;

	return 301 https://$host$request_uri;
}
```

This configuration is similar to the above. The only important difference is an SSL
certificate — it should be a wildcard certificate to include all subdomains that may
be created.

[1]: https://letsencrypt.org/
[2]: https://certbot.eff.org/
[3]: /administration/installation/config#media-files
