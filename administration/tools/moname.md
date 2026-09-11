---
layout: administration
title: Tools
up: tools
subtitle: moname
---

# moname

## Name

`moname` — query and manage names on the Moera naming server

## Synopsis

```
moname [--dev | --server SERVER] [--created] [--keys | --all-keys] [--similar] [--at AT] <name>
moname --list [--dev | --server SERVER] [--created] [--at AT] [--newer NEWER] [--ignore-case] [<name>]
moname --add [--dev | --server SERVER] <name> <uri>
moname --update [--dev | --server SERVER] [--uri URI] [--signing-key] [--updating-key] <name>
moname --help
moname --version
```

## Node Names

The names are given in the form `<name>_<generation>` (for example `lamed_0`),
where `<name>` is the name itself and `<generation>` is the number that
differentiate between usages of the same name — for example, different social
networks. If the generation is missing, generation `0` is used by default.

## Options

`-h, --help`

: Get the list of all available options, their meaning and their short and long
  forms.

`-V, --version`

: Show the program's version number and exit.

### Query a name

`<name>`

: Check a name and get a corresponding node URL.
  ```
  $ moname lamed
  lamed_0	https://lamed.moera.blog/moera
  ```

`-c, --created`

: See the creation date/time of the name.
  ```
  $ moname -c lamed
  2019-12-17 02:13:26 lamed_0	https://lamed.moera.blog/moera
  ```

`-d, --dev`
`-s SERVER, --server SERVER`

: Use the development naming server or any other naming server.
  ```
  $ moname -d balu-dev
  ...
  $ moname -s http://localhost.localdomain:8081/moera-naming balu-dev
  ...
  ```

`-S, --similar`

: Try to find a similar name if the provided one is not found.
  ```
  $ moname -S Lamed
  lamed_0	https://lamed.moera.blog/moera
  ```

`-k, --keys`

: See the detailed information about the name, including the keys.

  ```
  $ moname -k moera-blog
  name         : moera-blog
  generation   : 0
  node URI     : https://blog.moera.org/moera
  digest       : b42b9ba69e7e58bba1c2606bafb86eaac8683c6bc3784a3bf20e59c9f8ce2a0e
  updating key : 1894f11410389a0dc0d37a5b3f8f9b993e5e8da61f38d818cce4f662d1d5ad4728441134dfb660a28155520bf79beae07e95763e52ce9c5d3597e793c8f89737
  created      : 2019-09-22 02:49:15
  signing key  : 3d6dd81295985291c4727fdbcbacba3349f18876578d633dbff1956364269cab5f3fe4da30f60896d2327ca60df64d54adb154ca34320d2c0ece96f0ccc2bf9c
  valid from   : 2020-08-28 03:22:09
  ```

`-t AT, --at AT`

: See the information valid at some moment in the past.

  ```
  $ moname -k -t '2019-10-09' moera-blog
  name         : moera-blog
  generation   : 0
  node URI     : https://blog.moera.org/moera
  digest       : b42b9ba69e7e58bba1c2606bafb86eaac8683c6bc3784a3bf20e59c9f8ce2a0e
  updating key : 1894f11410389a0dc0d37a5b3f8f9b993e5e8da61f38d818cce4f662d1d5ad4728441134dfb660a28155520bf79beae07e95763e52ce9c5d3597e793c8f89737
  created      : 2019-09-22 02:49:15
  signing key  : d2b7f5a2c7578c1ed6a9048f5f9efdd98e7d1955769a926d26bf3210668992a3ff34092755e8b0d8f3da8fc22246d32187b6656e87f675c3fe894258c9248c8e
  valid from   : 2019-09-22 03:48:18
  ```

`-K, --all-keys`

: See the whole history of the keys.

  ```
  $ moname -K moera-blog
  name         : moera-blog
  generation   : 0
  node URI     : https://blog.moera.org/moera
  digest       : b42b9ba69e7e58bba1c2606bafb86eaac8683c6bc3784a3bf20e59c9f8ce2a0e
  updating key : 1894f11410389a0dc0d37a5b3f8f9b993e5e8da61f38d818cce4f662d1d5ad4728441134dfb660a28155520bf79beae07e95763e52ce9c5d3597e793c8f89737
  created      : 2019-09-22 02:49:15
  
  signing key  : 3d6dd81295985291c4727fdbcbacba3349f18876578d633dbff1956364269cab5f3fe4da30f60896d2327ca60df64d54adb154ca34320d2c0ece96f0ccc2bf9c
  valid from   : 2020-08-28 03:22:09
  
  signing key  : d2b7f5a2c7578c1ed6a9048f5f9efdd98e7d1955769a926d26bf3210668992a3ff34092755e8b0d8f3da8fc22246d32187b6656e87f675c3fe894258c9248c8e
  valid from   : 2019-09-22 03:48:18
  ```

### List names

`-l, --list`

