from http.server import HTTPServer, CGIHTTPRequestHandler

HOST = ""
PORT = 777

if __name__ == '__main__':
    print(f'Starting server in http://localhost:{PORT}')
    server = HTTPServer((HOST, PORT), CGIHTTPRequestHandler)
    server.serve_forever()
