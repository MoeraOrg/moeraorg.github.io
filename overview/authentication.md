---
layout: overview
title: Authentication
body_class: body-green
next: naming
---

# Authentication

To add, edit or remove publications on your own node (we will call it
*home node* by analogy with homepage) you need to authenticate with any
mechanism of your choice - login and password is the simplest one.

But for other nodes such a simple mechanism does not fit. You cannot
sign up and enter you credentials on every node in the Internet. To
confirm our identity when accessing other nodes we will use digital 
signatures.

Every user must generate for himself a *signing key* - a secret
cryptographic key he will use to sign all his messages and requests. The
corresponding public key must be stored in a public database accessible
to any Moera node or client, so they will be able to verify the
signature.

Cryptographic key must be long and random. No user can remember it and
enter by hand. Therefore, we store it at the home node instead. Every
time we need to sign a message, we send it to the home node, the home
node signs it and sends to the recipient.

The whole process is as follows:

1. Alice starts the client.
2. Alice enters the URL of her home node, her login and password.
3. The client authenticates on the home node with login and password and
   gets the authentication token. This token is stored on the client
   side and used in all interactions with the home node.
4. Alice opens Bob's node with the client, writes a comment and clicks
   "Send".
5. The client sends the comment to Alice's home node.
6. The home node signs the comment with Alice's signing key and sends it
   to the Bob's node.
7. Bob's node gets Alice's public key from the public database and
   verifies her signature. Also it checks whether Alice has a permission
   to leave comments under Bob's posts.
8. Bob's node publishes the comment together with Alice's signature.
9. Carol opens Bob's node with her client and reads Alice's comment.
10. Carol's client gets Alice's public key from the public database and
    verifies her signature.
11. Carol's client notifies Carol that the comment was indeed written by
    Alice.

(steps 2-3 may be skipped, if the client already has the authentication
token)

Note steps 10-11. In a decentralized network we do not trust Bob that he
doesn't write fake comments on Alice's behalf. The cryptographic
signature gives us proof instead of trust.

Also note that reading public content is possible without
authentication. There are no cookies that would be sent automatically on
every request. You may stay anonymous as long as you want. You can even
use Tor to hide you IP.

Anonymous postings are also allowed, if the node decides to accept them.
Or the node may receive a signed posting, check author's permissions and
strip the name and the signature before publishing. This may be
necessary if disclosure of the author's identity may hurt him. Privacy
is important.
