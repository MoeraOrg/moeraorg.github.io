---
layout: overview
title: Supervision
next: other
next_title: Other Features
---

# Supervision

Google Play and other similar app stores have rules for apps that display users'
content:

1. The app must publish rules for users' content that comply with Google Play's
own rules. This means that they must prohibit spam, violations of the law,
threats, etc. When registering, the user must agree to these rules.
2. The user must be able to block content he does not want to see.
3. The user must be able to report content that violates the rules, the report
must be reviewed and, if the rules are indeed violated, the content must stop
being displayed.

In the case of Moera, point 3 had to be thought about for an obvious reason: the
network is decentralized, there is no supervisor over it, and there is no even
a physical possibility to delete content from it.

Therefore, the following solution was proposed, which seems quite reasonable,
preserves decentralization and freedom in the network, and is quite universal.

1. For each app in the network, a special user will appear, called the "app
sheriff". Such sheriffs can also be created for other purposes, but for now let's
focus on Google Play. An app installed not through Google Play will be free of
restrictions.
2. A user who wants their blog to be visible through the app must approve the
supervision of their blog by the sheriff. This means that the sheriff has extended
access to all content, except for private (Only me), and the node must obey
the sheriff's orders. Blogs that have not approved the supervision will not be
visible through the app.
3. At the moment, there is only one type of order: to place a sheriff's mark on
the specified post or comment. This mark is saved and returned to the client upon
request. The app, seeing this mark, hides the corresponding post or comment. At
the same time, in other apps, on other platforms, these posts and comments will
remain visible.
4. In the menu of posts and comments, when viewed through the app, there is an
item "Report..." With it, one can send a sheriff a report of a violation of the
rules, indicating the type of violation and an additional comment.
5. All complaints are public by default. The user can ask not to show his
complaint to everyone, in that case the complaint will be hidden until the
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
in the right to self-moderation or voluntary choice of an external moderator.