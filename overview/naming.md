---
layout: overview
title: Naming
body_class: body-green
next: cheaper-names
---

# Naming

The *naming database* - the public database that keeps the names of the
users and the corresponding public keys - is a single point of failure
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

Records in the blockchain are called *transactions*. 

## Updating key

Transactions in the Moera blockchain operate on names. After some user
takes ownership of a name, further operations on this name are not
possible without knowledge of a key. This key we call *updating key*.

The private updating key is used very rarely - only when it is needed to
make changes in the naming database. Keeping it on a computer is
unnecessary and poses a security risk. Instead of this, we display the
key to the user in a human-readable form ([as a sequence of 24 English
words][4]) and encourage to write it down on a piece of paper and keep
the paper somewhere in a secure place.

![Updating key in a human-readable form][2]

## Forced release

After 1 year since the latest transaction with the name it is considered
free again and may be registered by anybody. It is done to prevent
exhaustion of the namespace. Unused names are forcibly released and made
available to those who need them. If the current owner wants to prolong
ownership, he must make a "dummy" transaction with the name (i.e.
transfer ownership to himself). Every transaction in the blockchain
requires payment, so it creates an incentive not to prolong
automatically the names that are not needed.

## Generation

Ability to transfer the name from one owner to another creates a problem
with the signatures. If the name <code>bond</code> was used by Bob and
then taken by Dave, it is not possible to distinguish between the old
Bob's comment and the new Dave's comment - they both are signed with the
same name and both signatures are valid. (It would be incorrect to
consider Bob's signature invalid after transferring the name to Dave,
because Bob really wrote these old comments.)

To solve this problem we introduce a concept of *generation* of the
name. Bob owned the zeroth generation of the name,
<code>bond<sub>0</sub></code> and Dave owned the first generation of it,
<code>bond<sub>1</sub></code>. When we write the name without mentioning
the generation (<code>bond</code>), we always have in mind the latest
generation of it.

The generation number is increased in one of two cases:

1. When the name was released and registered again without signing the
   transaction by the old updating key. Note that the generation number
   is not increased if the transaction was signed with the old updating
   key, even if 1 year has been passed and the name has been released.
   This may happen if the old owner forgot to prolong the name in time,
   but the name wasn't taken over by anybody else and the old owner
   prolonged it afterwards. In this case the generation is still the
   same.

2. When the owner voluntarily transfers the name to somebody else before
   1 year have been passed. In this case the owner still have to sign
   the transaction with his updating key, but marks the transaction as
   "transfer of ownership" by passing an increased generation number.

## Signing key invalidation

The private signing key must always be present on the home node to be
able to sign messages. What to do, if due to some security breach it is
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
\- to validate signature, give access or collect information - they
should subscribe to [notifications][3] to know if the corresponding key
have been changed. They should store enough information to undo the
operations that can be undone - content of deleted messages, previous
versions of the edited ones and so on. We limit the undo feature to up
to 1 week in the past. It will be enough for most cases and will not
require nodes to store too much of extra data or to follow too many
names.

## Recap of the consensus rules

(We are skipping all details related to empty values, data format,
maximal length etc.)

A transaction is considered invalid if and only if at least one of these
conditions is false:

* There were no transactions with *name*, and:
  1. *Generation* is not 0.
  2. Signing key *activation date* is in the past.
* The latest transaction with *name* is more than 1 year old, and:
  1. *Generation* does not equal to the previous generation plus 1.
  2. Signing key *activation date* is in the past.
* The latest transaction with *name* is less than 1 year old,
  *generation* equals to the previous generation plus 1, and:
  1. *Signature* is invalid.
  2. Signing key *activation date* is in the past.
* The latest transaction with *name* is less than 1 year old,
  *generation* equals to the previous generation, and:
  1. *Signature* is invalid.
  2. Signing key *activation date* is more than 1 week in the past.
  3. Signing key *activation date* is before *activation date* of the
     first signing key of this *generation* of *name*.

Note that inclusion of the transaction into the blockchain takes time.
If *activation date* is set to the current time, it may be in the past
at the moment when the transaction is being included into the
blockchain. To avoid the transaction invalidation for this reason, it is
recommended to set *activation date* in the future.

## Naming servers 

Integration with the blockchain requires installation of special
software and a lot of disk and CPU resources. It would be excessive to
require from every node to interact with the blockchain directly.
Instead of that, only Moera *naming servers* will integrate with
blockchain, and nodes will talk to them using a simple protocol.

Anybody can run a naming server, and a node may select from these
servers on the basis of latency, uptime, trust or any other
considerations. If you don't trust any naming server, you can always run
your own - that's why naming servers have almost no reason to provide
incorrect information to the nodes. The rare occasions of fraud will be
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
