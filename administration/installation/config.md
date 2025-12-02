---
layout: administration
title: Installation
up: installation
subtitle: Configuration File
---

# Configuration File

Moera node configuration file is a YAML file containing configuration options.
The file should be placed in the `moera-node` working directory and named
`application-prod.yml` for the production server or `application-dev.yml` for
the development server.

Configuration options have names like `node.registrar.domain`. In the configuration
file they may be set in two forms:

```yaml
node.registrar.domain: moera.blog
```

Or

```yaml
node:
  registrar:
    domain: moera.blog
```

#### Minimal configuration

Here is a minimal configuration file you may use as a basis for your configuration:

```yaml
server:
  port: 8081

spring:
  datasource:
    url: jdbc:postgresql:<DB name>?characterEncoding=UTF-8
    username: <DB username>
    password: <DB password>

  flyway:
    user: <DB username>
    password: <DB password>

node:
  root-secret: <secret>
  mail:
    reply-to-address: <mailrobot e-mail address>
    root-address: <admin e-mail address>
  media:
    path: media/
```

See the explanation of these and other options below.

## Server

All [server properties][1] are listed in Spring Boot documentation. The built-in web
server used by `moera-node` is Tomcat.

```yaml
server.port: 8080
```

Server HTTP port.

```yaml
server.tomcat.max-swallow-size: 2MB
```

Maximum amount of request body to swallow. Increase this number to support uploading
large files.

## Database

All [data properties][2] are listed in Spring Boot documentation. You need to set
[data migration properties][3] as well to allow `moera-node` to create the database
structure automatically.

```yaml
spring.datasource.url: jdbc:postgresql:<DB name>?characterEncoding=UTF-8
```

JDBC URL of the database.

```yaml
spring.datasource.username: <DB username>
```

Login username of the database.

```yaml
spring.datasource.password: <DB password>
```

Login password of the database.

```yaml
spring.flyway.user: <DB username>
```

Login user of the database to migrate.

```yaml
spring.flyway.password: <DB password>
```

Login password of the database to migrate.

## Authentication

```yaml
node.root-secret: <secret>
```

A long random sequence of characters that is used to authenticate as a topmost
administrator (root admin) of the server.

```yaml
node.address: <IP address>
```

IP address of the server visible to the clients. In most cases, there is no need
to configure it, since the address is detected automatically. But on servers having
several uplinks, it may be necessary to set the address explicitly. 

```yaml
node.encryption-key: <key>
```

BASE64-encoded AES encryption key that will be used to encrypt sensitive
information in the database.

## Media files

```yaml
node.media.path: media/
```

Location of the directory where media files are stored. The directory must be
readable and writable by `moera-node` process. The path is relative to
`moera-node` working directory.

```yaml
node.media.serve: stream
```

This option defines how media files are served to the client. The possible values
are:
* `stream` — the file is streamed to the client directly;
* `sendfile` — the file's location is passed back to the proxying web server in
  `X-Sendfile` header (used by Apache);
* `accel` — the file's location is passed back to the proxying web server in
  `X-Accel-*` headers (used by NGINX).

```yaml
node.media.accel-prefix: /mediafile/
```

If `node.media.serve` is set to `accel`, this option sets a prefix added to
the names of media files. This prefix is then used in NGINX configuration to
configure serving media files from the media files directory. 

```yaml
node.media.direct-serve: false
```

If `true`, enables [serving media files directly][6] from the filesystem.

## OCR service

Configuration of a third-party service that is used to recognize text in images.
The recognized text may be used in notifications and search.

```yaml
media.ocr.service: <service type>
```

Type of the service. The possible values are:
* `ocrspace` — [OCR.space][9] service.

```yaml
media.ocr.service-key: <service key>
```

The API key of the service.

## Multiple domains

`moera-node` allows to run several nodes on a single server instance. Each node
should have a separate domain name. Depending on the configuration, nodes may be
created only by the server administrator, or by any user.

The node named `_default_` is created automatically during the installation. If you
have no plans to run several nodes, the default node is all you need.

```yaml
node.multi: none
```

Activates the multi-node mode. The possible values are:
* `none` — single node mode (you also need to set `node.domain`);
* `private` — multi-node mode, only the server administrator may create new nodes
  (you also need to set `node.registrar.domain`);
* `public` — multi-node mode, any user may create a node (you also need to set
  `node.registrar.host` and `node.registrar.domain`).

```yaml
node.domain: <domain name>
```

If `node.multi` is set to `none`, this option defines domain name of the single node.

```yaml
node.registrar.host: <host name>
```

If `node.multi` is set to `public`, this option defines the host name of the built-in
web interface for creating nodes. If a user opens a subdomain that has no node
defined for it, they are redirected automatically to the web interface for creating
the node. 

```yaml
node.registrar.domain: <domain name>
```

