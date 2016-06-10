# pylint: disable=missing-docstring,unused-variable,redefined-outer-name,unused-argument,expression-not-assigned

import os
import sys
import subprocess
import time

import pytest
from expecter import expect
from click.testing import CliRunner
import requests

from sappy.cli import main


def cli(*options):
    args = sys.executable, '-m', 'sappy', *options
    process = subprocess.Popen(args)
    time.sleep(0.5)
    return process


@pytest.fixture
def temp(tmpdir):
    tmpdir.chdir()


@pytest.fixture
def temp_with_dist(temp):
    os.mkdir("dist")


def describe_cli():

    def with_defaults(temp_with_dist):
        process = cli()

        try:
            response = requests.get("http://localhost:8080/foobar")
        finally:
            process.kill()

        expect(response.status_code) == 200

    def with_custom_directory(temp):
        process = cli('.')

        try:
            response = requests.get("http://localhost:8080/foobar")
        finally:
            process.kill()

        expect(response.status_code) == 200

    def with_custom_port(temp_with_dist):
        process = cli('--port=1234')

        try:
            response = requests.get("http://localhost:1234/foobar")
        finally:
            process.kill()

        expect(response.status_code) == 200

    def with_an_invalid_directory(temp):
        runner = CliRunner()
        result = runner.invoke(main, ['unknown/directory'])

        expect(result.exit_code) == 2
