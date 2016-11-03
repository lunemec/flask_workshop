import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "flask-workshop",
    version = "0.0.1",
    author = "Your Name",
    author_email = "your.name@somewhere.com",
    description = ("Flask workshop."),
    url = "https://github.com/nekdo/flask-workshop",
    packages=[],
    long_description=read('README.md'),
    setup_requires=['pytest-runner'],
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "flask-admin",
        "flask-restful",
        "flask-httpauth",
        "flask-migrate",
        "passlib",
        "python-json-logger",
    ],
    tests_require=['pytest'],
)
