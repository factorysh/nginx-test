#!/usr/bin/env python3

import crossplane


class NginxException(Exception):
    errors = []


def errors(errors):
    n = NginxException()
    n.errors = errors
    raise n


class Nginx():

    def __init__(self, path):
        self.parse = crossplane.parse(path)
        if self.parse['status'] == 'failed':
            errors([cfg['errors'] for cfg in self.parse['config']])

    def configs(self):
        for config in self.parse['config']:
            yield config


if __name__ == '__main__':
    import sys
    n = Nginx(sys.argv[1])
    for config in n.configs():
        print(config)
