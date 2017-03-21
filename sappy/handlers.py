"""Request handlers."""

from http.server import SimpleHTTPRequestHandler
from urllib.parse import urlparse
from pathlib import Path


class SinglePageApplicationHandler(SimpleHTTPRequestHandler):
    """Handler to pass all requests to the index."""

    def do_GET(self):
        """Override GETs for unknown paths."""
        params = urlparse(self.path)
        path = Path(params.path.strip('/'))

        if path.exists():
            super().do_GET()

        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open("index.html", 'rb') as rfile:
                self.copyfile(rfile, self.wfile)
