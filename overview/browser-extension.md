---
layout: overview
title: Browser Extension
body_class: body-green
next: permissions
---

# Browser Extension

User of a centralized social network sees it as one big website. He
opens this site in a web browser and uses the site's UI to surf through
the social network.

As we [said above][1], Moera is not a single website, it is a web of
sites. The best way to surf through it is with an "upgraded" browser. We
use a combination of a web application and a browser extension to
achieve this goal.

1. When the user opens a Moera-capable site with his browser, the site
   includes a special `X-Moera` HTTP header to the response. This is an
   indication that the site supports Moera [REST API][1]. (The header
   may also contain the list of supported API capabilities and the
   location of the API endpoint.)
2. The browser extension detects the `X-Moera` header and **replaces**
   the HTML page returned by the site with a special *Moera web client*
   \- the one-page web application. The code of the application may be
   built into the browser extension or downloaded from a remote host.
3. The user uses the web client to surf through the content of this
   node. The web client interacts with the node via REST API.
4. When the user clicks an external link, the target website is opened
   in the browser as usual. If the target website is also a Moera node,
   steps 1-3 are repeated.

## Connect to home

Many Moera features depend on an established connection with the home
node. The user must sign into the home node with his credentials; the
node returns the authorization token that has to be used in all
subsequent interactions with the home node.

It's pretty obvious that we cannot use browser cookies to pass this
token to the web client. So the browser extension passes it directly
using the in-browser messaging mechanism. And the extension's local
storage is used for storing the token securely between the sessions.

## Virtual pages

When you open a web page, you can copy the link displayed in the address
bar of the browser and share it with someone else. Your friend may enter
this link into her browser and see the same page. This is the basic
functionality of the web.

Similarly, when you surf the node content with the web client, the URL
in the address bar is changing accordingly. If you copy this URL and
share it with someone else, she should be able to enter it into her
browser and see the same page. But it doesn't work out of the box,
because the URLs constructed by Moera web client are *virtual* - there
is no such page on the site itself.

Virtual pages have special prefix (for example, `/moera/`) that
distinguishes them from all *real* pages on the site. There are two main
reasons, why we use the virtual pages in the Moera web client:

* Some pages that may be opened in the client are absent from the web
  UI. Either because they have no meaning in the web UI (for example,
  web client settings page), or because they are not public (for
  example, list of friend groups).
* As we said before, Moera REST API may be implemented by any site and
  sites may have different structure. For example, on one site the
  "Contacts" page may have location `/contact-us.html` and on another
  site - `/info/contacts.php`, but both correspond to the same Moera
  virtual page `/moera/profile`. All virtual pages have standard names,
  this simplifies interactions between client and node. For example, if
  user `arthur` is mentioned in a comment somewhere, and we know that
  his node URL is `https://arthur.earth.org`, we can link his name to
  `https://arthur.earth.org/moera/profile` and be sure that the link
  points to `arthur`'s profile.

To make both real and virtual pages work, we do the following:

* The browser extension adds `X-Accept-Moera` HTTP header to all HTTP
  requests to inform the node that the browser supports Moera.
* `X-Moera` HTTP header in the response may contain the location of the
  virtual page that should be opened in the Moera web client.

The table summarises what response the node should send for each URL.

<table class="table table-bordered">
  <thead>
    <tr>
      <th>&nbsp;</th>
      <th><code class="highlighter-rouge">/contact-us.html</code></th>
      <th><code class="highlighter-rouge">/moera/profile</code></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>No extension</td>
      <td>HTML page</td>
      <td>Redirect to <code class="highlighter-rouge">/contact-us.html</code></td>
    </tr>
    <tr>
      <td>With extension</td>
      <td>Empty page, <code class="highlighter-rouge">X-Moera</code> points to <code class="highlighter-rouge">/moera/profile</code> (content replaced by client)</td>
      <td>Empty page, <code class="highlighter-rouge">X-Moera</code> (content replaced by client)</td>
    </tr>
  </tbody>
</table>

[1]: /overview/node.html
