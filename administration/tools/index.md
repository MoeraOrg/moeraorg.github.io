---
layout: administration
title: Tools
---

# Tools

`moera-tools` ([GitHub][1]) package contains Python command-line utilities helping
to perform many administrative tasks for Moera nodes.

The easiest way to install it is from [PyPI repository][2]:

```
python3 -m pip install moera-tools
```

The package includes:
* [moname][3] — query, register, and update names on the Moera naming service.
* [moctl][4] — administer Moera nodes.

The `moctl` command can read defaults such as provider, node address, tokens,
and secrets from a common [configuration file][5].

[1]: https://github.com/MoeraOrg/moera-tools
[2]: https://pypi.org/project/moera-tools/
[3]: moname.html
[4]: moctl.html
[5]: config.html
