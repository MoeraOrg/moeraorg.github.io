---
layout: administration
title: Tools
up: tools
subtitle: Configuration File
---

# Configuration File

The `moctl` command reads configuration from a file named `.moerc` in the
current user's home directory. It is strongly recommended to make it readable
by the owner only (on Unix-like systems, set file permissions to `600`).

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

Command-line options override values loaded from the file.

## Sections

Each section of the configuration file corresponds to a particular _provider_ or
server and contains settings specific to that provider. If you often administer
several nodes at the same provider, you can create a separate section for each
node.

A special section `[default]` contains global defaults. If `-P/--provider` is
not passed explicitly, `moctl` first tries to pick a section by matching the
node address against `domain = ...`; if there is no match, it falls back to the
first non-default section in the file.

## Variables

`naming-server = <URL> | main | development | dev`

: URL of the Moera naming server to be used. A special keyword `main` means the Moera
  main naming server (`naming.moera.org`). A special keyword `development` (or `dev`)
  means Moera development naming server (`naming-dev.moera.org`).

: This is the only variable read from the `[default]` section. In a provider
  section, it overrides the global default for that provider.

`domain = <domain name>`

: The domain the provider is located at. Usually each node located at the
  provider gets a subdomain of this domain. `moctl` uses this fact to select a
  provider automatically by the node URL or the URL resolved from `node-name`.

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
