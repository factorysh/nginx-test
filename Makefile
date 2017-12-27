PYTHON_VERSION=$(shell python3 -V | grep  -o -e "3\.\d*")
SHELL=/bin/bash

venv/lib/python$(PYTHON_VERSION)/site-packages/crossplane: venv
	./venv/bin/pip install .

venv/lib/python$(PYTHON_VERSION)/site-packages/pex: venv
	./venv/bin/pip install pex

pex: wheel venv/lib/python$(PYTHON_VERSION)/site-packages/pex
	./venv/bin/pex --disable-cache --python-shebang="/usr/bin/env python3" -f wheelhouse --no-index -e nginxtest.cli:main -o nginx.pex crossplane nginxtest

venv:
	python3 -m venv venv
	./venv/bin/pip install wheel

wheelhouse:
	make wheel

wheel: venv
	./venv/bin/pip wheel -w wheelhouse .

clean:
	rm -rf venv *.pex pip-selfcheck.json *.whl wheelhouse
