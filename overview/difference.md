---
layout: overview
title: What's the Difference?
next: moera
next_title: Why Is It Called Moera?
---

# What's the Difference?

A question that is asked very often is: What's the difference between Moera and other
decentralized social networks that already exist? Why was it needed to create
another one?

There is not much sense in comparing Moera to every social network one by one. So
let's highlight the strongest points that give Moera an advantage over the popular
solutions that exist in the decentralized world.

### Personal node

A popular approach for decentralization is to build the network as a federation of
small communities — _pods_ that have their own rules. A new user should first find
a pod that accepts new members and register a new account there. From then on,
the user's network name will be bound to the pod, their social connections will be
limited by the pod's own connections, and most of their social life will happen
inside the pod. And since the pod keeps the account and is responsible for
authentication, migration from the pod means losing the name, social connections
and probably all the data.

By contrast, Moera has a registration process independent of the server, where
the user stores his data. These servers are not communities, but just _providers_,
their job is to provide software and storage to the user for profit. Providers do
not impose any rules of their own, and the user is free to migrate from one provider to
another while keeping his name, social connections and data. Moera treats every
user as an individual, not as a part of some community. Moera _node_ is a personal
space in the cloud that has no ties to other nodes on the same server.

And if a user prefers to use their personal server as a node, Moera software makes
the installation process as easy as possible.

### Standardized API

Moera server software does not provide a web interface of its own. Users access
Moera with client software that may be a web application, a mobile app or any
other tool or script that may be written. All clients use the same well-documented
standard Moera API.

It is not necessary to use Moera software to become part of the network. Any
existing website may implement Moera API and become accessible by all Moera
clients without making any changes in its internals. Integration of popular
publishing platforms, like WordPress, into Moera should be as easy as installing
a plugin.

Obviously, the standard API makes it easy to create a gateway between Moera and
any other social network, centralized or decentralized.

### Simple technologies

Moera API is a thin layer over the standard HTTP protocol. Moera did not create
any special low-level protocol for decentralized storage, mesh networks or message
brokers. This makes it easy to implement the API, integrate it into existing systems,
host it on any server, and make client software simpler as well.

Blockchain is a great tool for decentralization. But storing all data in
a blockchain is costly, so not really achievable without compromising
decentralization. That's why Moera uses blockchain for storing user accounts only.
Since migration of data between providers is easy, market forces and free
competition will work to protect the user's content.

### User-friendly

Moera software seeks to be as user-friendly as possible: easy sign-up from
a single place, creating a node with a click, and simplifying complex things to make
the user experience even better than in the best centralized social networks.

Many existing decentralized social networks provide no more than a Twitter-like
interface. Moera has a goal to provide all advanced social features — access
rights, friendship, groups, discussions, recommendations, etc. For most users,
decentralization is not enough to choose to migrate to a new social network.
That's why user experience and unique features are key factors for success.

### Fighting malicious actors

Many decentralized social networks suffer from malicious actors, like spammers.
Moera, from the very beginning, is built to prevent scams and attacks. It uses
cryptography to verify ownership of posts and comments. It limits the rate of
requests and allows it to block clients to prevent DoS attacks. It uses spam lists
to fight spam. It provides a decentralized approach to detecting unlawful activity
and scams while maintaining freedom of choice and freedom of speech.

### Universal

Moera API is made to be universal. It allows the client to present the user's
data in any form, making it possible to create different social networks with
different interfaces and social mechanics. If some social network becomes outdated
and boring, the user may switch to another one by simply installing a different
client. All data on the server's side will be left untouched.

And social networks are not the only use of the Moera node; this is just one of
an infinite number of applications. The node may become a file or document
storage, a photo gallery, a notebook, a password manager, and so on. And if you
have a smart device, it would be much more secure to connect it to your Moera
node and store your personal data on it, instead of somewhere in the device
manufacturer's private cloud.
