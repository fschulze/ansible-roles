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


.. _avahi: http://avahi.org
.. _nss_mdns: http://0pointer.de/lennart/projects/nss-mdns/
