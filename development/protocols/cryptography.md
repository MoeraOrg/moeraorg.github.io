---
layout: development
title: Protocols
up: protocols
subtitle: Cryptography
body_class: body-pink
---

# Cryptography

**ECDSA** with **secp256k1** curve is used everywhere in Moera for
public key cryptography.

Private key is encoded as fixed-length 32-byte big-endian value.

Public key is encoded as two concatenated fixed-length 32-byte
big-endian values — x and y respectively.

**SHA3-256 with ECDSA** is used for digital signatures. The signature is
up to 72 bytes in length.

**SHA3-256** is used in every place where cryptographic hash is needed.
