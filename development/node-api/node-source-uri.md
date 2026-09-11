---
layout: development
title: Node API
up: node-api
subtitle: Node Source URI
---

# Node Source URI

A node source URI identifies the source of node identity. It may include an
ordered set of parameters after the URI:

```text
<uri>;<parameter-name>=<parameter-value>;...
```

The first semicolon ends the URI and starts the parameter block. Equal signs
before the first semicolon are part of the URI. A URI assigned programmatically
must not contain a semicolon.

Each segment after the URI is a parameter. The first equal sign in the segment
separates its name from its value. A segment without an equal sign has an empty
value. A parameter with an empty name is ignored. When a name occurs more than
once, its last value is used while its first position is retained.

Parameter names and values use UTF-8 percent-encoding according to RFC 3986.
Only letters, digits, `-`, `.`, `_`, and `~` are left unescaped. A space is
encoded as `%20`; a plus sign is encoded as `%2B` and never represents a space.
Serializers use uppercase hexadecimal digits and always include the equal sign,
including for an empty value.

Parsers preserve malformed percent escapes literally. For example, `%ZZ`
decodes to `%ZZ` and is serialized again as `%25ZZ`. Escaped bytes that are not
valid UTF-8 decode to the Unicode replacement character.

For example:

```text
https://example/node;via_email=alice%40example.com;label=%D0%9C%D0%B8%D1%80%20%2B
```

has URI `https://example/node`, parameter `via_email` with value
`alice@example.com`, and
parameter `label` with value `Мир +`.

`via_email` is currently the only parameter name defined by Moera libraries.
The `NodeSourceUri` utility preserves all other parameters without interpreting
them.
