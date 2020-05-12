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
a story is used for feeds containing postings.

`REACTION_ADDED_POSITIVE`

A positive reaction was added to a posting. `posting` field refers to
the posting.

`REACTION_ADDED_NEGATIVE`

A negative reaction was added to a posting. `posting` field refers to
the posting.

`MENTION_POSTING`

The user was mentioned in a posting on other node. `remoteNodeName` and
`remotePostingId` fields refer to the node and the posting on it,
respectively.
