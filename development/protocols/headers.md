---
layout: development
title: Protocols
up: protocols
subtitle: Headers
body_class: body-pink
---

# Headers

These are special Moera HTTP headers. [Read more][1] about them in the
Overview section.

<h4 class="identifier">
    X-Moera: [root=&lt;root>] [page=&lt;page>]
</h4>

This header is sent by a website in HTTP response. It signals that the
website supports Moera REST API and the current page corresponds to the
Moera [virtual page][2] `<page>`. If `page` is not set, the current page
itself is considered to be a virtual page.

If `root` is set, it points to the *Moera root* of the website (matches
the website root by default). Virtual pages are located under `/moera`
subdirectory of the Moera root, the REST API endpoint is located at
`/moera/api`.

<h4 class="identifier">
    X-Moera: redirect=&lt;url> [connectedOnly=&lt;true or false>]
</h4>

This header is sent by a standalone web client in HTTP response. If
browser extension detects it, it immediately performs HTTP redirect to
the `<url>` specified in the `redirect` parameter. If `connectedOnly`
parameter is set to `true` and the browser extension has no connection
data yet, the redirect is delayed until the web client starts and
transfers its connection data to the browser extension.

This mechanism allows users that have the browser extension installed to
seamlessly move from a standalone web client to the browser
extension-based client.

<h4 class="identifier">
    X-Accept-Moera: &lt;version>
</h4>

This header is sent by the client in HTTP request. It signals that the
client supports Moera REST API of the given version. Currently only
version `1.0` is defined.

[1]: /overview/browser-extension.html
[2]: /development/protocols/virtual-pages.html