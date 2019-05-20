---
layout: development
title: Development Environment
up: setup
subtitle: Creating PostgreSQL Database
body_class: body-pink
---

# Creating PostgreSQL Database

How to create a database in PostgreSQL and make it accessible for an
application:

1. Install PostgreSQL server and client. In all major Linux
   distributions you can install them from the main package repository.
2. Switch to `postgres` user:

   ```
   $ sudo su - postgres
   ```
3. Start `psql`:

   ```
   $ psql
   ```

4. Create a user `<username>` with password `<password>`:

   ```
   postgres=# CREATE USER <username> WITH PASSWORD '<password>';
   ```

5. Create a database `<dbname>`:

   ```
   postgres=# CREATE DATABASE <dbname> OWNER <username> COLLATE 'en_US.UTF-8';
   ```

6. Type `\q` to quit.
7. Press `^D` to exit the `postgres` user shell.
8. Under superuser, edit `/var/lib/pgsql/data/pg_hba.conf`
   (`/etc/postgresql/*/main/pg_hba.conf` in Debian) and add the
   following lines to it:

   ```
   # TYPE  DATABASE        USER            ADDRESS                 METHOD
   local   <dbname>        <username>                              password
   host    <dbname>        <username>      127.0.0.1/32            password
   host    <dbname>        <username>      ::1/128                 password
   ```
