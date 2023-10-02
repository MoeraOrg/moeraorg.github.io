---
layout: overview
title: Naming
next: cheaper-names
next_title: Cheaper Names
---

# Naming

The *naming database* - the public database that keeps the names of the
users, and the corresponding public keys - is a single point of failure
in this scheme. Making this database fault-tolerant, tamper-resistant
and censorship-resistant is critically important for the security of the
decentralized network. Blockchain is a natural choice for this task.

## Blockchain

[Blockchain][1] is a public database that is kept simultaneously on any
number of independent nodes that do not trust one another. No permission
is needed to become a node.
 
Only one state of the blockchain can be considered valid at any moment.
Old records in the blockchain cannot be modified or removed, only new
records can be added to the end of the blockchain in a strong
chronological order. Only those records can be added that conform to the
well-known *consensus rules*. The consensus rules cannot be changed
without the consent of a majority of the nodes.

Records in a blockchain are called *transactions*.

## Updating key

Transactions in the Moera blockchain operate on names. After some user
takes ownership of a name, further operations on this name are not
possible without knowledge of a key. This key we call *updating key*.

The private updating key is used very rarely — only when it is needed to
make changes in the naming database. Keeping it on a computer is
unnecessary and poses a security risk. Instead of this, we display the
key to the user in a human-readable form ([as a sequence of 24 English
words][4]) and encourage to write it down on a piece of paper and keep
the paper somewhere in a secure place.

![Updating key in a human-readable form][2]

## Signing key invalidation

The private signing key must always be present on the home node to be
able to sign messages. What to do if due to some security breach it is
stolen?

If the updating key is not stored in the computer, it will be safe. The
owner can use it to change the signing key in the blockchain. From that
moment the old signing key will be invalid, messages signed with it will
no longer be accepted (but for older messages the signature will still
be considered correct).

More than that, the owner may set the date of the key invalidation *in
the past*. In this case, even if the intruder had a chance to perform
some operations (post messages, delete them etc.) before the hack was
revealed, these operations may be undone.

Nodes should be aware of this possibility. For every name they deal with
\- to validate signature, give access or collect information — they
should subscribe to [notifications][3] to know if the corresponding key
has been changed. They should store enough information to undo the
operations that can be undone — content of deleted messages, previous
versions of the edited ones, and so on. We limit the undo feature to up
to 1 week in the past. It will be enough for most cases and will not
require nodes to store too much of extra data or to follow too many
names.

## Recap of the consensus rules

(We are skipping all details related to empty values, data format,
maximal length, etc.)

A transaction is considered invalid if and only if at least one of these
conditions is true:

* There were no transactions with *name*, and:
  1. Signing key *activation date* is in the past.
* There were transactions with *name*, and:
  1. *Signature* is invalid.
  2. Signing key *activation date* is more than 1 week in the past.
  3. Signing key *activation date* is before *activation date* of the
     first signing key of the *name*.

Note that inclusion of the transaction into the blockchain takes time.
If *activation date* is set to the current time, it may be in the past
at the moment when the transaction is being included in the
blockchain. To avoid the transaction invalidation for this reason, it is
recommended to set *activation date* in the future.

## Naming servers 

Integration with the blockchain requires installation of special
software and a lot of disk and CPU resources. It would be excessive to
require every node to interact with the blockchain directly.
Instead of that, only Moera *naming servers* will integrate with the
blockchain, and nodes will talk to them using a simple protocol.

Anybody can run a naming server, and a node may select from these
servers on the basis of latency, uptime, trust or any other
considerations. If you don't trust any naming server, you can always run
your own - that's why naming servers have almost no reason to provide
incorrect information to the nodes. Rare occasions of forgery will be
quickly revealed.

Moera clients may also use naming servers to get the information about
signing keys and to verify signatures on the client side.

## Node URL

For every registered name we also store in the blockchain the URL of the
node this name is assigned to. This information has many uses, for
example:

* If you know the registered name, you may enter it into a Moera client
  and go immediately to the desired node. No search is needed.
* If a node should be [notified][3] (for example, somebody replied to
  your comment somewhere), the notifier can easily get the node URL by
  the name.
* When a client connects to some node, the node reports its registered
  name to the client. The client may easily verify this information by
  comparing the node URL to the URL obtained from a naming server.

[1]: https://www.coindesk.com/information/what-is-blockchain-technology
[2]: /assets/images/Updating-Key-Words.png
[3]: /overview/notifications.html
[4]: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
