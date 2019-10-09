# coding: utf-8

"""
    PirlPay API

    The PirlPay API for automated payment processing

    OpenAPI spec version: v1
    Contact: support@pirl.io
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "pirlpay"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="PirlPay API",
    author_email="support@pirl.io",
    url="",
    keywords=["PirlPay API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The PirlPay API for automated payment processing for https://pirlpay.com \n
    - API version: v1 \n
    - Package version: 0.0.1\n

    ## Requirements.\n

    Python 2.7 and 3.4+\n

    ## Installation & Usage\n
    pip install pirlpay \n

    """
)
