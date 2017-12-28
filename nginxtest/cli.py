import click
from . import server_names as sn
from . import Nginx


@click.group()
def cli():
    pass


@cli.command()
@click.option('--regex/--no-regex', default=False)
def server_names(regex=False):
    n = Nginx()
    names = set()
    for server in n.servers():
        for name in sn(server):
            if not regex and name.startswith('~'):
                continue
            names.add(name)
    names = list(names)
    names.sort()
    print("\n".join(names))
