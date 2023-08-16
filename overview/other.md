---
layout: overview
title: Other Features
body_class: body-green
next: commercialization
---

# Other Features

Shortly about other popular features of social networks and how they may
be implemented in Moera.

## User search

Web search engines index all public data, including the public part of
user profiles. So it is possible to use Google, Bing, DuckDuckGo, etc.
to find a Moera user or a public post. But sometimes it is easier
to have a simple search that allows to quickly find a user by his name
right from the Moera client interface.

This search may be implemented as a separate service located on its own
host that subscribes to notifications from a naming server about any
nodes that appear and then fetches their profile data via REST API. It
may also subscribe to notifications from the nodes about changes in
their profiles.

The search engine provides a simple API that Moera clients can use. It
may provide a web UI as well.

## Local search

It is possible to integrate a small search engine into the node that
will index all the content, including private. The search results will
be accessible by the node's owner only.

## Activity log

Since the home node is used anyway for signing all posts and comments,
it is possible to keep a copy of them on the home node. This way you can
always find everything you have posted, even if it was deleted from the
node where you published it.

## Repost

You can repost somebody else's post in one of two ways: (a) post a link
to it; (b) copy it. If you make a copy, your home node subscribes to
notifications from the original node to know when the original post is
edited or deleted. The behavior is the same as for posts in your
[newsfeed][1]. And you are able to preserve your copy of the post even
if the original post was deleted.

It is not possible to prevent reposting of your non-public posts (you
cannot block copy-paste and screenshots). But the Moera client should
display a warning if somebody tries.

## Polls

You can publish a poll like any other post. You may allow anybody to
vote or require every voter to authenticate to be sure nobody has voted
several times. In this case, you will know who voted and how. That's your
decision whether to publish the detailed results.

Anonymous (but fair) voting is more complicated, because the voter must
be sure that the node owner doesn't know his identity. But there are
cryptographic algorithms that may be useful for this. For example,
[blind signatures][2].

## Recommendations

It is possible to create a service that will recommend you people that
may be your friends or posts that you may like. But to make it working,
you will need to compromise your privacy and allow this service to see
your list of friends and the list of posts you've liked. Do this at your
own risk.

## Verified users

How can you be sure that some Moera user is indeed the person they
pretend to be?

1. If a user wants their identity to be verified, they turn to an
   authoritative organization (or person).
2. The authoritative organization verifies that user's ID.
3. The authoritative organization signs the user's registered name and
   real name.
4. Your Moera client sees the signature, validates it and marks the user
   as verified.
   
You can choose which organizations or persons you trust to verify
the identity of others.

## Spam

If you allow anybody to comment, some heuristics can help you to avoid
spam comments: for example, you may not allow users without registered
names or with names registered not so long ago to comment or to put
links in comments. Or you can use spam lists.

Spam list is a service located on a separate host. It works as
following:

1. You connect your home node to the service.
2. When you see somebody posting a spam, you press a "Spam" button.
3. The name of the user and his signed comment are sent to the service.
4. If several people complain about the same user, he is added to the
   spam list. He is sent notification about this.
5. Your node subscribes to the spam list updates and blocks all users in
   the list from posting anything on your node.
6. The user may appeal to the service to be excluded from the list. The
   signed copies of his comments are used as a proof.
7. The nodes that sent false spam complaints too many times may be banned
   from using the service.

There may be many different services that use various definitions of
"unwanted behavior." You may choose which of them to trust.

[1]: /overview/newsfeed.html
[2]: https://en.m.wikipedia.org/wiki/Blind_signature
