#!/bin/bash

python3.8 setup.py sdist bdist_wheel

PKG_VERSION=$(python3.8 setup.py --version)
PKG_NAME=$(python3.8 setup.py --name)
DIST_NAME="${PKG_NAME}-${PKG_VERSION}"

python3.8 -m twine check --strict

if [ "live" == "$1" ]; then
  PYPI_REPOSITORY=pypi
else
  PYPI_REPOSITORY=testpypi
fi

python3.8 -m twine upload \
  --repository "$PYPI_REPOSITORY" \
  --username "$SMS77IO_PYPI_USERNAME" \
  --password "$SMS77IO_PYPI_PASSWORD" \
  "dist/$DIST_NAME.*"
