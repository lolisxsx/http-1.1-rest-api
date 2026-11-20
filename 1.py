import socket
import sys

host = sys.argv[1] if len(sys.argv) > 1 else "example.com"
port = 80

request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Connection: close\r\n"
    "\r\n"
)

with socket.create_connection((host, port), timeout=10) as sock:
    sock.sendall(request.encode("ascii"))
    chunks = []
    while True:
        data = sock.recv(4096)
        if not data:
            break
        chunks.append(data)

response = b"".join(chunks)
head, _, body = response.partition(b"\r\n\r\n")
print("=== Статус и заголовки ===")
print(head.decode("iso-8859-1"))
print("\n=== Тело (первые 300 байт) ===")
print(body[:300].decode("utf-8", errors="replace"))
