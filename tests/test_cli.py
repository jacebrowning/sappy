# pylint: disable=missing-docstring,unused-variable,expression-not-assigned

import os
import sys
import subprocess
import time

import requests
from expecter import expect


def cli(*options):
    args = sys.executable, '-m', 'sappy', *options
    process = subprocess.Popen(args)
    time.sleep(0.5)
    return process


def describe_cli():

    def with_defaults(tmpdir):
        tmpdir.chdir()
        os.mkdir("dist")
        process = cli()

        try:
            response = requests.get("http://localhost:8080/foobar")
        finally:
            process.kill()

        expect(response.status_code) == 200

    def with_custom_directory(tmpdir):
        tmpdir.chdir()
        process = cli('.')

        try:
            response = requests.get("http://localhost:8080/foobar")
        finally:
            process.kill()

        expect(response.status_code) == 200
