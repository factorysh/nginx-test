from . import find


nginx = None


def test_http3():
    if nginx:
        for server in nginx.servers():
            listen = find(server, 'listen')
            assert 'http2' in listen['args']
