---
layout: overview
title: Notifications
next: newsfeed
next_title: Newsfeed
---

# Notifications

Nodes can receive notifications about certain events from naming servers
and other nodes. Notifications are sent through the REST API of the
receiving node.

Some notifications are sent without subscribing to them — for example,
the notification about mentioning your name somewhere. But most
notifications require subscription.

Special measures are needed to make impossible to use the notification
protocol for DoS attacks — when the attacker subscribes someone else's
site to a lot of notifications.

The subscription request must contain the registered name of the
receiver and must be signed by its signing key. Only the latest
generation of the name is allowed. The name in the subscription request
must be node's *primary name*, i.e. the name reported by the node
itself.

In response to a notification, the receiver may point out that it does
not want to receive further notifications about this event. So if a node
receives a notification it shouldn't receive, the node can unsubscribe
from it immediately, without a separate request.

The first notification that the subscriber receives is always the
subscription notification. Until the subscriber responds to this
notification positively, the subscription is not considered confirmed
and no other notifications of this type are sent to the subscriber.

To receive notifications, the node must always be online. If a
notification cannot be delivered, the sender must put it and further
notifications to a queue and retry the delivery for some period of time.
If notifications cannot be delivered to the receiver for a long time,
the sender may unsubscribe the receiver and remove the queue. When the
receiving node comes online again after a long period of downtime, it
will require a recovery process to restore the subscriptions and refresh
the important data.

Big naming servers and nodes with millions of subscribers might not be
able to handle the large volume of notifications they have to send. For
this purpose, special notification delivery networks may be developed
that use more effective algorithms of delivery.

## Client notifications

An active client may use WebSockets to receive notifications about
recent updates from the home node and the node it is viewing currently.
This allows making the UI more responsive. The node begins to send
these notifications when a client opens a connection to it. To handle
intermittent connections, the node keeps a short queue of recent events
and the client, when reconnects, reports the timestamp of the last
notification it has seen.