: Get a list of all names registered on the server (it may be huge!).

  ```
  $ moname -l|head
  4ap-4aps_0	https://4ap-4aps.moera.blog/moera
  abrasha_0	https://abrasha.moera.blog/moera
  abu-chucha_0	https://abu-chucha.moera.blog/moera
  achernitsky_0	https://achernitsky.moera.blog/moera
  a-dev_0	http://a-dev.localhost.localdomain:8082/moera
  Aelita_0	https://aelita.moera.blog/moera
  Agropoliv_0	https://agropoliv.moera.blog/moera
  Akeon_0	https://akeon.moera.blog/moera
  akog_0	https://akog.moera.blog/moera
  akovalenko_0	https://akovalenko.moera.blog/moera
  ```

`<name>`

: Show only entries whose names start with the given prefix. If a generation
  suffix is omitted, entries from every generation are included. If the suffix
  is present, only that generation is included. For example, `al` matches
  `alice_0`, `alice_2`, `alex_0`, and `alla_5`, while `al_0` matches only
  `alice_0` and `alex_0`.

: Filtering is performed by the client. `moname` still downloads every page of
  the complete, potentially huge list from the naming server and filters only
  what it prints. Supplying `<name>` therefore does not reduce network traffic or
  the time needed to retrieve the list.

`-i, --ignore-case`

: Ignore letter case when comparing the `<name>` prefix. Without this option,
  prefix matching is case-sensitive.

`-c, --created`

: Prepend the creation date/time to every name in the list when it is available.

`-t AT, --at AT`

: Get the list as it was at some moment in the past.

  ```
  $ moname -l -t '2019-12-01'
  alice-dev_0	http://alice.localhost.localdomain:8082/moera
  balu-dev_0	http://balu.localhost.localdomain:8082/moera
  moera-blog_0	https://blog.moera.org/moera
  ```

`-w NEWER, --newer NEWER`

: Get the list of names registered recently.

: If `--newer` and `--at` are both specified, `--newer` takes precedence and
  `--at` has no effect.

  ```
  $ moname -l -w '2023-08-04'
  achernitsky_0	https://achernitsky.moera.blog/moera
  Amitaykrichevsky_0	https://amitaykrichevsky.moera.blog/moera
  IrinaVulf_0	https://irinavulf.moera.blog/moera
  mendel_0	https://mendel.moera.blog/moera
  thickstone_0	https://thickstone.moera.blog/moera
  Леямеламуд_0	https://leyamelamud.moera.blog/moera
  Олексій_0	https://alexeyvk.moera.blog/moera
  ```

### Add a name

`-a, --add <name> <uri>`

: Add a new name to the naming server and set its node URI to `<uri>`.
The updating and signing keys are generated automatically. Save both outputs:
the 24 secret words are required for future updates, and the raw private signing
key is needed by the node that will use the name. Keep the private signing key
secret. The corresponding public signing key becomes valid approximately ten
minutes after the request is made.

  ```
  $ moname -da moname-sample https://moname.moera.social/moera
  Request sent, waiting for the operation to complete...
  Secret words:
   1. sauce
   2. ordinary
   3. force
   4. mix
   5. meadow
   6. hockey
   7. cook
   8. maple
   9. swear
  10. dinner
  11. hint
  12. settle
  13. wheat
  14. fabric
  15. sleep
  16. memory
  17. radio
  18. collect
  19. much
  20. eager
  21. adult
  22. bleak
  23. cash
  24. innocent

  Signing key: af0eee5798fabc78332d945ab0b001ad60409c1343ed34edf927d1b0d1cdb498
  ```

: Status messages and the `Secret words:` and `Signing key:` labels are printed
  only when standard output is a terminal. When output is redirected, the
  numbered mnemonic and the raw private signing key are printed without those
  labels.

### Update a name

`-u, --update <name>`

: Update the given name on the naming server. Without any other options, this
command does not change anything (can be used to verify the secret words). The
secret words should be passed to the standard input. It is allowed to pass them
exactly how they are printed, with each word prepended with its number. These
numbers are ignored.

: The command always reads the current 24 secret words from standard input,
  even if you only change the URI or rotate keys.

: The `Enter 24 secret words:` prompt is printed only when standard input is a
  terminal. The operation status and the `Secret words:` and `Signing key:`
  labels are printed only when standard output is a terminal. When output is
  redirected, a newly generated mnemonic remains numbered, while a generated
  raw private signing key is printed without a label.

`-U, --uri URI`

: Set a new node URI.

`-g, --signing-key`

: Generate a new signing key and print its raw private value after the update
  completes. Keep this value secret. The corresponding public signing key
  becomes valid approximately ten minutes after the request is made.

`-G, --updating-key`

: Generate a new updating key and print the new 24 secret words after the
  update completes.

: `-g` and `-G` may be used together. In that case the command prints both the
  new secret words and the new signing key.
