
import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port

PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # -- Parse the path
        # -- NOTE: self.path already contains the requested resource
        list_resource = self.path.split('?')
        resource= list_resource[0]

        if resource == "/":
            # Read the file
            contents = Path('Index.html').read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/listSpecies":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, value = pairs[0].split("=")
            # Read the file

            import http.client
            import json
            SERVER = 'rest.ensembl.org'
            ENDPOINT = '/info/species'
            PARAMS = '?content-type=application/json'
            URL = SERVER + ENDPOINT + PARAMS

            print()
            print(f"Server: {SERVER}")
            print(f"URL: {URL}")

            # Connect with the server
            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + PARAMS)

            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()
            # solo ha pillado la ultima especie pero ya es algooo , solo pilla  uno
            content_type = 'text/html'
            response = conn.getresponse()
            data = response.read().decode()
            ensembl_data = json.loads(data)
            species = len(ensembl_data['species'])
            for item in ensembl_data['species']:
                common_name = item['common_name']
            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                        <title> LIST OF SPECIES IN THE BROWSER </title >
                        </head >
                        <body style="background-color: lightblue;>
                        <p> The limit you have selected is:  </p>
                        <p>The total number of species in the ensembl is: {species}  </p>
                        <p> The names of the species are: {common_name}  </p>
                        </body>
                        </html>
                        """

            error_code = 200
        elif resource=="/karyotype":
            # Read the file
            import http.client
            import json
            SERVER = 'rest.ensembl.org'
            ENDPOINT = '/info/assembly/homo_sapiens'
            PARAMS = '?content-type=application/json'
            URL = SERVER + ENDPOINT + PARAMS

            print()
            print(f"Server: {SERVER}")
            print(f"URL: {URL}")

            # Connect with the server
            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + PARAMS)

            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            response = conn.getresponse()
            data = response.read().decode()
            ensembl_data = json.loads(data)
            print(f"Response received!: {response.status} {response.reason}\n")

            for chromosome in ensembl_data['karyotype']:

              contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                        <title> KARYOTYPE OF A SPECIFIC SPECIES</title >
                        </head>
                        <body style="background-color: lightblue;">
                        <p> The name of the chromosomes are : {chromosome} </p>
                        </body>
                        </html>
                        """
            content_type = 'text/html'
            error_code = 404
        elif resource == "/chromosomeLength":
            # Read the file
            content_type = 'text/html'
            contents ="""
                  <!DOCTYPE html>
                  <html lang="en">
                  <head>
                  <meta charset="UTF-8">
                  <title>LENGTH OF THE SELECTED CHROMOSOME </title>
                  </head>
                  <body style="background-color: lightblue;">
                  <body>
                  <p>The length of the chromosome is: </p>
                  </body>
                  </html>
            """

            error_code = 200
        else:
            # Read the file
            contents = Path('Error.html').read_text()
            content_type = 'text/html'
            error_code = 404

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()



# if common_ name not in ensemmble_data, contents equal error.html
# avoid error de coger solo un dato , añadir indices (seq server 2)
# no hace falta html a parte del main page????
# limit
# specie
# specie and chromo
