---
layout: development
title: Protocols
up: protocols
subtitle: Moment
---

# Moment

Usually every post is assigned its place in a feed in accordance with
its timestamp. But it is absolutely possible that two posts will have
the same timestamp, so the position becomes ambiguous. To make the feed
working properly, we need to be able to fix the position and order of
posts and specify a position in the feed to within a particular post.

To achieve this goal, every post is assigned a *moment*, that is
calculated as follows:

```
moment = timestamp * 100 + seq
```

`seq` here is an arbitrary number from 0 to 99 that is chosen by the
node to make the resulting value unique.

Any moment that is larger than maximum safe integer in JavaScript
(2<sup>53</sup> - 1) is treated as "far future".

Similarly, any moment that is less than minimum safe integer in
JavaScript (- (2<sup>53</sup> - 1)) is treated as "far past".

Moments larger or equal to 9⋅10<sup>15</sup> are assigned to "pinned"
posts.
