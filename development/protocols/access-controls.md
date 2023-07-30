---
layout: development
title: Protocols
up: protocols
subtitle: Access Controls
body_class: body-pink
---

# Access Controls

Access to some Node API calls is restricted and the client should authenticate
to use them.

## Authentication

To authenticate, the client should provide a corresponding authentication token
or sign the request body with the home node's private signing key.

<a name="tokens"></a>
### Types of tokens

#### Root secret

_Root secret_ is set in the server configuration and is used to authenticate as
a topmost administrator _(root admin)_ of the server.

#### Admin token

_Admin token_ is used to authenticate as administrator on the home node.
The client should get login and password from the user and then
[call Node API](node-api.html#Tokens%20object) to generate the token.

<a name="carte"></a>
#### Carte

_Carte_ (from *carte-de-visite*) is a cryptographic token that allows
client to authenticate on any node besides the home node.

Nodes in Moera use public key cryptography to authenticate one another. Since
the client does not have access to the private signing key (giving such
access would weaken the security), it would need to ask the home node to
sign every request that needs authentication or to perform
authentication on every node individually. Carte is a compromise between
security and performance, it gives acceptable user experience, while
minimizing damage if some cartes are leaked.

After authentication on the home node, the client [requests a set of
cartes](node-api.html#Cartes%20object). Each carte is a BASE64-encoded array of
bytes that is a concatenation of
[CarteFingerprint](node-api-fingerprints.html#CarteFingerprint) and its signature.

```
carte = fingerprint + signature
```

The fingerprint contains the name of the home node, the IP address of the client,
optional name of the target node, beginning and end timestamps of the carte's life
and a random salt. Binding to time, IP address and target node minimizes ability
of an attacker to use a carte that was intercepted somehow. For the same reason
it is recommended to use cartes with a short lifetime (several minutes).
If the client needs to work longer, it can request several cartes in a single
request that correspond to successive periods of time. When one carte expires,
the client throws it off and uses the next one in the sequence.

### Signature

If the client wants to post a content (comment, reaction etc.) to a node, carte
authentication is not enough, because the content needs its own signature.
To provide better user experience, the client may use carte to post a temporary
content without a signature and then ask the home node to post its signed version.
If during a short period of time the signed content do not arrive, the node erases
the temporary version.

### Passing the token

The recommended way to pass the token with a request is to set `Authorization`
HTTP header with [Bearer](https://datatracker.ietf.org/doc/html/rfc6750)
authentication scheme. The token should be prefixed with its type. For example:

```
Authorization: bearer secret:<root secret>
Authorization: bearer <admin token>
Authorization: bearer token:<admin token>
Authorization: bearer carte:<carte>
```

In situations, when the client cannot change request headers, it can use `auth=`
parameter in the URL of the request to pass the token. This method is not
recommended, because request URLs usually appear in server and proxy logs.

For example:

```
https://mynode.org/moera/<request URL>?auth=secret:<root secret>
https://mynode.org/moera/<request URL>?auth=<admin token>
https://mynode.org/moera/<request URL>?auth=token:<admin token>
https://mynode.org/moera/<request URL>?auth=carte:<carte>
```

To authenticate [the event stream](events.html) the client should pass the token
in the `token:` header of `CONNECTED` STOMP frame. For example:

```
token:secret:<root secret>
token:<admin token>
token:token:<admin token>
token:carte:<carte>
```
