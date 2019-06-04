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

This header is sent by the website in HTTP response. It signals that the
website supports Moera REST API and the current page corresponds to the
Moera [virtual page][2] `<page>`. If `page` is not set, the current page
itself is considered to be a virtual page.

If `root` is set, it points to the *Moera root* of the website (matches
the website root by default). Virtual pages are located under `/moera`
subdirectory of the Moera root, the REST API endpoint is located at
`/moera/api`.

<h4 class="identifier">
    X-Accept-Moera: &lt;version>
</h4>

This header is sent by the client in HTTP request. It signals that the
client supports Moera REST API of the given version. Currently only
version `1.0` is defined.

[1]: /overview/browser-extension.html
[2]: /development/protocols/virtual-pages.html