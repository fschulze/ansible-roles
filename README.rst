.. contents:: Table of Contents

bsd_avahi
=========

This sets up `avahi`_ and `nss_mdns`_.

Publish Bonjour services
------------------------

To publish a Bonjour service, use something like this::

  tasks:
    - { include: ../ansible-roles/roles/avahi/tasks/avahi_service.yml,
        avahi_service_name: smb,
        avahi_services_info: [
            {
                type: _smb._tcp,
                port: 445 },
            {
                type: _device-info._tcp,
                port: 0,
                txt-record: model=Xserve }]}


bsd_periodic_with_anacron
=========================

This sets everything up, so periodic tasks are run by anacron.
This is useful for systems that don't run 24/7.


bsd_postgresql
==============

This sets up `postgresql`_.
The id of the user and group for postgresql must be unique on the whole jail host.
This is because postgresql uses shared memory.
If you don't do this, you will get errors in the form of::

  semctl(10223622, 3, SETVAL, 0) failed: Invalid argument

To use this role, do something like this in your roles list::

  - { role: postgresql,
      pgsql_user_group_id: 300}

If you install the server and the client in the same jail and want to use the python client, you have to set the version for the packages.
At the time of this writing it works with postgresql90 like this::

  - { role: postgresql,
      pgsql_user_group_id: 300,
      postgresql_package_prefix: postgresql90}

ZFS setup
---------

If you use postgresql on ZFS, then you should setup a separate filesystem for it like this::

  - name: postgresql data ZFS file system
    zfs:
      name: tank/data/production/demo/postgresql
      state: present
      recordsize: 8K
      primarycache: metadata

The ``recordsize`` of 8K is the blocksize that postgresql uses.
Setting it ensures consistency of the data on disk.
The ZFS default of 128K could cause a too long delay before data is written to disk and if interrupted might lead to inconsistencies unexpected to postgresql.

Since postgresql implements it's own caching, we only cache metadata.


bsd_samba3
==========

This sets up `samba`_.

See ``roles/samba3/defaults/main.yml`` for the default settings.
You can change those in your host_vars, but you have to copy the existing ones.

Users
-----

By default samba is configured to use unix users, but with it's own password db.
So you first have to add a unix user and then use ``pdbedit -a -u [username]`` to set the password.

Declaring shares
----------------

In your host_vars use something like this::

  samba3_shares:
      mnt:
          path: "/mnt"
          unix extensions: "no"
          read only: "yes"
          valid users: "fschulze"


.. _avahi: http://avahi.org
.. _nss_mdns: http://0pointer.de/lennart/projects/nss-mdns/
.. _postgresql: http://www.postgresql.org
.. _samba: http://www.samba.org


bsd_ssh_nodns
=============

Turns off DNS lookup of connecting ssh client.
