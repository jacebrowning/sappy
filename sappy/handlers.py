"""Request handlers."""

from http.server import SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

from . import settings


class SinglePageApplicationHandler(SimpleHTTPRequestHandler):
    """Handler to pass all requests to the index."""

    def do_GET(self):
        """Override GETs for unknown paths."""
        params = urlparse(self.path)
        path = Path(params.path.strip("/"))

        if settings.BASIC_AUTH:
            basic_auth = self.headers.get("Authorization")

            if basic_auth != settings.get_basic_auth():
                self.send_response(401)
                self.send_header("WWW-Authenticate", 'Basic realm="Test"')
                self.send_header("Content-type", "text/html")
                self.end_headers()
                return None

        if path.exists():
            return super().do_GET()

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        with open("index.html", "rb") as rfile:
            self.copyfile(rfile, self.wfile)  # type: ignore
        return None
