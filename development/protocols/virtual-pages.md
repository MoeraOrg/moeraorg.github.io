---
layout: development
title: Protocols
up: protocols
subtitle: Virtual Pages
body_class: body-pink
---

# Virtual Pages

These are standard virtual pages supported by Moera nodes.
[Read more][1] about virtual pages in the Overview section.

Virtual pages are located under `/moera` subdirectory of the *Moera
root* of the website (matches the website root by default, may be
changed by [`X-Moera` header][2]).

`/compose?id=<id>`

Post composer. If `id` is not provided, the composer is opened for
creating a new post, otherwise it is opened for editing the post with
the given ID.

`/compose?draft=<id>`

Post composer opened for creating a new post, with a draft loaded. ID of
the draft is passed in the `draft` parameter.

`/media/private/<id>.<extension>`

Private media file. The `extension` does not affect the result.

`/media/public/<id>.<extension>`

Public media file. The `extension` does not affect the result.

`/news`

Newsfeed - publications from the nodes this node is subscribed to in
reverse chronological order.

`/news?before=<moment>`

Newsfeed, positioned at about the given [moment][3].

`/people`

Information related to other nodes.

`/people/subscribers`

Information about subscribers of this node.

`/people/subscriptions`

Information about subscriptions of this node.

`/post/<id>`

Detailed view of the post with the given ID.

`/post/<id>?comment=<commentId>`

View of the comment with the given ID to the given post.

`/post/<id>?media=<mediaId>`

View of the media with the given ID attached to the given post.

`/post/<id>?comment=<commentId>&media=<mediaId>`

View of the media with the given ID attached to the given comment to the given post.

`/profile`

Profile - the detailed information about the node's owner, node's
purpose etc.

`/profile?edit=true`

Profile in editing mode.

`/settings`

Settings page.

`/settings/<tab>`

Settings page with the given tab open (may be `node` or `client`).

`/timeline`

Timeline - all publications in reverse chronological order.

`/timeline?before=<moment>`

Timeline, positioned at about the given [moment][3].

[1]: /overview/browser-extension.html
<!-- @IGNORE PREVIOUS: link -->
[2]: /development/protocols/headers.html
<!-- @IGNORE PREVIOUS: link -->
[3]: /development/protocols/moment.html
<!-- @IGNORE PREVIOUS: link -->
