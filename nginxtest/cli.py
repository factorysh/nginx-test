import sys
from . import server_names, Nginx


def main():
    if sys.argv[1] == "server_name":
        print("\n".join(show_server_names()))


def show_server_names():
    n = Nginx()
    names = set()
    for server in n.servers():
        for name in server_names(server):
            names.add(name)

    names = list(names)
    names.sort()
    return names
