---
layout: development
title: Node API
up: node-api
subtitle: Headers
---

# Headers

These are special Moera HTTP headers. [Read more][1] about them in the
Architecture Overview section.

## Clients

<h4 class="identifier">
    X-Moera: [root={root}] [page={page}]
</h4>

This header is sent by a website in HTTP response. It signals that the
website supports Moera REST API and the current page corresponds to the
Moera [virtual page][2] `{page}`. If `page` is not set, the current page
itself is considered to be a virtual page.

If `root` is set, it points to the *Moera root* of the website (matches
the website root by default). Virtual pages are located under `/moera`
subdirectory of the Moera root, the REST API endpoint is located at
`/moera/api`.

<h4 class="identifier">
    X-Accept-Moera: {version}
</h4>

This header is sent by the client in HTTP request. It signals that the
client supports Moera REST API of the given version. Currently only
version `1.0` is defined.

Node that usually redirects all non-API requests to a web client should
disable this behavior when receives this header.

## Plugins

<h4 class="identifier">
    X-Moera-Auth: [root-admin={true or false}]
        [admin={true or false}]
        [auth-category={comma-separated list}]
        [client-name={name}]
        [remote-address={IP address}]
        [user-agent={browser name}]
        [user-agent-os={OS name}]
        [node-id={ID}]
        [node-name={node name}]
        [domain-name={domain name}]
</h4>

This header is sent by the node to a plugin when forwarding a user request to it.
All fields have the same meaning as corresponding fields of
<code><a href="requests.html#PluginContext">PluginContext</a></code>
structure.

<h4 class="identifier">
    X-Moera-Origin: {url}
</h4>

This header is sent by the node to a plugin when forwarding a user request to it.
It contains the full URL of the user request.

[1]: /overview/browsing.html
[2]: virtual-pages.html
