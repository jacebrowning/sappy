"""The HTTP server."""

import os
import sys
from pathlib import Path
from http.server import HTTPServer

import click

from . import __version__, settings
from .handlers import SinglePageApplicationHandler

sys.argv[0] = 'sappy'
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('path', default="dist")
@click.version_option(version=__version__)
def main(path=None):
    """Serve a single-page application from a directory."""
    path, httpd = init(path)

    click.echo("Serving {d}/ on {p}".format(d=path, p=httpd.server_port))
    httpd.serve_forever()


def init(root):
    """Create a new HTTP daemon to run."""
    path = Path(root).resolve()

    os.chdir(str(path))
    httpd = HTTPServer(settings.ADDRESS, SinglePageApplicationHandler)

    return path, httpd
