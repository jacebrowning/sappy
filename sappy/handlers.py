"""Request handlers."""

import os
from urllib.parse import urlparse
from http.server import SimpleHTTPRequestHandler


class SinglePageApplicationHandler(SimpleHTTPRequestHandler):
    """Handler to pass all requests to the index."""

    def do_GET(self):
        """Override GETs for unknown paths."""
        params = urlparse(self.path)
        filepath = '.' + os.sep + params.path

        if os.path.exists(filepath):
            super().do_GET()

        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open("index.html", 'rb') as rfile:
                self.copyfile(rfile, self.wfile)
