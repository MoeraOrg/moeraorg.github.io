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

`/post/<id>`

Detailed view of the post with the given ID.

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
[2]: /development/protocols/headers.html
[3]: /development/protocols/moment.html