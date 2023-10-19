---
layout: administration
title: Tools
up: tools
subtitle: Configuration File
---

# Configuration File

Moera tools configuration file is named `.moerc` and located in the current user's
home directory. It is strongly recommended to make it readable by the owner only
(on Unix-like systems, set file permissions to `600`).

The file has INI format, similar to the following:

```
[default]

[moera.blog]
domain = moera.blog
node-name = lamed
token = zzzzzzzzzzzzzzzzzzzzzzzz

[local]
domain = localhost.localdomain:8082
naming-server = development
node-name = balu-dev
secret = ooooooooooooooooooooooooo
```

## Sections

Each section of the configuration file corresponds to a particular _provider_ or
server and contains settings specific to that provider. But if you often administer
several nodes at the same provider, you can create a separate section for each node.
A special section `[default]` contains the default settings for all providers.

## Variables

`naming-server = <URL> | main | development | dev`

: URL of the Moera naming server to be used. A special keyword `main` means the Moera
  main naming server (`naming.moera.org`). A special keyword `development` (or `dev`)
  means Moera development naming server (`naming-dev.moera.org`).

: This is the only variable that may appear in the `[default]` section.

`domain = <domain name>`

: The domain provider is located at. Usually each node located at the provider gets
  a subdomain of this domain. Moera tools use this fact to select a provider
  automatically by the node URL.

`node-name = <name>`

: The name of the node that is used by default if no node is specified in the command
  line.

`node-url = <URL>`

: URL of the node that is used by default if no node is specified in the command
  line. If both `node-name` and `node-url` are specified, `node-url` has a priority.

`secret = <root secret>`

: Secret to be used to authenticate as a root admin.

`token = <token>`

: Token to be used to authenticate as a node admin.
