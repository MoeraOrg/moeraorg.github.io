---
layout: overview
title: Supervision
next: other
next_title: Other Features
---

# Supervision

## App store rules

Google Play and other similar app stores have rules for apps that display users'
content:

1. The app must publish rules for users' content that comply with Google Play's
own rules. This means that they must prohibit spam, violations of the law,
threats, etc. When registering, the user must agree to these rules.
2. The user must be able to block content they do not want to see.
3. The user must be able to report content that violates the rules, and the report
must be reviewed and, if the rules are indeed violated, the content must stop
being displayed.

In the case of Moera, point 3 had to be thought about for an obvious reason: the
network is decentralized, there is no supervisor over it, and there is not even
a physical possibility to delete content from it.

Therefore, the following solution was proposed, which seems quite reasonable,
preserves decentralization and freedom in the network, and is quite universal.

1. For each app in the network, a special user will appear, called the "app
sheriff". Such sheriffs can also be created for other purposes, but for now let's
focus on Google Play. An app installed not through Google Play will be free of
restrictions.
2. A user who wants their blog to be visible through the app must approve the
supervision of their blog by the sheriff. This means that the sheriff has extended
access to all content, except private ("Only me") content, and the node must obey
the sheriff's orders. Blogs that have not approved the supervision will not be
visible through the app.
3. At the moment, there is only one type of order: to place a sheriff's mark on
the specified post or comment. This mark is saved and returned to the client upon
request. The app, seeing this mark, hides the corresponding post or comment. At
the same time, in other apps, on other platforms, these posts and comments will
remain visible.
4. In the menu of posts and comments, when viewed through the app, there is an
item "Report...". With it, one can send a sheriff a report of a violation of the
rules, indicating the type of violation and an additional comment.
5. All complaints are public by default. The user can ask that their
complaint not be shown to everyone; in that case, the complaint will be hidden until the
sheriff makes a decision. Further hiding of the complaint is at the discretion of
the sheriff, but, as a rule, the sheriff will hide the complaint only in
exceptional cases.
6. Naturally, the review of the complaint and the sheriff's order are accompanied
by sending notifications to everyone involved.
7. The sheriff's node also stores a list of users whose comments the sheriff has
banned from showing everywhere, without making a decision on each individual
comment. Nodes that have approved the supervision check this list and place a
sheriff's mark on the comments of all users included in the list.

Thus, the requirements of Google Play will be met, but to the minimum necessary
extent and at the discretion of the network participants. And there will always
be alternatives: access through a browser, installation from an APK or from other
stores where these restrictions will not exist.

And, of course, if desired, any group of users can come together, elect a sheriff
and give him the right to supervise their content. Moera does not restrict users
in their right to self-moderation or the voluntary choice of an external moderator.

## Malware detection

Now that posts and comments may have arbitrary files attached to them, not only
pictures, malicious files may be attached as well. This problem is real, and it
should be solved in a Moera way, without concentrating too much power in one
place.

It is impossible to detect every malicious file at the moment of upload. But it
is possible to maintain databases of known malware and block such files from
being downloaded. For this purpose, a special account called the "Security
Guard" may store such a database in the form of file hashes, and others may
check files against it. There may be many such databases, and every user may
decide which of them to trust, whether to connect to one of them, to several of
them, or to none at all.

Who should perform the check, and when? It is hard to organize this on the
client device. The node where the file is stored cannot be trusted either,
because it may distribute malicious files intentionally. So the most reasonable
place to perform the check is the home node.

Every attached file that you are going to download is first passed through your
home node. There it is checked against the databases you have chosen. If the
check is successful, the file becomes available for downloading. This may take
some time, but it is the price of safety.

In the future, more advanced protection systems may be installed on the home
node. The Security Guard may also proactively search the network for files and
check them. Many approaches are possible.

## Spam

If you allow anybody to comment, some heuristics can help you to avoid
spam comments: for example, you may not allow users without registered
names or with names registered not so long ago to comment or to put
links in comments. Or you can use spam lists.

A spam list is a service located on a separate host. It works as
follows:

1. You connect your home node to the service.
2. When you see somebody posting spam, you press a "Spam" button.
3. The name of the user and his signed comment are sent to the service.
4. If several people complain about the same user, he is added to the
   spam list. He is sent a notification about this.
5. Your node subscribes to the spam list updates and blocks all users in
   the list from posting anything on your node.
6. The user may appeal to the service to be excluded from the list. The
   signed copies of his comments are used as a proof.
7. The nodes that sent false spam complaints too many times may be banned
   from using the service.

There may be many different services that use various definitions of
"unwanted behavior." You may choose which of them to trust.
