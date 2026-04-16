---
layout: overview
title: Authentication
next: naming
next_title: Naming
---

# Authentication

To add, edit or remove publications on your own node (we will call it *home node*
by analogy with a homepage), you need to authenticate with any mechanism of your
choice — a login and password are the simplest option.

But for other nodes, such a simple mechanism does not fit. You cannot sign up and
enter your credentials on every node on the Internet. To confirm your identity when
accessing other nodes, we will use digital signatures.

Every user must generate a *signing key* — a secret cryptographic key used to sign
all their messages and requests. The corresponding public key must be stored in a
public database accessible to any Moera node or client, so they can verify the
signature.

The cryptographic key must be long and random. No user can remember it and enter it
by hand. Therefore, we store it at the home node instead. Every time Alice needs
to sign a message, she sends it to her home node; the home node signs it and sends
it to Bob.

Note that in the decentralized network, we do not trust Bob not to write
fake comments on Alice's behalf. Carol, reading Alice's comment, may validate
Alice's signature at any moment. Cryptography gives us proof instead of trust.

Also note that reading public content is possible without authentication.
You may stay anonymous as long as you want. You can even use Tor to hide your IP.

Anonymous postings are also allowed if the node decides to accept them.
Alternatively, the node may receive a signed posting, check the author's
permissions, and strip the name and the signature before publishing. This may be
necessary if disclosure of the author's identity may harm them. Privacy
is important.
