Nginx test
==========

Build a test file `test.py` :

```python
from pytest import fixture
from nginx import Nginx


@fixture
def nginx():
    return Nginx()

from nginx.test import test_http2, test_ssl_everywhere, test_hsts
```

Use pytest :

    py.test -v test.py


Licence
-------

3 terms BSD licence, © 2017, Mathieu Lecarme
