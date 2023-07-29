---
layout: development
title: Protocols
up: protocols
subtitle: Access Controls
body_class: body-pink
redirect_from:
  - /development/protocols/carte.html
---

# Access Controls

## Authentication

### Carte

**Carte** (from *carte-de-visite*) is a cryptographic token that allows
client to authenticate on any node besides the home node. Since the
client does not have access to the private signing key (giving such
access would weaken the security), it would need to ask the home node to
sign every request that needs authentication or to perform
authentication on every node individually. Carte is a compromise between
security and performance, it gives acceptable user experience,
minimizing damage if some cartes are leaked.

After authentication on the home node, the client requests a set of
cartes. Each carte is a BASE64-encoded array of bytes that is a
concatenation of
[CarteFingerprint](/development/protocols/node-api-fingerprints.html#CarteFingerprint)
and its signature.

```
carte = fingerprint + signature
```

The fingerprint contains the name of the home node, the IP address of
the client, beginning and end timestamps of the carte's life and a
random salt. Binding to time and IP address minimizes ability of an
attacker to use a carte that was intercepted somehow. For the same
reason it is recommended to use cartes with a short lifetime (several
minutes). If a client needs to work longer, it can request several
cartes in a single request that correspond to successive periods of
time. When one carte expires, the client throws it off and uses the next
one in the sequence.

If client wants to post a content (comment, reaction etc.) to a node,
carte authentication is not enough, because the content needs its own
signature. To give better user experience, the client may use carte to
post a temporary content without a signature and then ask the home node
to post its signed version. If during a short period of time the signed
content do not arrive, the node erases the temporary version.
