import sys
import click
from . import server_names as sn
from . import Nginx, NginxException


@click.group()
def cli():
    pass


@cli.command()
@click.option('--regex/--no-regex', default=False)
def server_names(regex=False):
    try:
        n = Nginx()
    except NginxException as ne:
        print(ne)
        sys.exit(-1)
    names = set()
    for server in n.servers():
        for name in sn(server):
            if not regex and name.startswith('~'):
                continue
            names.add(name)
    names = list(names)
    names.sort()
    print("\n".join(names))
