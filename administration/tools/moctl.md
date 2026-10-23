---
layout: administration
title: Tools
up: tools
subtitle: moctl
---

# moctl

## Name

`moctl` — administer Moera nodes

## Synopsis

```
moctl [-h] [-d] [-H URL | -N NAME] [-k]
      [-s URL] [-S SECRET]
      [-P PROVIDER] [-T TOKEN]
      [-V] OBJECT COMMAND ...
```

## Options

`-h, --help`

: Get the list of all available options, their meaning, and their short and long
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

`-k, --insecure`

: Disable SSL certificate verification for HTTPS connections to the naming server
  and the node.

: Use this option only when connecting to a trusted server with a self-signed or
  otherwise untrusted certificate.

`-S SECRET, --root-secret SECRET`

: Define root admin secret used for authentication.

`-T TOKEN, --token TOKEN`

: Define the admin token used for authentication.

`-P PROVIDER, --provider PROVIDER`

: Use the named profile defined in the [configuration file][1]. It is recommended
  to use the configuration file to store tokens and secrets instead of passing
  them through the command line. Command-line options override the defaults set
  in the configuration file.

: If the profile is not set explicitly, the program uses the node address passed
  in `-H`/`-N` options to find the first profile that has `domain=` defined and
  the node is located on one of its subdomains. For example, if the node is
  `lamed.moera.blog`, the profile having `domain = moera.blog` fits the criteria.

: If no profile is found by domain name, the first non-default profile in the
  configuration file is used.

`OBJECT`

: The object to be managed. Each object has a set of `COMMAND`s defined for it.
  Use `-h` to get the list of commands for a particular object (`moctl domain -h`)
  and the list of command-specific options for a particular command
  (`moctl domain create -h`).

: The available objects are (short names are shown in parentheses):
  
  * `domain (dom)` — manage domains (nodes located on the same server)
  * `credentials (cr)` — manage credentials
  * `profile (pr)` — manage profile
  * `avatar (av)` — manage avatars
  * `name (nm)` — manage node name
  * `malware (mal)` — manage malware hashes
  * `token (t)` — manage authentication tokens
  * `grant (gr)` — manage administrative grants
  * `option (op)` — change settings

: The commands are described in the following sections.

Most commands that modify node state require authentication. Depending on the
operation, use either a root admin secret (`-S`) or an admin token (`-T`).
`token create` is the main exception: it authenticates with the current admin
password passed as a positional argument.

## Manage domains

These commands manage domains — nodes located on the same server. Usually they have
domain names that are subdomains of the same domain, but this is not required.

`domain list`

: List all domains (nodes) defined on the server.

`domain show`

: Show the detailed information about the domain. (The domain is defined by
`-H`/`-N` options.)

`domain available NAME`

: Find and display an available domain name recommended by the server for the
  given node name.

`domain create DOMAIN`

: Create a domain with the given domain name.

`domain delete DOMAIN`

: Delete a domain with the given domain name.

## Manage credentials

These commands manage credentials used to authenticate the owner (admin) of
the node.

`credentials check`

: Check and display whether admin credentials are set for the node.

`credentials disable-login`

: Disable creation of authentication tokens and changing or resetting credentials.
  To enable login again, delete credentials and set a new password.

`credentials set-password PASSWORD`

: Set the admin password for the node. If the node has an admin password defined,
  this operation fails.

`credentials delete-password`

: Alias: `credentials del-password`.

: Delete the admin password of the node. Without a password, the node can be taken
  over by anybody, so a new password should be set as soon as possible.

`credentials get-email`

: Display node owner's e-mail address, if set.

`credentials set-email ADDRESS`

: Set node owner's e-mail address.

## Manage profile

These commands manage the node profile.

`profile get-full-name`

: Display node owner's full name, if set.

`profile set-full-name FULL_NAME`

: Set node owner's full name. Enclose `FULL_NAME` in quotes if it contains spaces.

`profile get-bio`

: Display the source text of node owner's bio, if set.

`profile set-bio BIO`

: Set node owner's bio using Markdown. Enclose `BIO` in quotes if it contains
  spaces or line breaks. Pass an empty string (`""`) to clear the bio.

`profile get-avatar`

: Display the ID of the current profile avatar. Print nothing if no avatar is set.

`profile set-avatar ID`

: Set the profile avatar to the avatar with the given `ID`. Use `avatar list` to
  find available avatar IDs.

## Manage avatars

These commands manage the node owner's avatars. `av` is an alias for `avatar` in
all commands. Creation and deletion require an admin token (`-T`) or a root admin
secret (`-S`).

`avatar list`

: List avatars, one per line. Each line contains the avatar ID, dimensions in
  `WIDTHxHEIGHT` format, and shape, separated by tabs.

`avatar get [-o FILE] ID`

: Download the image of the avatar with the given `ID`. By default, write the
  image bytes to standard output.

