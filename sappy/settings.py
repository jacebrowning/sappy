"""Settings loaded from the environment."""

import base64
import os
import sys

sys.argv[0] = "sappy"  # use a consistent name regardless of program invocation

DEFAULT_PATHS = "dist", "site", "_site", "public"

HOST = os.getenv("SAPPY_HOST", "")
PORT = int(os.getenv("SAPPY_PORT", "8080"))

BASIC_AUTH = os.getenv("SAPPY_BASIC_AUTH", "")


def get_address(port=None):
    """Get the (host, port) for server bindings."""
    return HOST, port or PORT


def get_basic_auth():
    if BASIC_AUTH:
        return "Basic " + base64.b64encode(BASIC_AUTH.encode()).decode()
    return None
