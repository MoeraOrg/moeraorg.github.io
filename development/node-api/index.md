---
layout: development
title: Node API
---

# Node API

Moera Node API is a JSON-based REST API. See [introduction][1] to Node REST API in
the Architecture Overview section. Until the API is stabilized, it may be changed in
various ways and backward compatibility is not guaranteed.

`timestamp` below is the number of seconds that passed since 01-01-1970 00:00:00 in
UTC timezone.

## Table of Contents

1. [Requests](requests.html)
2. [Events](events.html)
3. [Notifications](notifications.html)
4. [Virtual Pages](virtual-pages.html)
5. [Headers](headers.html)
6. [Node Name](node-name.html)
7. [Moment](moment.html)
8. [Authentication](authentication.html)
9. [Access Controls](access-controls.html)
10. [Fingerprints](fingerprints.html)
10. [OAuth2](oauth2.html)

## General errors

If an error occurs when processing an API request,
<code><a href="requests.html#Result">Result</a></code> structure
is returned instead of the regular response. The structure contains the error code
and message, and also the [HTTP status code][2] is set accordingly. All error codes
are case-insensitive.

An error may occur on different stages of request processing.

* If the request URL is unknown, `not-found` error is returned.
* If the request Content-Type is unknown, `invalid-content-type` error is returned.
* If there were too many requests done in a short period of time, `too-many-requests`
  error is returned. In addition, [`Retry-After`][6] and [`RateLimit-Policy`][7]
  headers are set.
* If incorrect JSON is provided, `invalid-syntax` error is returned.
* If the request is correct, but the operation is not supported by the node,
  `not-supported` error is returned.
* If value of one of the arguments does not correspond its type,
  `invalid-argument-value` error is returned.
* If authentication is required, but not provided, `authentication.required` error
  is returned.
* If an invalid authentication token or root secret is provided,
  `authentication.invalid` error is returned.
* If the provided signature is incorrect, `authentication.incorrect-signature` error
  is returned.
* If the provided [carte][3] is incorrect, one of the following error codes is
  returned:
  * `carte.client-address-unknown` &ndash; cannot determine client IP address;
  * `carte.unknown-fingerprint` &ndash; unknown fingerprint version encoded in the carte;
  * `carte.invalid` &ndash; the carte format is invalid;
  * `carte.not-begun` &ndash; the timespan of the carte has not begun yet;
  * `carte.expired` &ndash; the carte is expired;
  * `carte.unknown-signing-key` &ndash; cannot find public key for the carte owner;
  * `carte.invalid-signature` &ndash; carte signature is invalid.
* If the node is blocked from performing the operation, `authentication.blocked`
  error is returned.
* If the request needs a node name, but it is not defined, `node-name-not-set` error
  is returned.
* If the request needs a signing key, but it is not defined, `signing-key-not-set`
  error is returned.
* If request body does not pass validation, a validation error is returned. Look 
  into the chapter on the particular structure for the list of validation errors
  that correspond to the structure.
* If an error occurs while executing the operation, one of the errors listed in
  the corresponding operation's chapter is returned.
* If a configuration error or a software bug occurs, `server.misconfiguration` error
  is returned.
* If request processing involves a naming server, but it is not available,
  `naming.not-available` error is returned.

## Authentication requirements

[Authentication][4] requirements, if specified in the request description, may be one
of the following:
* _none_ or not present &ndash; authentication is not needed, it does not affect
  the request;
* _optional_ &ndash; authentication is not mandatory, but it does affect the request;
* _required_ &ndash; authentication is required to perform the request;
* _signature_ &ndash; signature should be included in the request body;
* _root admin_ &ndash; the client should authenticate as server administrator
  to perform the request;
* _admin_ &ndash; the client should authenticate as node administrator to perform
  the request.

## CID

`cid` parameter may be passed with any request. See [Events][5] page for
the description of its purpose.

[1]: /overview/node.html
[2]: requests.html#http-status-codes
[3]: authentication.html#carte
[4]: authentication.html
[5]: events.html
[6]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After
[7]: https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/
