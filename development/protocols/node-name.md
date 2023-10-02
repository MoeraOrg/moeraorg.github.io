---
layout: development
title: Protocols
up: protocols
subtitle: Node Name
---

# Node Name

Node name is registered at the [naming service][1]. Currently, Moera
supports only *registered names* (you may [read about them][1] in the
Architecture Overview section), but there are many other [name types][2] possible.
Every name type has a unique syntax that distinguishes it from others.

<table class="table">
    <thead>
        <tr>
            <th>Type</th>
            <th>Syntax</th>
         </tr>
    </thead>
    <tbody class="table-group-divider">
        <tr>
            <td>Registered name</td>
            <td>
                <code>&lt;name&gt;_&lt;generation&gt;</code>
            </td>
        </tr>
    </tbody>
</table>

[1]: http://moera.org/overview/naming.html
[2]: http://moera.org/overview/cheaper-names.html
