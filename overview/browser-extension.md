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
node returns the authentication token that has to be used in all
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
      <th class="col-2">&nbsp;</th>
      <th class="col-5"><code class="highlighter-rouge">/contact-us.html</code></th>
      <th class="col-5"><code class="highlighter-rouge">/moera/profile</code></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>No extension</th>
      <td>HTML page</td>
      <td>Redirect to <code class="highlighter-rouge">/contact-us.html</code></td>
    </tr>
    <tr>
      <th>With extension</th>
      <td>Empty page, <code class="highlighter-rouge">X-Moera</code> points to <code class="highlighter-rouge">/moera/profile</code> (content is replaced by client)</td>
      <td>Empty page, <code class="highlighter-rouge">X-Moera</code> (content is replaced by client)</td>
    </tr>
  </tbody>
</table>

## Standalone approach

Why at all we need this browser extension? Why we cannot create a
regular web application, put it on some website and let users to open it
and use as Moera web client, without installing anything into the
browser? It would be much easier and user-friendly.

Yes, it is possible, at least theoretically. But we need to solve two
problems that arise:

* **Discovery.** When you visit some site, you don't know whether it
  supports Moera. Even if somehow you find out, you will need to open
  the Moera client and enter the same address into it.
* **Links.** You cannot just copy the address in the address bar and
  send it to you friend, because this address points to your web client,
  but your friend may use some other client. You need a way to get a
  client-independent link and make it open your friend's preferred web
  client when entered in a browser.

The first problem may be solved by the site itself by displaying the
Moera logo somewhere with a client-independent Moera link to the site.
Which brings us again to the second problem.

To solve the second problem we can establish a special host for Moera
redirections, let's call it `r.moera.org`. Then, the algorithm is
as following:

1. Each user must go to `r.moera.org` and enter the URL of his
   preferred Moera web client there. For example,
   `https://client.moera.net`. It is saved in the cookies.
2. When somebody wants to share a link to some post, he must use a
   special "Copy Link to Post" button provided by his client. The link
   will be in the form `https://r.moera.org/roxxon.corp/posts/42`.
3. When the friend receives the link and enters it into a browser,
   `r.moera.org` will take the client URL from the cookies and will make
   redirection to `https://client.moera.net/roxxon.corp/posts/42`.

With this approach, users must take care not to share the links that
appear in the address bar. But experience has shown that they will
continue to do that. This will cause frustration when the receiver
clicks the link and it is opened in an unfamiliar client. It may even
lead to security issues, if the receiver enters login/password of his
home node in this client.

Besides not so smooth UI, this solution creates the central point of
failure: `r.moera.org` that must be highly-available and handle a lot of
traffic. Also, if the web client is built into the browser extension, it
loads faster, cannot be mutated and do not create traffic from the
website, where the client is located in the scheme described above.

The browser extension may also have other features that improve user
experience.

But, although I strongly recommend to use the browser extension, the
standalone approach is likely to be implemented in some form anyway.

[1]: /overview/node.html
