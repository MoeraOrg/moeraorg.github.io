---
layout: development
title: Node API
up: node-api
subtitle: OAuth2
---

# OAuth2

[OAuth2][1] is a secure authorization framework that lets third-party
applications obtain tokens to access user data.

To use a standard OAuth2 flow, an application must first register with the
target service. After registration, the application receives a client ID and
client secret, which are later used for authorization.

In Moera, this process is simplified by registering a name in the Moera [naming
service][2]. The registered name becomes the application's client ID, and
a [carte][3], signed with the private signing key, serves as the client secret.

After the target node's owner authorizes the application, the node adds the
application's name to a list of names with special privileges. The application
doesn’t need an additional token to use these privileges. Instead, the
application authenticates as usual using a carte and sets the `adminScope`
[field][4] in the carte to indicate the privileges it intends to use.

Here is the Moera OAuth2 flow:

1. The application registers a name with the Moera naming service.
2. The application generates a carte for authentication on the target node,
   with `clientScope` field containing `grant`.
3. The application redirects the user to `https://moera.page/@/~/grant` with
   the following query parameters:
   * `client_id=` the application's registered name;
   * `client_secret=` the carte generated in step 2;
   * `scope=` a comma- or space-separated list of [privileges][5]
     the application is requesting;
   * `redirect_uri=` the URL to redirect to after successful authorization
     (see step 6).
4. The Moera client validates the request and prompts the user to authorize
   the application, showing its name and the requested privileges.
5. If the user confirms, the Moera client sends a request to the user's home
   node to record the application's new privileges.
6. Upon a successful response from the node, the Moera client redirects the user
   to the `redirect_uri`. If no URL is provided, the client informs the user
   that the process is complete and that the page can be closed.

[1]: https://oauth.net/2/
[2]: /overview/naming.html
[3]: authentication.html#carte
[4]: fingerprints.html#Carte
[5]: requests.html#Scope