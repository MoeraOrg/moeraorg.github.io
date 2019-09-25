---
layout: overview
title: Cheaper Names
body_class: body-green
next: notifications
---

# Cheaper Names

Blockchain storage is expensive. Since blockchain nodes must have
incentive to participate, every transaction in the blockchain includes a
fee. Like in the familiar DNS name registration system, every name
registration/renewal costs money.

Another problem is the blockchain size and network traffic. If too much
information is stored in the blockchain, maintenance of a blockchain
node becomes a complex task. It affects decentralization, because only a
few big companies may afford maintaining a node. We need to keep the
blockchain size small to allow everyone to run a node.

(That's why it is impractical to store everything - posts, comments,
etc. - in the blockchain, the approach taken by some decentralized
social networks.)

There are many cheaper alternatives to the blockchain. They don't have
all positive qualities of the blockchain, but may be useful in many
cases.

## Hierarchical names

Since naming servers are independent from the underlying storage, it is
possible to use different storage types for different naming servers.
The names may have prefix designating the storage. For example,
`b.bettan` designates the name `bettan` registered in the blockchain,
and `m.bosse` is a cheaper name stored in a centralized database. A node
may ask different naming servers to resolve different types of names.

Another approach is to organize naming servers into a hierarchy similar
to DNS hierarchy. That is, `test.moera.org` domain is resolved by
requesting one of root nameservers for the list of nameservers for `org`
domain, then asking one of them for the address of the nameserver for
`moera` subdomain and asking one of them for the address of `moera`
host.
 
Similarly in Moera we may have top-level names registered in the
blockchain and allow them to point to the second-level naming servers
for resolving second-level names. For example, to resolve
`klaus.uacademy` name we get the URL of the naming server for `uacademy`
and ask it for the information about `klaus` name.

Hierarchical names need more requests to resolve, but they are cheaper
and allow to extend the namespace without limits. However, the
lower-level names lack decentralization advantages. If you registered
the name `steve.avengers`, you are dependent on the central naming
server for `avengers` domain. If you are not happy with it, you may
register another name in `hydra` domain, but you cannot move your
previous name to the new naming server. That means you loose all
friendship relations you had for the previous name, all access rights,
your comments are not yours anymore and so on. Thus, if you need true
decentralization, register you name in the blockchain.

(Theoretically it would be possible to move a low-level name to the
blockchain, because the blockchain is always checked first and
information in it has a priority. But in practice, allowing that will
open possibility of hijacking the name by registering it in the
blockchain instead of the true owner. That's because the blockchain
cannot use external sources of information (like other naming servers)
to prove ownership. To solve this problem we may allow to register such
names only when the transaction is signed by the owner of the top-level
name. But this way the full power will be again in the hands of the
top-level name owner.)

## Subordinate names

If you create a local group for your friends or a small event like an
Independence day barbecue, it has no sense to install a separate node
for it and register a name in the blockchain. You may use the same node
and a subordinate name instead.

For example, a node `https://omer.levi.family/` has a registered name
`omer-levi`. Then, the owner wants to organize a Passover event. He
assigns a subordinate name `passover-5779` to it. The full name for the
event will be `omer-levi/passover-5779` and the corresponding node URL
will be `https://omer.levi.family/~passover-5779/`. The name
`omer-levi/passover-5779` is not registered anywhere. To resolve it you
need to resolve `omer-levi` first, get the corresponding node URL and
construct the URL of the subordinate node using the well-known rules.

Note that the subordinate name does not have a separate signing key (its
signing key is the same as the signing key of the senior name), so this
mechanism cannot be used to create user accounts. But it is useful for
groups, events etc. where each member writes under his own name and
nobody writes under the name of the group.

## Surrogate names

If you don't need a human-readable name, you can use random sequences of
letters and digits instead of names. If they are long and truly random,
you will have an infinite namespace and every name will be unique. It
simplifies the naming system a lot.

Every user has a public signing key, which is long and nearly random.
Hash of this key in an encoded form (for example, [bech32][1]-encoded)
may be used as a *surrogate name* (looks like `0c5xw7kv`). In practice,
it will be enough to display first 8 characters of the encoded key to
the user - it will give about 1 trillion variants and probability of
collision will be low enough. Internally though the whole hash should be
used.

We don't need to keep a central storage for surrogate names. The
algoritm of publishing and usage of such names is as follows:

1. The node is installed and generates a signing key, private and
   public.
2. The node sends its URL and the public key to a naming server. The
   message is signed with the private key to prove ownership.
3. The naming server verifies the signature, generates the surrogate
   name and stores it in the internal database together with the node
   URL and the public key.
4. The naming server forwards the surrogate name and the related
   information to other naming servers via the peer-to-peer network of
   naming servers.
5. Each naming server that receives the information asks the node to
   prove the ownership of the key. If the proof is received, the naming
   server repeats the steps 3-4.
6. The node must refresh the surrogate name periodically. If not
   refreshed for more than 1 day, the record is deleted. This prevents
   unused names to point to URLs where the node was located in the past,
   but now there is a some unrelated site located. When the surrogate
   name is refreshed, the node URL may be changed.
7. When the surrogate name is used, nodes and clients query any naming
   server for the information related to it, as they usually do with any
   name. The search by the shortened form of a surrogate name should
   also work.
8. When the owner writes a post or comment using his surrogate name, he
   must include the full public key into it. This will allow to verify
   the signature even after the name is deleted from naming servers.
9. When a new naming server is installed, it must query from other
   naming servers all the data about registered surrogate names.

The surrogate names are coupled with the corresponding signing key. If
the signing key is compromised, there is no ability to invalidate the
key and to generate a new key preserving the name.

But, on the other hand, the surrogate names are much cheaper and more
private than other types of names.

[1]: https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki
