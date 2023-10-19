---
layout: administration
title: Tools
---

# Tools

`moera-tools` ([GitHub][1]) package contains command-line utilities helping to perform many
administrative tasks for Moera nodes.

The tools are written in Python, and the easiest way to install them is from
[PyPI repository][2]:

```
pip install moera-tools
```

The package includes:
* [moname][3] — get information about names from the Moera naming service.
* [moctl][4] — manage domains, credentials, and settings.

All tools use a common [configuration file][5].

[1]: https://github.com/MoeraOrg/moera-tools
[2]: https://pypi.org/project/moera-tools/
[3]: moname.html
[4]: moctl.html
[5]: config.html
