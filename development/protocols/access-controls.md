---
layout: development
title: Protocols
up: protocols
subtitle: Access Controls
body_class: body-pink
---

# Access Controls

Node API allows to define, who has access to the content of the node - postings,
comments, reactions, media files etc. Each one of these objects has a set of
_operations_ like view, edit, delete and so on and every operation is assigned
a _principal_. Principal is a string that defines which client or a group of
clients has a permission to perform the operation.

Operations are returned together with the content of the object from
the corresponding API calls. To save traffic, only operations that have
non-default values are returned. To update the operations, use the same API calls
that create or update the object.

Read also [the overview of the permissions architecture](/overview/permissions.html)
in Moera.

## Hierarchy of Objects

Objects are organized into hierarchy, as follows:

* Node
  * Node name
  * Profile
  * Feed
  * Story
  * Posting
    * Comment
      * Reaction
    * Reaction
  * Media file
  * Draft
  * People info
  * Contact
  * Subscriber
  * Subscription
  * Friend group

Every object has its own set of operations. But, in many cases, several
operations need to be permitted to perform a particular request. For example, to
add a negative reaction to a posting, the client needs to have access to both
`addReaction` and `addNegativeReaction` operations. To view a comment the client
needs both `view` on the comment itself and `viewComments` on the posting.

Objects on higher levels may override permissions of the objects on lower levels.
For example, comment's author may disable negative reactions to his comment by
setting `addNegativeReaction` operation to `none`. But posting's author may
override this permission to force all comments to the posting to accept negative
reactions. When the client queries an object, it will get both the object's own
operations and the overrides coming from the higher levels of the hierarchy.

## Principals


### Simple Principals

Simple principals allow the operation to the object's owner and owners of
higher-level objects (node admin is the owner of the node). The following tables
describe how simple principals are defined for objects on different levels of the
hierarchy.

The rightmost column in the table is the principal. Other columns correspond to
the owner of the object and owners of higher-level objects in the hierarchy.

`+` - the access is allowed\
`-` - the access is not allowed 

#### Level 1

<table class="table table-bordered">
  <thead>
    <tr>
      <th>node owner</th>
      <th>object owner</th>
      <th>&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>+</td>
      <td>+</td>
      <td><code>private</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>+</td>
      <td><code>secret</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>+</td>
      <td><code>enigma</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td><code>senior</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td><code>major</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td><code>admin</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td>+</td>
      <td><code>owner</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td><code>none</code></td>
    </tr>
  </tbody>
</table>

#### Level 2

<table class="table table-bordered">
  <thead>
    <tr>
      <th>node owner</th>
      <th>posting owner</th>
      <th>object owner</th>
      <th>&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td><code>private</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td>+</td>
      <td><code>secret</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td>+</td>
      <td><code>enigma</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>+</td>
      <td>-</td>
      <td><code>senior</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td>-</td>
      <td><code>major</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td>-</td>
      <td><code>admin</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>+</td>
      <td><code>owner</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td><code>none</code></td>
    </tr>
  </tbody>
</table>

#### Level 3

<table class="table table-bordered">
  <thead>
    <tr>
      <th>node owner</th>
      <th>posting owner</th>
      <th>comment owner</th>
      <th>object owner</th>
      <th>&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td><code>private</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>+</td>
      <td>-</td>
      <td>+</td>
      <td><code>secret</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td>-</td>
      <td>+</td>
      <td><code>enigma</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>-</td>
      <td><code>senior</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>+</td>
      <td>-</td>
      <td>-</td>
      <td><code>major</code></td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td><code>admin</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>+</td>
      <td><code>owner</code></td>
    </tr>
    <tr>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td><code>none</code></td>
    </tr>
  </tbody>
</table>

### Complex Principals

`node:<list of node names>`

Allows the operation to the node's admin and to all nodes in the list. Names in
the list are separated by commas.

`only:<list of node names>`

Allows the operation to all nodes in the list. Names in the list are separated by
commas.

`f:<friend group ID>`

Allows the operation to the node's admin and to the members of a particular group
of friends.

`subscribed`

Allows the operation to the node's admin and to all nodes this node is subscribed
to.

`signed`

Allows the operation to any authenticated client.

`public`

Allows the operation to any client, including unauthenticated.

`unset`

This is a special value used in overrides. It means that the higher-level object
does not override the permission, so the object's own permission take effect. 