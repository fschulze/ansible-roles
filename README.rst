Avahi
=====

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


Samba3
======

This sets up `samba`_.

See ``roles/samba3/defaults/main.yml`` for the default settings.
You can change those in your host_vars, but you have to copy the existing ones.

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
.. _samba: http://www.samba.org
