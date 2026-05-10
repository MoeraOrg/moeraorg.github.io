---
layout: overview
title: Media Files
next: browsing
next_title: Browsing
---

# Media Files

Media files are large immutable blocks of data that are usually stored
separately, either in a file system or in cheaper object storage. They
are stored as a single copy even if they are used in different
publications. A client often requests them directly from the storage,
without involving the node. So handling media files has some
differences that should be considered in detail.

## Grant

When a client requests a media file, either directly from the storage or
via API, it specifies only the media file identifier. This information
is not enough to verify whether the given client is allowed to access
the media file. Even if the request contained the publication
identifier, only the node itself could check the access rights. A simple
web server that serves media files from the storage has no such
capabilities.

To work around this limitation, the node does the following. When a
client requests a publication, the node checks the access rights to it.
If access is allowed, the node returns a list of media file URLs related
to this publication. It adds a _grant_ to each URL, a special
cryptographic token that allows the client to access the media file.

If the media file is served directly from the storage, a simple grant
structure is used, based on a hash function and a key known only to the
node and the web server.

If the media file is served via API, a grant signed with the node's
private key is used. Such a grant may also be used to access other APIs,
for example, to obtain detailed information about the media file, a list
of available resolutions, previews, etc. Besides that, a signed grant
has one more advantage: it may be used to access media files located on
other nodes.

## Lease

Usually, when a node composes a newsfeed or makes a repost of a
publication, it copies the whole publication to itself, including the
attached media files. But for very large media files this is too
wasteful. It would be useful to have a media file _lease_ mechanism that
allows a node to serve its clients a media file physically located on
another node, taking its access rights into account.

Let us consider two typical scenarios:

1. Bob copies Alice's post from her node, but does not copy the media
   file attached to the post.
2. Alice adds a comment to Bob's post on his node. The comment contains
   a media file that Alice uploaded to her node.

### Scenario 1

1. Bob copies Alice's post from her node.
2. Bob sends Alice a lease request, specifying Alice's post identifier
   and the media file identifier.
3. Alice checks Bob's right to access the post. If the post is
   accessible, Alice records on her side that Bob has received a lease
   and informs Bob about it. In the response, Alice specifies the lease
   identifier.
4. Bob records in the post that the attached media file is located on
   Alice's node and is available under a lease with this identifier.

### Scenario 2

1. Alice uploads a media file to her node.
2. Alice creates a lease for Bob on her node.
3. Alice sends a request to add a comment to Bob's post on his node.
   Alice indicates in the comment that a media file is attached to it
   and available under a lease with this identifier.
4. Bob checks Alice's right to add a comment to the post. If she is
   allowed to do so, Bob records the comment indicating the location of
   the media file and the lease identifier.

### Client Access

1. Carol requests a publication (a post or a comment) from Bob's node.
2. Bob checks Carol's right to access the publication. If she is
   allowed to do so, Bob returns the content of the publication,
   including the URL that may be used to obtain information about the
   media file on Alice's node. A grant signed by Bob is added to the
   URL.
3. Carol requests information about the media file from Alice's node,
   using the grant she received.
4. Alice checks that Bob has a lease for this media file. If the lease
   exists, Alice returns information about the media file, including the
   URL for downloading the media file itself. A grant signed by Alice is
   added to the URL.
5. Carol downloads the media file using the grant she received.

### Deleting the Publication

1. If the publication is deleted, Bob sends Alice a request to delete
   the lease, specifying the lease identifier.
2. Alice checks that the lease belongs to Bob and deletes it.

### Copying the Media File

1. If Bob wants to copy the media file to his node, he requests it from
   Alice using a grant that he signs for himself.
2. Alice checks that Bob has a lease for this media file. If the lease
   exists, Alice returns information about the media file, including the
   URL for downloading the media file itself. A grant signed by Alice is
   added to the URL.
3. Bob downloads the media file using the grant he received.
4. Bob stores the media file on his node.
5. Bob sends Alice a request to delete the lease, specifying the lease
   identifier.
6. Alice checks that the lease belongs to Bob and deletes it.

### Media File Deletion Notice

1. If Alice no longer wants to store the media file, she checks who has
   a lease for this media file.
2. Alice sends Bob a notice that the media file will be deleted soon.
3. If he wishes, Bob copies the media file to his node as described
   above.
4. After the specified time has passed, Alice deletes the media file and
   all leases associated with it from her node.

It is important to note that media files may be uploaded to a node
**only on its own initiative**. Media files are stored by whoever is
more interested in them, taking all costs and risks into account. If a
node does not want to store someone else's media file, it must accept
that the file may be deleted by its author and lost forever. If a
commenter does not want to store a media file, he may simply not attach
it to his comment.
