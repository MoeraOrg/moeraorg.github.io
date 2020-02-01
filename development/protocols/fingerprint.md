---
layout: development
title: Protocols
up: protocols
subtitle: Fingerprint
body_class: body-pink
---

# Fingerprint

When a signature is required for an object, the designated fields of the
object are taken, encoded in the standard way (see below) and
concatenated together in the designated order. The resulting block of
data is called the *fingerprint* of the object. It is signed with the
private key of the respective user.

The encoding is designed in such a way so that any two different objects
produce different fingerprints. This prevents object malleability - to
make impossible to change the object while the signature remains valid.

The fingerprint is a structure consisting of fields in a fixed order.
Every field may be of one of primitive types, a structure, or an array
of any type. The encoding of the supported types is described below.

##### Null

Null value of any type is encoded as one-byte value `0xFF`.

##### Boolean

Boolean value is one byte: `0x00` for `False` and `0x01` for `True`.

##### Variable-sized integer

* `value < 0xFC`
  * value (one byte)
* `value <= 0xFFFF`
  * `0xFC` (one byte)
  * value (two bytes, little-endian)
* `value <= 0xFFFF FFFF`
  * `0xFD` (one byte)
  * value (four bytes, little-endian)
* `value > 0xFFFF FFFF`
  * `0xFE` (one byte)
  * value (eight bytes, little-endian)

##### String

* length of the string in UTF-8 encoding (variable-sized integer)
* the string in UTF-8 encoding

##### Array of bytes

* number of bytes (variable-sized integer)
* the bytes

##### Array of any other type

* total length of the encoded values in bytes (variable-sized integer)
* the values encoded according to their type

##### Structure

* structure version (variable-sized integer)
* the fields in a predefined order, encoded according to their type

##### Digest (cryptographic hash)

Encoded as array of bytes. The length of the array is present, as for
every other array of bytes, but will be the same for all hashes using
the same [algorithm][1].

##### InetAddress

IPv4 or IPv6 address, encoded as array of bytes in network order.

[1]: /development/protocols/cryptography.html
