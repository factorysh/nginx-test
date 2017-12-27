from . import find


def test_ssl_everywhere(nginx):
    """
    For each server listening port 80,
    one server listening port 443, with the same server_name is mandatory
    """
    http = set()
    https = set()
    for server in nginx.servers():
        sn = find(server, 'server_name').__next__()['args']
        if sn == ['_']:  # catch all server
            continue
        listen = find(server, 'listen').__next__()
        if '443' in listen['args']:
            for s in sn:
                https.add(s)
        if '80' in listen['args']:
            for s in sn:
                http.add(s)
    http_only = http - https
    assert len(http_only) == 0, "No SSL for domain : %s" \
        % ", ".join(http_only)


def test_http2(nginx):
    """
    When listening 443, handle http2 too
    """
    for server in nginx.servers():
        listen = find(server, 'listen').__next__()
        if '443' in listen['args']:
            assert 'http2' in listen['args']


def test_hsts(nginx):
    """
    HSTS header in mandatory on port 443
    """
    for server in nginx.servers():
        listen = find(server, 'listen').__next__()
        if '443' not in listen['args']:
            continue
        hsts = False
        for header in find(server, 'add_header'):
            if 'Strict-Transport-Security' in header['args']:
                hsts = True
        assert hsts, "Strict-Transport-Security header is required"
