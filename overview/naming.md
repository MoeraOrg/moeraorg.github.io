---
layout: overview
title: Naming
body_class: body-green
---

# Naming

The *naming database* - the public database that keeps the names of the
users and the corresponding public keys is a single point of failure in
this scheme. Making this database fault-tolerant, tamper-resistant and
censorship-resistant is critically important for the security of the
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
key to the user in a human-readable form (as a sequence of 24 English
words) and encourage to write it down on a piece of paper and keep the
paper somewhere in a secure place.

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
with the signatures. If the name <tt>superman</tt> was used by Bob and
then taken by Dave, it is not possible to distinguish between the old
Bob's comment and the new Dave's comment - they both are signed with the
same name and both signatures are valid. (It would be incorrect to
consider Bob's signature invalid after transferring the name to Dave,
because Bob really wrote these old comments.)

To solve this problem we introduce a concept of *generation* of the
name. Bob owned the zeroth generation of the name,
<tt>superman<sub>0</sub></tt> and Dave owned the first generation of it,
<tt>superman<sub>1</sub></tt>. When we write the name without noting the
generation (<tt>superman</tt>), we always have in mind the latest
generation of it.

The generation number is increased in one of two cases:

1. When the name was released and registered again without signing the
   transaction by the old updating key. Note that the generation number
   is not increased, if the transaction was signed with the old updating
   key, even if 1 year has been passed and the name has been released.
   This may happen if the old owner forgot to prolong the name in time,
   but the name wasn't taken over by anybody else and the old owner
   prolonged it afterwards. In this case the generation is still the
   same.

2. When the owner voluntarily transfers the name to somebody else before
   1 year have been passed. In this case the owner still have to sign
   the transaction with his updating key, but marks the transaction as
   "transfer of ownership".

## Signing key invalidation

## Recap of the consensus rules

## Naming servers 

[1]: https://www.coindesk.com/information/what-is-blockchain-technology
[2]: /assets/images/Updating-Key-Words.png
