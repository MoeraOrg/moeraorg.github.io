---
layout: overview
title: Browsing
next: permissions
next_title: Permissions
---

# Browsing

A user of a centralized social network sees it as one big website. He
opens this site in a web browser and uses the site's UI to surf through
the social network.

As we [said above][1], Moera is not a single website, it is a web of
sites. The best way to surf through it is with an "upgraded" browser.
The browser should handle some sort of URIs designating a post, feed or profile
in Moera, like
```
moera:<node name>/<location>
```
and open this location in a *Moera web client*.

Unfortunately, it is currently impossible to configure a web browser to handle
a different URI scheme. That's why Moera uses a regular URL instead. The Moera
URL has the following form:
```
https://moera.page/@<node name>/<node host>/<location>
```
For example:
```
https://moera.page/@lamed/lamed.moera.blog/post/99d6af7f
```
Let's analyze what the URL is built of.

### Redirector

The host `moera.page` used in the URL is the Moera redirector. When a user
opens a Moera URL, the `moera.page` host redirects the browser to a default
Moera web client. If the user wants to change the preferred web client, there
is a special UI at `https://moera.page/set-client?client=<domain name>` for
doing this. The user's choice is saved in cookies and `moera.page` reads
the cookies when doing the redirection.

### Node Name and Node Host

The web client uses the [node name][1] and the node host in the URL to open
a correct node. Each of them is optional, but the corresponding element in the
URL should be present. If the node name is not known, it should be written
as `/@/`. If the node host is not known, it should be written as `/~/`.

Essentially, there is enough to know the node name to locate the node. The
client just needs to resolve the name through the Moera naming service. But the
presence of the host in the URL makes the process faster. If the node host is
known, the client tries to open it first. Later, if the hostname returned by the
naming service appears to be different, the client opens it instead. The
redirector (see the previous chapter) can also put the correct hostname into the
URL if it knows it at the moment of redirection.

If the node does not have a registered name, or it is not known, the node host
in the URL becomes the only way to locate the node. If the node host is not set
as well, the user's home node is used if it is known to the client.

If the node uses a protocol other than HTTPS or a different port, they should
be specified with the host name, like `http:localhost:8000`.

### Virtual Page

The location part of the URL is called a *virtual page*. 

As we said before, Moera REST API may be implemented by any site and
sites may have different structures. For example, on one site the
"Contacts" page may have location `/contact-us.html` and on another
site — `/info/contacts.php`, but both correspond to the same Moera
virtual page `/profile`.

All virtual pages have standard names, this simplifies interactions between a
client and node. For example, if user `Arthur` is mentioned in a comment
somewhere, and we know that his node hostname is `arthur.earth.org`, we can link
his name to `https://moera.page/@Arthur/arthur.earth.org/profile` and be sure
that the link points to `Arthur`'s profile. This does not mean the page
`https://arthur.earth.org/profile` exists — that's why these pages are called
*virtual*.

## Discovery

There are two problems with the redirector approach that we need to solve
somehow. The first one is the **discovery** problem:

>When you visit some site, you don't know whether it supports Moera. Even
if somehow you find out, you will need to open the Moera client and enter
the same address into it.

The problem may be solved by the site itself by displaying the Moera logo
somewhere with a Moera link to the site. But we should take into account that

>We cannot trust the node because it may open a malicious client.

The solution is to make all Moera-capable sites manifest themselves by adding
a special HTTP header (`X-Moera`) to their HTTP response. A browser extension
may detect this header and open a Moera web client automatically.

## Single Point of Failure

The second problem is that the redirector becomes a single point of failure.
The redirector must be highly-available, secure and handle a lot of traffic.
It also puts decentralization in danger.

To mitigate this problem, the Moera URL handling and redirection should happen
in the browser itself, without actually sending requests to `moera.page` host.
A browser extension may be used for this task.

[1]: /overview/naming.html