: `-o FILE, --output FILE`

  : Write the image to `FILE`. Use `-` for standard output.

`avatar create [-i FILE] [--size PIXELS] [--shape SHAPE]`

: Create an avatar from an image and print the new avatar ID. By default, read
  the image from standard input. The MIME type is detected automatically from
  the image contents.

: The image is cropped to a centered square, taking EXIF orientation into
  account. Both input dimensions must be at least 100 pixels. Use
  `profile set-avatar ID` to select the new avatar for the profile.

: `-i FILE, --input FILE`

  : Read the image from `FILE`. Use `-` for standard input.

: `--size PIXELS`

  : Set the avatar size in pixels. The minimum and default value is `200`.

: `--shape SHAPE`

  : Set the avatar shape, for example `circle` or `square`. The default is
    `circle`.

`avatar delete ID`

: Delete the avatar with the given `ID`. Print nothing on success.

## Manage node name

These commands manage the node name stored on the node. The commands do not make any
changes on the naming server — the node itself updates the naming server when
needed.

`name show`

: Show the node name.

`name status`

: Display the status of the last operation on the name.

`name show-words`

: Display the secret words stored on the node, one per line, with each word
  prepended with its number.

`name delete-words`

: Delete the secret words stored on the node.

`name register [-w] NAME`

: Alias: `name reg [-w] NAME`.

: Register a new name `NAME` and assign it to the node. The command outputs the 24
  secret words that are needed to control the name.

: `-w, --store-words`

  : Store the secret words on the node instead of displaying them. If the words
    cannot be stored, the command displays them before reporting the error.

`name assign NAME`

: Assign an existing name `NAME` to the node. The 24 secret words are to be passed
to the standard input, one per line. It is allowed to pass them exactly as they
are printed by `name register`, where each word is prepended with its number.
These numbers are ignored.

`name delete`

: Remove name information from the node. 

## Manage malware hashes

These commands manage the `malware` user list on the node. Each hash is stored
in the list as `node_name`.

`malware add HASH`

: Add `HASH` to the malware list.

`malware delete HASH`

: Delete `HASH` from the malware list.

`malware show HASH`

: Show `HASH` and its creation timestamp, separated by a tab. If `HASH` is not
  found, print nothing.

## Manage authentication tokens

These commands manage tokens that are used to authenticate as administrator on
the node. The token ID is used to identify the particular token in later
commands.

`token list`

: List all tokens available on the node. Each line contains the token ID and
  either the token name or, for unnamed tokens, the token value itself. If the
  token belongs to a plugin, the plugin name is shown in a third column.

`token show ID`

: Show the detailed information about the token with the given `ID`, including
  the token value, permissions, timestamps, and last-use information when
  available.

`token create [-n NAME] [-p PERMISSIONS] PASSWORD`

: Create a new token using the current admin `PASSWORD`. This command
  authenticates with the password directly and does not require `-T` or `-S`.

: `-n NAME, --token-name NAME`

  : The name to be assigned to the token. If not set, the token becomes unnamed.

: `-p PERMISSIONS, --permissions PERMISSIONS`

  : Comma-separated list of permissions to be assigned to the token.

`token update [-n NAME] [-p PERMISSIONS] ID`

: Change the token's name or permissions and print the updated token details.

: `-n NAME, --token-name NAME`

  : Assign a human-readable name to the token.

: `-p PERMISSIONS, --permissions PERMISSIONS`

  : Comma-separated list of permissions to be assigned to the token.

`token delete ID`

: Delete the token.

## Manage administrative grants

These commands manage administrative permissions granted by this node to other
nodes. All grant commands require admin authentication. A node name passed to
`show`, `grant`, or `revoke` is expanded to its full form with a generation
suffix before it is sent to the node API; for example, `alice` becomes
`alice_0`.

`grant list`

: List all grants issued by the node. Each line contains the full node name,
  followed by a tab and a comma-separated list of permissions.

`grant show NAME`

: Show the grant issued to `NAME`, using the same format as `grant list`. If no
  grant exists, print nothing.

`grant grant NAME SCOPES`

: Grant the comma-separated `SCOPES` to `NAME`. Spaces around permission names
  are ignored, but the whole list must be passed as one command-line argument.
  For example:

  ```
  moctl -N mynode grant grant alice view-content,react
  moctl -N mynode grant grant alice 'view-content, react'
  ```

: A space-separated list without commas, such as `'view-content react'`, is
  invalid. An unquoted space after a comma creates an extra command-line
  argument and is also invalid.

`grant revoke NAME SCOPES`

: Revoke the comma-separated `SCOPES` from `NAME`. The list follows the same
  syntax as in `grant grant`.

: Use `all` to revoke all administrative permissions issued to the node:

  ```
  moctl -N mynode grant revoke alice all
  ```

## Change settings

These commands are used to display or change node settings (options). The node admin
may change regular settings, while changing privileged settings or default values
requires root admin authentication.

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
