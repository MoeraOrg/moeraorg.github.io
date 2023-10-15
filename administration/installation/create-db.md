---
layout: administration
title: Installation
up: installation
subtitle: PostgreSQL Database
---

# PostgreSQL Database

To create a database in PostgreSQL and make it accessible:

1. Install PostgreSQL server and client. In all major Linux
   distributions you can install them from the main package repository
   (note that you need `postgresql-contrib` package also). Make sure it
   is up and running.
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
   postgres=# CREATE DATABASE <dbname> OWNER <username> ENCODING 'utf8';
   ```

6. Connect to the database:

   ```
   postgres=# \c <dbname>
   ```

7. Activate `uuid-ossp` extension:

   ```
   <dbname>=# CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
   ```

8. Type `\q` to quit.
9. Press `^D` to exit the `postgres` user shell.
10. Under superuser, edit `/var/lib/pgsql/data/pg_hba.conf`
    (`/etc/postgresql/*/main/pg_hba.conf` in Debian) and add the
    following lines to it:

    ```
    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    local   <dbname>        <username>                              password
    host    <dbname>        <username>      127.0.0.1/32            password
    host    <dbname>        <username>      ::1/128                 password
    ```

11. Restart PostgreSQL server:
    ```
    $ sudo systemctl restart postgresql
    ```

There is no need to create any tables in the database. `moera-node` creates them
automatically on the first start and upgrades the structure when a new version is
run.
