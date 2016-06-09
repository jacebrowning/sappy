# pylint: disable=missing-docstring,unused-variable,expression-not-assigned

import os
import sys
import subprocess
import time

import requests
from expecter import expect


def describe_cli():

    def it_starts_a_server(tmpdir):
        tmpdir.chdir()
        os.mkdir("dist")
        process = subprocess.Popen([sys.executable, '-m', 'sappy'])
        time.sleep(0.25)

        try:
            response = requests.get("http://localhost:8080/")

            expect(response.status_code) == 200
        finally:
            process.kill()
