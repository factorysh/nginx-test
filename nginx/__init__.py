#!/usr/bin/env python3

import crossplane


class NginxException(Exception):
    errors = []


def errors(errors):
    n = NginxException()
    n.errors = errors
    raise n


class Nginx():

    def __init__(self, path='/etc/nginx/nginx.conf'):
        self.parse = crossplane.parse(path)
        if self.parse['status'] == 'failed':
            errors([cfg['errors'] for cfg in self.parse['config']])

    def configs(self):
        for config in self.parse['config']:
            yield config

    def servers(self):
        for config in self.configs():
            for ps in config['parsed']:
                for p in ps:
                    for block in p.get('block', []):
                        if block.get('directive') == 'server':
                            yield block


if __name__ == '__main__':
    import sys
    n = Nginx(sys.argv[1])
    for config in n.configs():
        print(config)
