import os
import http.server
import socketserver

PORT = int(os.environ.get('PORT', 8080))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('Serving at port', PORT)
    httpd.serve_forever()