Civo

This project is the python API library for using in python projects.

Usage
-----
>>> from civo import Civo
>>> civo = Civo('token')
>>> ssh_file = open('~/.ssh/id_dsa.pub').read()

>>> # you can filter the result
>>> size_id = civo.size.search(filter='name:g2.xsmall')[0]['name']
>>> template = civo.templates.search(filter='code:debian-stretch')[0]['id']

>>> civo.ssh.create(name='default', public_key=ssh_file)
>>> civo.instances.create(hostname='text.example.com', size='g2.xsmall',
                      region='lon1', template_id=template,
                      public_ip='true', ssh_key='default')


Installation
------------
pip3 install civo

Requirements
^^^^^^^^^^^^
requests

Compatibility
-------------
python 3.7

Licence
-------
Mit License

Authors
-------

`civo` was written by `Alejandro JNM <alejandrojnm@gmail.com>`_.