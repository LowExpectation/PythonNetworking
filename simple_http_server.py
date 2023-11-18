# Create a local host using simple http server
# Testing can be done using this program or CLI below:
# python3 -m http.server - this allows for current directory to be served with default port 8000
# python3 -m http.server 9000 - port 9000 for current directory to be served
# python3 -m http.server --bind 127.0.0.1 - binding for interface local host
# python3 -m http.server --directory /tmp/ - port 8000 but directory is specified
# https://docs.python.org/3.10/library/http.server.html

import http.server, socketserver

# Handle when a URL with specified port is requested during parse above
Handler = http.server.SimpleHTTPRequestHandler
port = 8000

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("serving at port", port)
    httpd.serve_forever()