If `node.multi` is set to `private` or `public`, this option defines the name of
the domain where subdomains are created for the new nodes. Note that `moera-node`
cannot register subdomains in DNS by itself, so you need to have a wildcard
subdomain defined on the DNS server. Or you can add subdomains manually for every
node.

## Mail

All [mail properties][4] are listed in Spring Boot documentation. In addition, there
are several properties specific to `moera-node`.

```yaml
spring.mail.host: localhost
```

SMTP server host.

```yaml
spring.mail.port: 2525
```

SMTP server port.

```yaml
spring.mail.username: <username>
```

Login user of the SMTP server.

```yaml
spring.mail.password: <password>
```

Login password of the SMTP server.

```yaml
spring.mail.properties.*
```

Additional [JavaMail properties][5].

```yaml
spring.mail.properties.mail.smtp.auth: false
```

If `true`, attempt to authenticate the user using the `AUTH` command.

```yaml
spring.mail.properties.mail.smtp.starttls.enable: false
```

If `true`, enables the use of the `STARTTLS` command (if supported by the server)
to switch the connection to a TLS-protected connection before issuing any login
commands.

```yaml
node.mail.send-limit: 10
node.mail.send-period: 10
```

Limit the rate of outbound mail to `node.mail.send-limit` mails in
`node.mail.send-period` minutes.

```yaml
node.mail.reply-to-address: mailrobot@myblog.com
```

The e-mail address that is put to the `Reply-To:` header in outgoing mails.

```yaml
node.mail.root-address: myblog-admin@gmail.com
```

E-mail address of the server's administrator.

## FCM relay

```yaml
node.fcm-relay: https://fcm.moera.org/moera-push-relay
```

API endpoint of the relay used to send push notifications to mobile devices.
[Read more][7] in the Developer's Guide.

## Link preview service

Configuration of a third-party service that creates previews for links. This
service may be used instead of the built-in one for some domains.

```yaml
node.link-preview.service: <service type>
```

Type of the service. The possible values are:
* `linkpreviewnet` — [LinkPreview][8] service.

```yaml
node.link-preview.service-key: <service key>
```

The API key of the service.

```yaml
node.link-preview.domains: []
```

The list of regular expression patterns matching domains. Previews of the links
in these domains will be constructed with the third-party service instead of
the built-in one.

## IndexNow service

IndexNow is an easy way for websites to instantly inform search engines
(like Bing, for example) about the latest content changes. In its simplest form,
IndexNow is a simple ping so that search engines know that URL and its content
have been added, updated, or deleted, allowing search engines to quickly reflect
this change in their search results.

```yaml
node.index-now.endpoint: https://api.indexnow.org/indexnow
```

Endpoint to be used for submitting URLs to IndexNow. All IndexNow endpoints are
created equal, so it is unlikely that you will need to change the default.

```yaml
node.index-now.key: <service key>
```

The API key is needed to match the ownership of the domain with submitted URLs.
You can get it on [Bing website][10] or from any other IndexNow-enabled search
engine.

## Settings

It is possible to use the configuration file to override the built-in default values
of the node settings. This will affect all nodes in the server.

The settings are given as a list of name-value pairs:

```yaml
node:
  options:
    - name: posting.max-size
      defaultValue: 65536
    - name: posting.subject.present
      defaultValue: true
```

## Thread pools

These options set the number of threads in the thread pools used by `moera-node` for
various purposes. A larger number increases memory usage and the peak load on
the server but allows running more tasks in parallel.

```yaml
node.pools.naming: 16
```

The pool used to resolve node names with Moera naming service.

```yaml
node.pools.notification-sender: 32
```

The pool used to send notifications to other nodes.

```yaml
node.pools.picker: 12
```

The pool used to fetch posts from other nodes.

```yaml
node.pools.push: 4
```

The pool used to push notifications to clients.

```yaml
node.pools.remote-task: 16
```

The pool used for unspecified background tasks.

## Logging

```yaml
logging.file.max-history: 10
```

Number of old log files that are preserved.

## Debugging

```yaml
node.mock-network-latency: false
```

If set to `true`, a random delay is added before answering to any request,
to simulate network latency.

```yaml
node.log-slow-requests: false
```

If set to `true`, a special message will be added to the node log if a slow API
request is detected.

```yaml
node.slow-request-duration: 500
```

The API request execution time threshold (in milliseconds). If a request takes
more time to execute, it is logged as a slow one (see above).

[1]: https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#appendix.application-properties.server
[2]: https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#appendix.application-properties.data
[3]: https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#appendix.application-properties.data-migration
[4]: https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#application-properties.mail.spring.mail.properties
[5]: https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html
[6]: direct-serving.html
[7]: https://moera.org/development/push-relay-api.html
[8]: https://www.linkpreview.net/
[9]: https://ocr.space/
[10]: https://www.bing.com/indexnow/getstarted#implementation
