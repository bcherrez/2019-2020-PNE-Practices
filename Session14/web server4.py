import http.server
import socketserver
import termcolor


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        termcolor.cprint(self.requestline, 'green')

        # Message to send back to the clinet
        contents = "I am the happy server! :-)"
        self.send_response(200)  # -- Status line: OK!
        # Content-type header:
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(contents.encode()))
        # The header is finished
        self.end_headers()
        self.wfile.write(contents.encode())

        return

Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()