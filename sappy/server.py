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

ReadableDirectory = click.Path(exists=True, readable=True, file_okay=False)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('root', type=ReadableDirectory, required=False)
@click.option('-p', '--port', type=int)
@click.version_option(version=__version__)
def main(root=None, port=None):
    """Serve a single-page application from a directory."""
    path, httpd = init(root, port)

    click.echo("Serving {d}/ on {p}".format(d=path, p=httpd.server_port))
    httpd.serve_forever()


def init(root, port):
    """Create a new HTTP daemon to run."""
    path = Path.cwd()
    for root in [root, 'dist', 'public']:
        if root and Path(root).exists():
            path = Path(root).resolve()  # pylint: disable=redefined-variable-type
            os.chdir(str(path))
            break

    address = settings.get_address(port=port)
    httpd = HTTPServer(address, SinglePageApplicationHandler)

    return path, httpd
