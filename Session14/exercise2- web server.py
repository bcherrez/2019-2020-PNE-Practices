import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        req_line = self.requestline.split(' ')
        path = req_line[1]
        path = path[1:]
        # Content type header
        # Error and the main page are in HTML
        content_type = 'text/html'

        if path == "":
            path = "index.html"

        if path == "index.html":
            termcolor.cprint("Main page requested", 'blue')

            # Read the index from the file
            contents = Path(path).read_text()

            # Status code is ok
            status = 200
        else:
            termcolor.cprint("ERROR: Not found", 'red')
            contents = Path("Error.html").read_text()
            status = 404
        self.send_response(status)

        # Define the content-type header:
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