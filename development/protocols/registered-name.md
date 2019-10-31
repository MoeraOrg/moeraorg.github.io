---
layout: development
title: Protocols
up: protocols
subtitle: Registered Name
body_class: body-pink
---

# Registered Name

*Registered name* is the name of the node that is registered at the
[naming service][1]. Currently Moera supports only *delegated names*
(you may [read about them][1] in the Overview section), but there are
many other [name types][2] possible. Every name type has a unique syntax
that distinguishes it from others.

<table class="table table-bordered">
    <thead>
        <tr>
            <th>Type</th>
            <th>Syntax</th>
         </tr>
    </thead>
    <tbody>
        <tr>
            <td>Delegated name</td>
            <td>
                <code>&lt;name&gt;_&lt;generation&gt;</code>
            </td>
        </tr>
    </tbody>
</table>

[1]: http://moera.org/overview/naming.html
[2]: http://moera.org/overview/cheaper-names.html
