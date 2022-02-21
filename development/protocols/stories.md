---
layout: development
title: Protocols
up: protocols
subtitle: Stories
body_class: body-pink
---

# Stories
Stories describe something happening in Moera, they are building blocks
for feeds. All stories have
[the same structure](node-api.html#StoryInfo)<!-- @IGNORE PREVIOUS: anchor -->,
but the meaning of fields depends on the story type. A story may
reference a posting, a remote object etc. Some feeds may not allow some
types of stories.

`POSTING_ADDED`

A posting was added. `posting` field refers to the posting. This type of
story is used for feeds containing postings.

`REACTION_ADDED_POSITIVE`

A positive reaction was added to user's posting. `posting` field refers
to the posting.

`REACTION_ADDED_NEGATIVE`

A negative reaction was added to user's posting. `posting` field refers
to the posting.

`MENTION_POSTING`

The user was mentioned in a posting on another node. `remoteNodeName`
and `remotePostingId` fields refer to the node and the posting on it,
respectively.

`SUBSCRIBER_ADDED`

Another node subscribed to user's feed.

`SUBSCRIBER_DELETED`

Another node unsubscribed from user's feed.

`COMMENT_ADDED`

A comment was added under user's posting.

`MENTION_COMMENT`

The user was mentioned in a comment.

`REPLY_COMMENT`

A reply was added to user's comment.

`COMMENT_REACTION_ADDED_POSITIVE`

A positive reaction was added to user's comment.

`COMMENT_REACTION_ADDED_NEGATIVE`

A negative reaction was added to user's comment.

`REMOTE_COMMENT_ADDED`

A comment was added under a posting the user is subscribed to.

`COMMENT_POST_TASK_FAILED`

A failed attempt to post a comment.

`COMMENT_UPDATE_TASK_FAILED`

A failed attempt to update a comment.

`POSTING_UPDATED`

A posting was updated.

`POSTING_POST_TASK_FAILED`

A failed attempt to create a posting.

`POSTING_UPDATE_TASK_FAILED`

A failed attempt to update a posting.

`POSTING_MEDIA_REACTION_ADDED_POSITIVE`

A positive reaction was added to a media attached to a posting.

`POSTING_MEDIA_REACTION_ADDED_NEGATIVE`

A negative reaction was added to a media attached to a posting.

`COMMENT_MEDIA_REACTION_ADDED_POSITIVE`

A positive reaction was added to a media attached to a comment.

`COMMENT_MEDIA_REACTION_ADDED_NEGATIVE`

A positive reaction was added to a media attached to a comment.

`POSTING_MEDIA_REACTION_FAILED`

A failed attempt to add a reaction to a media attached to a posting.

`COMMENT_MEDIA_REACTION_FAILED`

A failed attempt to add a reaction to a media attached to a comment.

`POSTING_SUBSCRIBE_TASK_FAILED`

A failed attempt to subscribe to a posting.

`POSTING_REACTION_TASK_FAILED`

A failed attempt to post a reaction to a posting.

`COMMENT_REACTION_TASK_FAILED`

A failed attempt to post a reaction to a comment.
