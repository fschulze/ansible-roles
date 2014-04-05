from os.path import dirname, join


# register our own library and roles paths into ansible
ansible_paths = dict(
    roles=[join(dirname(__file__), 'roles')])
