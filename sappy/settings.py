"""Settings loaded from the environment."""

import os


HOST = os.getenv('SAPPY_HOST', "")
PORT = int(os.getenv('SAPPY_PORT', 8080))


def get_address(port=None):
    """Get the (host, port) for server bindings."""
    return HOST, port or PORT
