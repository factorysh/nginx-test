from . import find


nginx = None


def test_http2():
    if nginx:
        for server in nginx.servers():
            listen = find(server, 'listen').__next__()
            print(listen)
            if '443' in listen['args']:
                assert 'http2' in listen['args']
