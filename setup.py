from setuptools import setup
import os


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


setup(
    version='0.1',
    description="A collection of Ansible roles to setup FreeBSD jails using BSDploy",
    long_description=README,
    name="bsd_ansible_roles",
    author='Florian Schulze',
    author_email='florian.schulze@gmx.net',
    include_package_data=True,
    zip_safe=False,
    py_modules=['bsd_ansible_roles'],
    install_requires=[
        'bsdploy',
    ],
    entry_points="""
        [ansible_paths]
        bsd_ansible_roles = bsd_ansible_roles:ansible_paths
    """)
