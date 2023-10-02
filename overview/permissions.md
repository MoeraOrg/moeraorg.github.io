---
layout: overview
title: Permissions
next: supervision
next_title: Supervision
---

# Permissions

The node decides by itself whether to permit a particular user to view,
edit, delete, comment etc. the content that is posted on the node. That
includes the comments — if you commented a post on someone's node, the
owner of the node decides from that moment whether to allow you or
somebody else to edit or delete it. But your signature cannot be forged,
so if somebody edited your comment, the fact of the editing will be
visible to everyone.

## Access hints

Access controls may be implemented in many ways, but all these internal
implementation details are not visible to the client (except the owner).
Node simply does not return the content that the user is not allowed to
view or returns error in the answer to the editing request if the user
is not allowed to edit — without any explanation. However, the node may
return hints that help user to know in advance what operations he may be
allowed to perform. But they do not guarantee that the operation will be
allowed, they are just hints. They may be used to hide or gray out some
buttons or menu items.

For each post, comment etc. the node returns a list of operations that
may be performed on it, and for each operation - a list of groups of
users that are allowed to perform the operation. There are only names of
the groups, without any details. Some names are standard — "admin",
"owner", "moderator". Other are meaningless strings or numbers — this is
recommended for privacy, to keep the real purpose of the groups in
secret.

Every user may ask the node about himself (and only himself) — what
groups he is included in. With this information, he can predict what
operations he may be allowed to perform.

Public operations (like viewing public posts) are allowed to any user
without authentication. There is no way to deny a public operation for
anybody.

## Signed requests

If you want to perform an operation that is allowed only for a limited
group of users, you need to authenticate. The authentication mechanism
is explained [in a separate chapter][1]. Note that signing is needed not
only for posting something. Getting information may also require
signature if some posts are hidden from the public. The information
about your own permissions (see above) is also accessible only by signed
request.

To protect against [replay attacks][2], the request data that is signed
must include the name of the target node, the subject, the current
timestamp and a sequential number. The signature is valid only for a
short period of time, and sequential numbers must increase with every
request.

We prefer to use signatures everywhere, not tokens, because they are
bound to the request. Leaked signature is useless for the attacker. But
for interactions with the home node, we have no alternative to tokens.
(Of course, we protect all communications with SSL.) There may be
restricted tokens that allow read-only access or only access to certain
information — they are useful for backup scripts, auto-responders, etc.

## Friends

We call *friends* the users that have some permissions on your node that
the public do not have. Friends are not subscribers. Subscribers follow your
publications, but if they are not friends, they do not see "friends
only" publications and may be restricted in other ways. And vice versa,
not all friends are subscribers.

The above means that the "friendship" is not mutual. When somebody
subscribes to you or gives you some permissions, you are not required to
do the same. But she may send you a request asking to give her extended
access. Since she usually does not know what group of users you have, the
request has a generic form (maybe, with some personal message). It
appears in your [notification box][3], and you can accept, decline or
dismiss it (decline without informing the requester).

## Ban

*Ban* means placing a user into a list of particularly restricted users.
Ban means different things in different social networks. There are some
of them:

* Deny access to your public posts and comments — not possible in Moera.
* Deny access to your non-public content — remove him from all groups
  granting special access rights.
* Deny from commenting — if you, for example, allow comments from any
  authenticated user, you still can reject comments from some of them,
  without any explanation.
* Deny from commenting under your posts in groups — if the group node
  agrees (see below).
* Delete all comments — you can do this at any moment.
* Hide in any discussion - your client gets the list of banned users
  from your node and hides their comments from you. The newsfeed builder
  can do the same.
* Hide from [search][4] and [recommendations][4] - your client can
  filter the search results and recommendations before showing them to
  you.

Besides of bans, nobody can stop you from implementing any system of
warnings, temporary bans, karma — anything you've seen on forums, in
FIDO or invented by yourself.

## Publications on other nodes

As we already said, if you wrote a post in a group or commented under
somebody's post, you do not control your publication. The node where
the publication is located controls everything — who can view it, edit
or delete. But you can ask the node to obey some of your personal
restrictions (for example, to stop somebody from commenting under your
post), and the node can make you a favor. Specifically, the node may do a
request to your home node to check whether, for example, you allow the
given user to comment under your post. 

[1]: /overview/authentication.html
[2]: https://en.wikipedia.org/wiki/Replay_attack
[3]: /overview/newsfeed.html
[4]: /overview/other.html
