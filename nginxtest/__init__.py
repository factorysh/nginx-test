#!/usr/bin/env python3

import crossplane
from io import StringIO


class NginxException(Exception):
    errors = []

    def __str__(self):
        buff = StringIO()
        for error in self.errors:
            line = error.get('line')
            if line:
                buff.write("Line %s\n" % line)
            buff.write("\tError: %s\n" % error.get('error'))
        return buff.getvalue()


def errors(errors):
    n = NginxException()
    n.errors = errors
    raise n


def find(haystack, directive):
    for h in haystack:
        if h['directive'] == directive:
            yield h


def server_names(server):
    for sn in find(server, 'server_name'):
        for a in sn['args']:
            yield a


class Nginx():

    def __init__(self, path='/etc/nginx/nginx.conf'):
        self.parse = crossplane.parse(path)
        if self.parse['status'] == 'failed':
            err = NginxException()
            for cfg in self.parse['config']:
                for error in cfg['errors']:
                    err.errors.append(error)
            raise err

    def configs(self):
        for config in self.parse['config']:
            yield config

    def servers(self):
        for config in self.configs():
            for ps in config['parsed']:
                if ps.get('directive') == 'server':
                    yield ps['block']


if __name__ == '__main__':
    import sys
    n = Nginx(sys.argv[1])
    for config in n.configs():
        print(config)
