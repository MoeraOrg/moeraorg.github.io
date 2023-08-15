---
layout: overview
title: Browser Extension
body_class: body-green
next: permissions
---

# Browser Extension

A user of a centralized social network sees it as one big website. He
opens this site in a web browser and uses the site's UI to surf through
the social network.

As we [said above][1], Moera is not a single website, it is a web of
sites. The best way to surf through it is with an "upgraded" browser. We
use a combination of a web application and a browser extension to
achieve this goal.

1. When the user opens a Moera-capable site with his browser, the site
   includes a special `X-Moera` HTTP header into the response. This is
   an indication that the site supports Moera [REST API][1]. (The header
   may also contain the list of supported API capabilities and the
   location of the API endpoint.)
2. The browser extension detects the `X-Moera` header and redirects the browser
   to a special *Moera web client* - the one-page web application.
   The original URL is passed to the web client.
3. The user uses the web client to surf through the content of this
   node. The web client interacts with the node via REST API.
4. When the user clicks an external link, the web client prefetches the target
   page and checks for `X-Moera` header. If it is found, the target page is
   opened in the same client. Otherwise, it as opened in the browser as
   a regular page.

## Connect to home

Many Moera features depend on an established connection with the home
node. The user must sign in to the home node with his credentials; the
node returns the authentication token that has to be used in all
subsequent interactions with the home node.

The web client uses the browser's local storage to store the token securely
between the sessions.

## Virtual pages

When you open a web page, you can copy the link displayed in the address
bar of the browser and share it with someone else. Your friend may enter
this link into her browser and see the same page. This is the basic
functionality of the web.

It doesn't work the same for the web client because the link in the address
bar points to the web client, not to the page itself, and your friend may use
a different web client. So you should use a 'Copy link' or 'Share' button in
the web client to get a correct URL.

And there is one more detail. The URLs constructed by Moera web client are
*virtual* - there is no such page on the site exists.

Virtual pages have special prefix (for example, `/moera/`) that
distinguishes them from all *real* pages on the site. There are two main
reasons why we use the virtual pages in the Moera web client:

* Some pages that may be opened in the client are absent from the web
  UI. Either because they have no meaning in the web UI (for example,
  web client settings page), or because they are not public (for
  example, the list of friend groups).
* As we said before, Moera REST API may be implemented by any site and
  sites may have different structures. For example, on one site the
  "Contacts" page may have location `/contact-us.html` and on another
  site - `/info/contacts.php`, but both correspond to the same Moera
  virtual page `/moera/profile`. All virtual pages have standard names,
  this simplifies interactions between a client and node. For example, if
  user `arthur` is mentioned in a comment somewhere, and we know that
  his node URL is `https://arthur.earth.org`, we can link his name to
  `https://arthur.earth.org/moera/profile` and be sure that the link
  points to `arthur`'s profile.

To make both real and virtual pages work, we do the following:

* The browser extension adds `X-Accept-Moera` HTTP header to all HTTP
  requests to inform the node that the browser supports Moera.
* `X-Moera` HTTP header in the response may contain the location of the
  virtual page that should be opened in the Moera web client.

The table summarizes what response the node should send for each URL.

<table class="table table-bordered">
  <thead>
    <tr>
      <th class="col-2">&nbsp;</th>
      <th class="col-5"><code>/contact-us.html</code></th>
      <th class="col-5"><code>/moera/profile</code></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>No extension</th>
      <td>HTML page</td>
      <td>Redirect to the default Moera web client to <code>/moera/profile</code> page</td>
    </tr>
    <tr>
      <th>With extension</th>
      <td>Empty page, <code class="highlighter-rouge">X-Moera</code> points to <code class="highlighter-rouge">/moera/profile</code> (the extension redirects to the web client)</td>
      <td>Empty page, <code class="highlighter-rouge">X-Moera</code> (the extension redirects to the web client)</td>
    </tr>
  </tbody>
</table>

## Without the extension

Why at all we need this browser extension? Why cannot we create a
regular web application, put it on some website and let users open it
and use as a Moera web client, without installing anything into the
browser? It would be much easier and user-friendly.

Yes, it is possible, at least theoretically. But we need to solve
the **discovery** problem:

_When you visit some site, you don't know whether it supports Moera. Even
if somehow you find out, you will need to open the Moera client and enter
the same address into it._

The problem may be solved by the site itself by displaying the
Moera logo somewhere with a client-independent Moera link to the site.
Which brings us to the second problem:

_The site does not know which client the user prefers._

To solve the second problem we can establish a special host for Moera
redirections, let's call it `r.moera.org`. Then, the algorithm is
as following:

1. Each user must go to `r.moera.org` and enter the URL of his
   preferred Moera web client there. For example,
   `https://client.moera.net`. It is saved in the cookies.
2. When somebody wants to share a link to some post, they must use a
   special 'Copy Link' or 'Share' button provided by his client. The link
   will be in the form `https://r.moera.org/roxxon.corp/posts/42`.
3. When the friend receives the link and enters it into a browser,
   `r.moera.org` will take the client URL from the cookies and make
   redirection to `https://client.moera.net/roxxon.corp/posts/42`.

This solution creates a central point of failure: `r.moera.org`. It must be
highly-available and handle a lot of traffic.

The browser extension may also have other features that improve user
experience.

But although I strongly recommend using the browser extension, it is likely
that the majority of users will not install it.

[1]: /overview/node.html
