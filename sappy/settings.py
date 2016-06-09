"""Settings loaded from the environment."""

import os


HOST = os.getenv('SAPPY_HOST', "")
PORT = int(os.getenv('SAPPY_PORT', 8080))
ADDRESS = HOST, PORT
