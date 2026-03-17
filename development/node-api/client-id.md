---
layout: development
title: Node API
up: node-api
subtitle: Client ID
---

# Client ID

Each Moera client may optionally provide a randomly generated client ID (CID).
It is passed to the node in the `Client-ID` [header][1].

The client ID has the following format:

```
Client-ID: <session-id>:<client-id>
```

`client-id` should be changed whenever the client is restarted;<br>
`session-id` may be left unchanged for longer periods of time.

Currently, there are two known use cases for the client ID:

1. If an event was created as a result of processing a REST API request of some 
   client, the event will contain a copy of the CID passed with the request.
   This mechanism allows the client to know that the event is a result of
   processing its own request. Usually such events are ignored because they
   contain information already known to the client.

2. Since all anonymous content is signed with the same key, the CID is used to
   distinguish anonymous content authors from each other. For this purpose,
   `session-id` part of the CID is stored along with the content for a short
   period of time. It acts as a temporary authentication token allowing
   the anonymous client to view the content authored by them when it is not
   public.

[1]: headers.html
