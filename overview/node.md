---
layout: overview
title: Node
body_class: body-green
next: authentication
---

# Node

So we return to the original idea of the World Wide Web: every user,
group, organization or project has his own website. We will call it
*node*. Installation of a node is made as simple as possible - you
install one package, run one script or deploy one container, and your
node is up and running.

Node provides to the outer world two interfaces: Web UI and REST API.

##### Web UI

The Web UI is a simple non-interactive website that displays the public
content of the node. For example, if the node is used as blog, the Web
UI will contain public part of the user's profile, all public posts,
public comments, photos in public albums etc.

The first goal of the Web UI is to allow regular Internet users to
browse the node's content without need to install any special software
or registering anywhere. This also solves a chicken-and-egg problem of
social networks - even if there are not so many users that have Moera
software installed, you always have readers from outside.

The second goal is to allow search engines to index the public content
of the node. All possible (and fair) search engine optimizations should
be utilized.

##### REST API

The REST API is the gateway to all features of the node. It allows to
authenticate, read and post public and private content, change settings,
get notifications and so on. The REST API must be open, standardized and
well-documented, anybody must be able to use and implement it in any
software.

Web clients and mobile clients use REST API for all operations.
Automated operations, like backups, reposts from other social networks,
data migration, specialized Moera search engines etc. also use it.
REST API is also used for inter-node communication - receiving
[notifications][2], fetching new posts for the [newsfeed][3] etc.

Node REST API may be implemented (fully or partially) by any existing
website, making its content available for reading and commenting with
Moera client, for reposting to other nodes in Moera network, for adding
to the newsfeed etc. The site becomes part of the social network without
the need to copy every post, to have comments in different places and to
hire a separate person to maintain this. It is possible to distribute a
Moera REST API implementation as a plugin for popular content management
systems (Wordpress, Joomla etc.), so any site using a CMS may be
converted to Moera node in one click.

##### \* \* \*

You may think about this as a backward-compatible "upgrade" of the Web.

The regular web server implements HTTP protocol. User connects to it
with a web browser and the server returns data in HTML format that the
browser knows to display.

The Moera node implements Moera node protocol (REST API). User connects
to it with the Moera client (which is a web browser with [add-on][1] or
a separate application on mobile) and the server returns social network
data in a structured form that the client knows to display.

But, for backward compatibility, if user connects with a Moera-capable
browser to a site that does not provide Moera API, it will show the
regular HTML interface. And other way around, if user connects with a
regular web browser to a Moera-capable site, it will show the fallback
Web UI described above.

[1]: /overview/browser-extension.html
[2]: /overview/notifications.html
[3]: /overview/newsfeed.html
