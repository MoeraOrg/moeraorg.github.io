---
layout: administration
title: Installation
---

# Installation

The simplest way to install the Moera server software (`moera-node`) is to download
a prebuilt WAR file [from the GitHub repository][1] and place it in a directory on
your server.

After that, create a [PostgreSQL database][2] and a [configuration file][3]. These
steps are explained on separate pages.

The WAR file is self-executable, so you do not need to install Tomcat or a similar
Java servlet server to run it. Just give the file executable permissions:

```bash
$ chmod +x moera-node-0.14.0.war
```

And run it:

```bash
$ SPRING_APPLICATION_JSON={"spring.profiles.active":"prod"} ./moera-node-0.14.0.war
```

The value of `spring.profiles.active` setting (that is set above through
`SPRING_APPLICATION_JSON` environment variable) should correspond to the name of
your configuration file. If `spring.profiles.active` is set to `prod`,
the configuration file should be named `application-prod.yml`.

After `moera-node` starts, the Moera node will be available on the port you have
set in the configuration file.

## Adding to systemd

You need to write a script to start `moera-node` automatically as a daemon when
your server starts. If you have a systemd-based Linux distribution, the correct way
would be to create a unit file and add it to `systemd`.

For example, create the following `moera-node.service` file:

```
[Unit]
Description=Moera server
After=syslog.target

[Service]
User=moeranode
Group=moeranode
ProtectSystem=full
ProtectHome=true
WorkingDirectory=/srv/moera-node
Environment=LANG=en_US.UTF-8 \
            'SPRING_APPLICATION_JSON={"spring.profiles.active":"prod"}' \
            JAVA_OPTS="-Xmx2G -XX:+UseG1GC -XX:+UseStringDeduplication"
ExecStart=/srv/moera-node/moera-node-0.14.0.war
SuccessExitStatus=143
StandardOutput=syslog
StandardError=inherit
SyslogIdentifier=moera-node

[Install]
WantedBy=multi-user.target
```

`User=` and `Group=` define the user and the group that will be used by
the `moera-node` process. Do not forget to create the user and the group in your
system.

The WAR file is located in `/srv/moera-node` directory in the example above. If
the path on your server is different, put the correct path in `WorkingDirectory=`
and `ExecStart=`.

You can set any JRE options you want in `JAVA_OPTS` environment variable.
Explaining them is out of scope of this Guide.

To add the unit file to `systemd`, run

```bash
# systemctl enable ./moera-node.service
```

And then start the daemon:

```bash
# systemctl start moera-node
```

[1]: https://github.com/MoeraOrg/moera-node/releases
[2]: /administration/create-db.html
