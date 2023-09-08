---
layout: development
title: Protocols
up: protocols
subtitle: Stories
body_class: body-pink
---

# Stories
Stories describe something happening in Moera, they are building blocks
for feeds. All stories have [the same structure](node-api.html#StoryInfo)
but the meaning of fields depends on the story type. A story may
reference a posting, a remote object, etc. Some feeds may not allow some
types of stories.

`ASKED_TO_FRIEND`

A remote node asked to add it to friends.

`ASKED_TO_SUBSCRIBE`

A remote node asked to subscribe to it.

`BLOCKED_USER`

A remote node has blocked the user globally.

`BLOCKED_USER_IN_POSTING`

A remote node has blocked the user in a posting.

`COMMENT_ADDED`

A comment was added under the user's posting.

`COMMENT_MEDIA_REACTION_ADDED_NEGATIVE`

A positive reaction was added to a media attached to a comment.

`COMMENT_MEDIA_REACTION_ADDED_POSITIVE`

A positive reaction was added to a media attached to a comment.

`COMMENT_MEDIA_REACTION_FAILED`

A failed attempt to add a reaction to a media attached to a comment.

`COMMENT_POST_TASK_FAILED`

A failed attempt to post a comment.

`COMMENT_REACTION_ADDED_NEGATIVE`

A negative reaction was added to the user's comment.

`COMMENT_REACTION_ADDED_POSITIVE`

A positive reaction was added to the user's comment.

`COMMENT_REACTION_TASK_FAILED`

A failed attempt to post a reaction to a comment.

`COMMENT_UPDATE_TASK_FAILED`

A failed attempt to update a comment.

`FRIEND_ADDED`

A remote node has added the user to friends.

`FRIEND_DELETED`

A remote node has removed the user from friends.

`FRIEND_GROUP_DELETED`

A remote group of friends, the user was a member of, has been deleted.

`MENTION_COMMENT`

The user was mentioned in a comment.

`MENTION_POSTING`

The user was mentioned in a posting on another node.

`POSTING_ADDED`

A posting was added. **This type of story is used for feeds containing postings.**

`POSTING_MEDIA_REACTION_ADDED_NEGATIVE`

A negative reaction was added to a media attached to a posting.

`POSTING_MEDIA_REACTION_ADDED_POSITIVE`

A positive reaction was added to a media attached to a posting.

`POSTING_MEDIA_REACTION_FAILED`

A failed attempt to add a reaction to a media attached to a posting.

`POSTING_POST_TASK_FAILED`

A failed attempt to create a posting.

`POSTING_REACTION_TASK_FAILED`

A failed attempt to post a reaction to a posting.

`POSTING_SUBSCRIBE_TASK_FAILED`

A failed attempt to subscribe to a posting.

`POSTING_UPDATE_TASK_FAILED`

A failed attempt to update a posting.

`POSTING_UPDATED`

A posting was updated.

`REACTION_ADDED_NEGATIVE`

A negative reaction was added to the user's posting.

`REACTION_ADDED_POSITIVE`

A positive reaction was added to the user's posting.

`REMOTE_COMMENT_ADDED`

A comment was added under a posting the user is subscribed to.

`REPLY_COMMENT`

A reply was added to the user's comment.

`SHERIFF_COMPLAIN_ADDED`

A new complaint was received.

`SHERIFF_COMPLAIN_DECIDED`

A decision was made on the user's complaint.

`SHERIFF_MARKED`

User's entry was marked by a sheriff.

`SHERIFF_UNMARKED`

User's entry was unmarked by a sheriff.

`SUBSCRIBER_ADDED`

Another node subscribed to user's feed.

`SUBSCRIBER_DELETED`

Another node unsubscribed from user's feed.

`UNBLOCKED_USER`

A remote node has unblocked the user globally.

`UNBLOCKED_USER_IN_POSTING`

A remote node has unblocked the user in a posting.
