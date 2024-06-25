---
layout: administration
title: Tools
up: tools
subtitle: moctl
---

# moctl

## Name

`moctl` — manage domains, credentials, and settings

## Synopsis

```
moctl [-h] [-d] [-H URL | -N NAME]
      [-s URL] [-S SECRET]
      [-P PROVIDER] [-T TOKEN]
      [-V] OBJECT COMMAND ...
```

## Options

`-h, --help`

: Get the list of all available options, their meaning and their short and long
forms.

`-V, --version`

: Show the program's version number and exit.

`-d, --dev`

: Use the development naming server to resolve node names.

`-s URL, --naming-server URL`

: Use the provided naming server to resolve node names.

`-H URL, --host URL`
`-N NAME, --name NAME`

: Manage the node designated by the given `URL` or `NAME`. These options are
  mutually exclusive.

  These options define the node to be managed by all commands, except domain
  creation/deletion commands. For domain creation/deletion commands, these options
  define the node for sending API requests to.

`-S SECRET, --root-secret SECRET`

: Define root admin secret used for authentication.

`-T TOKEN, --token TOKEN`

: Define admin token used for authentication.

`-P PROVIDER, --provider PROVIDER`

: Use the provider defined in the [configuration file][1]. It is recommended to use
  the configuration file to store tokens and secrets instead of passing them through
  the command line. Command-line options override the defaults set in
  the configuration file.

: If the provider is not set explicitly, the program uses the node address passed in
  `-H`/`-N` options to find the first provider that has `domain=` defined and
  the node is located on one of its subdomains. For example, if the node is
  `lamed.moera.blog`, the provider having `domain = moera.blog` fits the criteria.

: If no provider is found by domain name, the first provider in the configuration
  file is used.

`OBJECT`

: The object to be managed. Each object has a set of `COMMAND`s defined for it.
  Use `-h` to get the list of commands for a particular object (`moctl domain -h`)
  and the list of command-specific options for a particular command
  (`moctl domain create -h`).

: The available objects are (you can use a full or short name):
  
  * `domain (dom)` — manage domains (nodes located on the same server)
  * `credentials (cr)` — manage credentials
  * `name (nm)` — manage node name
  * `token (t)` — manage authentication tokens
  * `option (op)` — change settings

: The commands are described in the following sections.

## Manage domains

These commands manage domains — nodes located on the same server. Usually they have
domain names that are subdomains of the same domain, but this is not required.

`domain list`

: List all domains (nodes) defined on the server.

`domain show`

: Show the detailed information about the domain. (The domain is defined by
`-H`/`-N` options.)

`domain create DOMAIN`

: Create a domain with the given domain name.

`domain delete DOMAIN`

: Delete a domain with the given domain name.

## Manage credentials

These commands manage credentials used to authenticate the owner (admin) of
the node.

`credentials check`

: Check and display whether admin credentials are set for the node.

`credentials set-password PASSWORD`

: Set the admin password for the node. If the node has an admin password defined,
  this operation fails.

`credentials delete-password`

: Delete the admin password of the node. Without a password, the node can be taken
  over by anybody, so a new password should be set as soon as possible.

`credentials get-email`

: Display node owner's e-mail address, if set.

`credentials set-email ADDRESS`

: Set node owner's e-mail address.

## Manage node name

These commands manage the node name stored on the node. The commands do not make any
changes on the naming server — the node itself updates the naming server when
needed.

`name show`

: Show the node name.

`name status`

: Display the status of the last operation on the name.

`name register NAME`

: Register a new name `NAME` and assign it to the node. The command outputs the 24
secret words that are needed to control the name.

`name assign NAME`

: Assign an existing name `NAME` to the node. The 24 secret words are to be passed
to the standard input, one per line. It is allowed to pass them exactly how they
are printed by `name register`, where each word is prepended with its number.
These numbers are ignored.

`name delete`

: Remove name information from the node. 

## Manage authentication tokens

These commands manage tokens that are used to authenticate as administrator on
the node. The token itself is displayed only once — when created. All further
operations on the token use token ID to identify the particular token.

`token list`

: List all tokens available on the node.

`token show ID`

: Show the detailed information about the token with the given `ID`.

`token create [-n NAME] PASSWORD`

: Create a new token. This operation requires additional authentication with
  `PASSWORD`.

: `-n NAME, --token-name NAME`

  : Assign a human-readable name to the token.

`token rename [-n NAME] ID`

: Change the human-readable name of the token.

: `-n NAME, --token-name NAME`

  : The name to be assigned to the token. If not set, the token becomes unnamed.

`token delete [-h] ID`

: Delete the token.

## Change settings

These commands are used to display or change node settings (options). The node admin
may change regular settings, while changing privileged settings or default values
require root admin authentication.

`option show [-d] [--defaults] [-m] [--prefix PREFIX] [-t]`

: List all available settings. Letter `P` in the first column means that
  the setting is privileged (can be changed by the root admin only). `*` in
  the second column means that the setting was modified (i.e., holds a non-default
  value).

: `-d, --description`

  : Show descriptions of the settings' meaning.

: `--defaults`

  : Show the default values of the settings instead of the current values.

: `-m, --modified`

  : Show only the settings that were modified.

: `--prefix PREFIX`

  : Show only the settings having names starting with `PREFIX`.

: `-t, --type`

  : Show information about the settings' type. 

`option set NAME VALUE`

: Set the setting `NAME` to the given `VALUE`.

`option reset NAME`

: Reset the setting `NAME` to its default value.

`option set-default NAME VALUE`

: Set default value of the setting `NAME` to the given `VALUE`.

`option reset-default NAME`

: Reset default value of the setting `NAME` to its built-in value.

`option set-privileged NAME`

: Make the setting `NAME` privileged.

`option set-not-privileged NAME`

: Make the setting `NAME` not privileged.

`option reset-privileged NAME`

: Reset privileged status of the setting `NAME` to its built-in value.

[1]: config.html