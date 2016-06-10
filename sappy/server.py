"""The HTTP server."""

import os
from pathlib import Path
from http.server import HTTPServer

from . import __version__, settings
from .handlers import SinglePageApplicationHandler


def init(root, port):
    """Create a new HTTP daemon to run."""
    path = Path.cwd()
    for root in [root, *settings.DEFAULT_PATHS]:
        if root and Path(root).exists():
            path = Path(root).resolve()  # pylint: disable=redefined-variable-type
            os.chdir(str(path))
            break

    address = settings.get_address(port=port)
    httpd = HTTPServer(address, SinglePageApplicationHandler)

    return path, httpd
