"""Command-line interface."""

import click

from . import __version__
from . import server

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

ReadableDirectory = click.Path(exists=True, readable=True, file_okay=False)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('root', type=ReadableDirectory, required=False)
@click.option('-p', '--port', type=int, help="Port for the web server.")
@click.option('-l', '--launch', is_flag=True, help="Launch the page's index.")
@click.version_option(version=__version__)
def main(root=None, port=None, launch=False):
    """Serve a single-page application from a directory."""
    path, httpd = server.init(root, port)

    click.echo("Serving {d}/ on {p}".format(d=path, p=httpd.server_port))
    if launch:
        click.launch("http://localhost:{p}".format(p=httpd.server_port))
    httpd.serve_forever()
