---
layout: development
title: Protocols
up: protocols
subtitle: Virtual Pages
---

# Virtual Pages

These are standard virtual pages supported by Moera nodes.
[Read more][1] about virtual pages in the Architecture Overview section.

Virtual pages are located under `/moera` subdirectory of the *Moera
root* of the website (matches the website root by default, may be
changed by `X-Moera` [header][2]).

<h4 class="identifier">/api-docs</h4>

Node API specification in OpenAPI format.

<h4 class="identifier">/api-ui.html</h4>

Web interface for executing node API requests.

<h4 class="identifier">/complains</h4>

_(for sheriffs only)_ Complaints management interface.

<h4 class="identifier">/complains/{id}</h4>

_(for sheriffs only)_ Management interface for a particular group of complaints,
related to the same posting or comment.

<h4 class="identifier">/compose?id={id}</h4>

Post composer. If `id` is not provided, the composer is opened for
creating a new post; otherwise it is opened for editing the post with
the given ID.

<h4 class="identifier">/compose?draft={id}</h4>

Post composer opened for creating a new post, with a draft loaded. ID of
the draft is passed in the `draft` parameter.

<h4 class="identifier">/gotoname?client={client URL}&name={node name}&location={path}&trackingId={id}</h4>

Resolve the given node `name` and open the given `location` at it. If `client` is
given, it is opened and the location is passed to it. If `trackingId` is given,
the story with this tracking ID is marked as read.

<h4 class="identifier">
    /media/private/{id}.{extension}?width={number}&download={true or false}
</h4>

Private media file. The `{extension}` does not affect the result.

The optional `width` parameter is the preferred width of the media in pixels.
The node will try to return the smallest in size, but the best in quality variant
of the media, according to the width provided.

If the `download` parameter is present and set to `true`, the node will add
`Content-Disposition: attachment` header to the output.

<h4 class="identifier">/media/public/{id}.{extension}?width={number}&download={true or false}</h4>

Public media file. The `<extension>` does not affect the result.

The optional `width` parameter is the preferred width of the media in pixels.
The node will try to return the smallest in size, but the best in quality variant
of the media, according to the width provided.

If the `download` parameter is present and set to `true`, the node will add
`Content-Disposition: attachment` header to the output.

<h4 class="identifier">/news</h4>

Newsfeed — publications from the nodes this node is subscribed to in
reverse chronological order.

<h4 class="identifier">/news?before={moment}</h4>

Newsfeed, positioned at about the given [moment][3].

<h4 class="identifier">/people</h4>

Information related to other nodes.

<h4 class="identifier">/people/subscribers</h4>

Information about subscribers of this node.

<h4 class="identifier">/people/subscriptions</h4>

Information about subscriptions of this node.

<h4 class="identifier">/people/friend-ofs</h4>

Information about nodes that added this node to their friends.

<h4 class="identifier">/people/blocked</h4>

Information about nodes blocked by this node.

<h4 class="identifier">/people/blocked-by</h4>

Information about nodes that blocked this node.

<h4 class="identifier">/people/{id}</h4>

Information about friends of this node that are members of the group of friends
with the given ID.

<h4 class="identifier">/post/{id}</h4>

Detailed view of the post with the given ID.

<h4 class="identifier">/post/{id}?comment={commentId}</h4>

View of the comment with the given ID to the given post.

<h4 class="identifier">/post/{id}?media={mediaId}</h4>

View of the media with the given ID attached to the given post.

<h4 class="identifier">/post/{id}?comment={commentId}&media={mediaId}</h4>

View of the media with the given ID attached to the given comment to the given post.

<h4 class="identifier">/profile</h4>

Profile — the detailed information about the node's owner, node's
purpose etc.

<h4 class="identifier">/profile?edit=true</h4>

Profile in editing mode.

<h4 class="identifier">/settings</h4>

Settings page.

<h4 class="identifier">/settings/{tab}</h4>

Settings page with the given tab open (one of `node` or `client`).

<h4 class="identifier">/timeline</h4>

Timeline - all publications in reverse chronological order.

<h4 class="identifier">/timeline?before={moment}</h4>

Timeline, positioned at about the given [moment][3].

[1]: /overview/browser-extension.html
<!-- @IGNORE PREVIOUS: link -->
[2]: /development/protocols/headers.html
<!-- @IGNORE PREVIOUS: link -->
[3]: /development/protocols/moment.html
<!-- @IGNORE PREVIOUS: link -->
