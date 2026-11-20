import mimetypes
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = Path(sys.argv[2] if len(sys.argv) > 2 else "public").resolve()

TYPES = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".txt": "text/plain; charset=utf-8",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".svg": "image/svg+xml",
}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body=b"", ctype="text/plain; charset=utf-8", extra=None):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _serve(self):
        path = self.path.split("?", 1)[0]
        if path == "/":
            path = "/index.html"
        target = (ROOT / path.lstrip("/")).resolve()
        # защита от выхода за пределы корня (../)
        if ROOT not in target.parents and target != ROOT:
            return self._send(404, b"404 Not Found")
        if not target.is_file():
            return self._send(404, b"404 Not Found")
        ctype = TYPES.get(target.suffix.lower()) or mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self._send(200, target.read_bytes(), ctype)

    def do_GET(self):
        self._serve()

    def do_HEAD(self):
        self._serve()

    def _not_allowed(self):
        self._send(405, b"405 Method Not Allowed", extra={"Allow": "GET, HEAD"})

    do_POST = do_PUT = do_DELETE = do_PATCH = _not_allowed


if __name__ == "__main__":
    ROOT.mkdir(exist_ok=True)
    index = ROOT / "index.html"
    if not index.exists():
        index.write_text("<h1>Привет из статического сервера</h1>", encoding="utf-8")
    print(f"Раздаю {ROOT} на http://localhost:{PORT}")
    HTTPServer(("", PORT), Handler).serve_forever()
