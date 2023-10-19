---
layout: administration
title: Tools
up: tools
subtitle: moname
---

# moname

## Name

`moname` — get information about names from the Moera naming server

## Synopsis

```
moname [-h] [-c] [-d] [-k] [-K] [-l]
       [-s SERVER] [-S] [-t AT]
       [-w NEWER] [-V] [<name>]
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
  updating key : 1894f11410389a0dc0d37a5b3f8f9b993e5e8da61f38d818cce4f662d1d5ad47
  28441134dfb660a28155520bf79beae07e95763e52ce9c5d3597e793c8f89737
  created      : 2019-09-22 02:49:15
  signing key  : 3d6dd81295985291c4727fdbcbacba3349f18876578d633dbff1956364269cab
  5f3fe4da30f60896d2327ca60df64d54adb154ca34320d2c0ece96f0ccc2bf9c
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
  updating key : 1894f11410389a0dc0d37a5b3f8f9b993e5e8da61f38d818cce4f662d1d5ad47
  28441134dfb660a28155520bf79beae07e95763e52ce9c5d3597e793c8f89737
  created      : 2019-09-22 02:49:15
  signing key  : d2b7f5a2c7578c1ed6a9048f5f9efdd98e7d1955769a926d26bf3210668992a3
  ff34092755e8b0d8f3da8fc22246d32187b6656e87f675c3fe894258c9248c8e
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
  updating key : 1894f11410389a0dc0d37a5b3f8f9b993e5e8da61f38d818cce4f662d1d5ad47
  28441134dfb660a28155520bf79beae07e95763e52ce9c5d3597e793c8f89737
  created      : 2019-09-22 02:49:15
  
  signing key  : 3d6dd81295985291c4727fdbcbacba3349f18876578d633dbff1956364269cab
  5f3fe4da30f60896d2327ca60df64d54adb154ca34320d2c0ece96f0ccc2bf9c
  valid from   : 2020-08-28 03:22:09
  
  signing key  : d2b7f5a2c7578c1ed6a9048f5f9efdd98e7d1955769a926d26bf3210668992a3
  ff34092755e8b0d8f3da8fc22246d32187b6656e87f675c3fe894258c9248c8e
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
