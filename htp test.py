import http.server
import socketserver

PORT = 8000  # 서버 포트

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("서버 시작 - 포트:", PORT)
    httpd.serve_forever()
