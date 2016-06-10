"""Settings loaded from the environment."""

import os
import sys

sys.argv[0] = 'sappy'  # use a consistent name regardless of program invocation

DEFAULT_PATHS = 'dist', 'site', '_site', 'public'

HOST = os.getenv('SAPPY_HOST', "")
PORT = int(os.getenv('SAPPY_PORT', 8080))


def get_address(port=None):
    """Get the (host, port) for server bindings."""
    return HOST, port or PORT
