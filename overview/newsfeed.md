---
layout: overview
title: Newsfeed
body_class: body-green
---

# Newsfeed

The user's newsfeed is built by his home node in the background. The
user instructs the home node to subscribe to the nodes he wants to read.
The home node in the background fetches the content from these nodes,
receives notifications about updates and other information it needs and
builds the newsfeed. The user may read it at any moment using a Moera
client.

There are many possible algorithms of building the newsfeed. From the
simplest - all posts in the reverse chronological order - to very
complex, with grouping, filtering, statistical analysis and AI. The
newsfeed content is not limited to posts - any other news, events,
important pieces of informations may be added to the feed. The newsfeed
builder may be integrated into the node software, or node owner may
decide to use some third-party service (paying by his privacy). The
choice is in the user's hands.

It is recommended not to change the newsfeed after it was read. The new
posts should be added to the end (or the beginning) of the feed and this
"active part" of the feed may change in the process of building. But
after it was seen by the user, it is recommended to lock it, so the user
may be able to find the posts he just have seen. It also simplifies the
client and makes caching possible.

In particular, this means that the posts appear in the newsfeed not in
the order of publication, but in the order they have been received by
the newsfeed builder. Some posts may appear in the feed several times -
for example, if the algorithm is instructed to pop up the most popular
posts. Unsubscribing means you will not receive new posts from this
source anymore, but the posts you received earlier do not disappear
(while it is possible to remove them explicitly).

Since the posts may be edited or removed by the author, the
notifications the subscriber receives include not only the posts, but
also editing and removal events (and maybe even more - like change in
the number of reactions or comments). Note that the subscriber may
decide not to include these changes into his copy of the post, to keep
all revisions of it or to preserve the post that the author wants to be
deleted. There is no way to avoid this - even in centralized systems
anybody can copy-paste a post or make a screenshot.

(A node may add a delay between receiving a post from the node owner and
publishing it and sending notifications. This may give a chance to the
author to think again and make changes not visible to others.)

A node may decide to send notifications about old posts that changed
their visibility from private to public and now available to be read by
subscribers.

Simplified nodes may not support notifications. In this case subscribers
need to poll such nodes periodically to get the updates. But polling may
also be used intentionally - to preserve privacy. As we already said,
public posts may be read without authentication, so the fact you're
subscriber will not be disclosed.

## Notifications box

*Notifications box* is a button, usually in the top-right corner of the
screen, where you see quick notifications about the most important
events - reactions to your posts, replies to your comments or anything
else you want to see and respond quickly.

In Moera the content of the notification box is built as one more
newsfeed, but for different set of events.

Worth noting that you may have any number of different newsfeeds for
different purposes and they may be shown on separate pages, in sidebars,
dropdown menus - how the client wants to present them. Read whatever you
want using an interface of your choice - that's the power of Moera.
