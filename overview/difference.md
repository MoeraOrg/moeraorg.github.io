---
layout: overview
title: Difference
body_class: body-green
next: moera
---

# What's a difference?

The question asked very often: What's a difference between Moera and other
decentralized social networks that already exist? Why it was needed to create
another one?

There is no much sense to make comparison to every social network one-by-one. So
let's highlight the strongest points that give Moera advantage over the popular
solutions that exist in decentralized world.

### Personal node

A popular approach for decentralization is to build the network as a federation of
small communities - _pods_ that have their own rules. A new user should first find
a pod that accepts new members and register a new account at it. From now and then
the user's network name will be bound to the pod, his social connections will be
limited by connections of the pod itself and most of the social life will happen
inside the pod. And since the pod keeps the account and responsible to
authentication, migration from the pod means losing the name, social connections
and probably all the data.

As a contrast, Moera has a registration process independent of the server, where
the user stores his data. These servers are not communities, but just _providers_,
their job is to provide software and storage to the user for profit. Providers do
not impose any rules of their own and user is free to migrate from one provider to
another while keeping his name, social connections and data. Moera treats every
user as an individual, not as a part of some community. Moera _node_ is a personal
space in the cloud that has no ties to other nodes on the same server.

And if a user prefers to use his personal server as a node, Moera software makes
the installation process as easy as possible.

### Standardized API

Moera server software does not provide a web interface of its own. Users access
Moera with a client software that may be a web application, a mobile app or any
other tool or script that may be written. All clients use the same well-documented
standard Moera API.

It is not mandatory to use Moera software to become part of the network. Any
existing website may implement Moera API and become accessible by all Moera
clients without making any changes in its internals. Integration of popular
publishing platforms, like WordPress, into Moera should be as easy as installing
a plugin.

Obviously, the standard API makes easy to create a gateway between Moera and any
other social network, centralized or decentralized.

### Simple technologies

Moera API is a thin layer over the standard HTTP protocol. Moera did not create
any special low-level protocol for decentralized storage, mesh networks or message
brokers. This makes it easy to implement the API, integrate into existing systems
and host at any server. And makes client software simple as well.

Blockchain is a great tool for decentralization. But storing all data in
a blockchain is costly, so not really achievable without compromising
decentralization. That's why Moera uses blockchain for storing user accounts only.
Since migration of data between providers is easy, market forces and free
competition will work to protect the user's content.

### User-friendly

Moera software seeks to be as user-friendly as possible. Easy sign up from
a single place, creating a node by a click, simplifying complex things to make
user experience even better than in the best centralized social networks.

Many existing decentralized social networks provide no more than a Twitter-like
interface. Moera makes a goal to provide all advanced social features - access
rights, friendships, groups, discussions, recommendations etc. For most users
decentralization is not enough to choose to migrate to a new social network.
That's why user experience and unique features is a key factor to success.  

### Fighting malicious actors

Many decentralized social networks suffer from malicious actors, like spammers.
Moera from very beginning is built to prevent fraud and attacks. It uses
cryptography to verify ownership of posts and comments. It limits rate of
requests and allows to block clients to prevent DoS attacks. It uses spam lists
to fight spam. It provides a decentralized approach to detect unlawful activity
and fraud, while maintaining freedom of choice and freedom of speech.

### Universal

Moera API is made to be universal. It allows the client to present the user's
data in any form, making possible to create different social networks with
different interfaces and social mechanics. If some social network becomes outdated
and boring, the user may switch to another one by simply installing a different
client. All data on server's side will be left untouched.

And social networks is not the only usage of the Moera node, it is just one of
an infinite number of applications. The node may become a file or document
storage, a photo galley, a notebook, a password manager and so on. And if you
have a smart device, it would be much more secure to connect it to your Moera
node and store your personal data on it, instead of somewhere in the device
manufacture's private cloud.