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

#### Secure context (HTTPS)

Some browser APIs require a secure context (HTTPS). For example, those working
with the clipboard. For this purpose, you may configure your local development
environment to serve the client over HTTPS as described below.

If the client is served over HTTPS, modern browsers do not allow fetching
unencrypted content by HTTP (see [mixed active content][8]). It means that
Moera nodes must also be served over HTTPS; otherwise the browser will not
allow the client to access nodes. It also will not be possible to access
a naming server by HTTP.

The simplest way to serve the client over HTTPS is to use a self-signed
certificate. `mkcert`[11] is a great tool for this purpose. If you did not use
it before, install it and run `mkcert -install` to create the root certificate
authority (CA) in your system trust store. After that, run `mkcert localhost` to
create a certificate for `localhost`, or use any other domain name you want.

To enable HTTPS in the client, create `.ssl/` directory in the client root and
copy the certificate and key files to it. `run` script will detect this
directory automatically and enable the HTTPS configuration.

For the node, you will need to add the following settings to
`application-dev.yml`:

```yaml
server:
  ssl:
     enabled: true
     certificate: "file:.ssl/localhost.pem"
     certificate-private-key: "file:.ssl/localhost-key.pem"
```

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
[11]: https://github.com/FiloSottile/mkcert
