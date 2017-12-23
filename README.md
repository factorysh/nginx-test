Nginx test
==========

Build a test file `test.py` :

```python
from nginx import Nginx
import nginx.test

nginx.test.nginx = Nginx()

from nginx.test import test_http2, test_ssl_everywhere, test_hsts
```

Use pytest :

    py.test -v test.py


Licence
-------

3 terms BSD licence, © 2017, Mathieu Lecarme
