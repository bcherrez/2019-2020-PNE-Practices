import http.server
import socketserver
import termcolor


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        req_line = self.requestline.split(' ')
        # Get the path. It always start with the / symbol
        path = req_line[1]
        path = path[1:]

        # Variable for sending the response back
        contents = ""
        # Status code
        status = 0
        # Content type header
        content_type = 'text/plain'
        if path == "":
            termcolor.cprint("Main page requested", 'blue')
            contents = "Welcome to my server"
            status = 200
        else:
            termcolor.cprint("ERROR: Not found", 'red')
            contents = "Resource not available"
            # Status code is NOT FOUND
            status = 404
        self.send_response(status)

        # Content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))
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