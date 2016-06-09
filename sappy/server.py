"""The HTTP server."""

import os
from pathlib import Path
from http.server import HTTPServer
import logging

from . import settings
from .handlers import SinglePageApplicationHandler


log = logging.getLogger(__name__)


def main():
    """Run the server."""
    path, httpd = init()

    print("Serving {d}/ on {p}".format(d=path, p=httpd.server_port))
    httpd.serve_forever()


def init(root="dist"):
    """Create a new HTTP daemon to run."""
    path = Path(root).resolve()

    os.chdir(str(path))
    httpd = HTTPServer(settings.ADDRESS, SinglePageApplicationHandler)

    return path, httpd
