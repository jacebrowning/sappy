"""The HTTP server."""

import os
from http.server import HTTPServer
from pathlib import Path

from . import __version__, settings
from .handlers import SinglePageApplicationHandler


def init(custom_root, port):
    """Create a new HTTP daemon to run."""
    path = Path.cwd()
    for root in [custom_root, *settings.DEFAULT_PATHS]:
        if root and Path(root).exists():
            path = Path(root).resolve()
            os.chdir(str(path))
            break

    address = settings.get_address(port=port)
    httpd = HTTPServer(address, SinglePageApplicationHandler)

    return path, httpd
