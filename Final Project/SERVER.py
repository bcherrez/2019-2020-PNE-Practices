import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import json

SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'
conn = http.client.HTTPConnection(SERVER)
# Define the Server's port
PORT = 8080
bases = ['A', 'C', 'T', 'G']

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


limit_value = " "


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
# Print the request line

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method in the HTTP protocol request"""
        termcolor.cprint(self.requestline, 'green')
        request_line = self.requestline.split(' ')
        arguments = (request_line[1]).split("?")
        resource = arguments[0]
        self.send_response(404)
        # to avoid error: local _variable may be referenced before assignment
        global PARAMS, limit_value

        try:
            if resource == "/":
                contents = Path('Main page.html').read_text()
                self.send_response(200)

            elif resource == '/listSpecies':
                endpoint = '/info/species'
                conn.request("GET", endpoint + PARAMS)
                response = conn.getresponse()
                data = response.read().decode("utf-8")
                ensembl_data = json.loads(data)
                species = ensembl_data['species']

                if len(arguments) > 1:
                    new_argument = arguments
                    limit = new_argument[1]
                    limit_value = limit.split("=")
                list_species = []
                if limit_value[1] == '':
                    for item in ensembl_data['species']:
                        list_species.append(item['common_name'])
                else:

                    if len(limit_value) == 3:
                        limit_value = (limit_value[1]).split('&')
                        species = ensembl_data['species']
                        count = 0
                        for item in species:
                            if count < int(limit_value[0]):
                                list_species.append(item['common_name'])
                                count += 1
                    else:
                        species = ensembl_data['species']
                        count = 0
                        for item in species:
                            if count < int(limit_value[1]):
                                list_species.append(item['common_name'])
                                count += 1
                contents = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <title>LIST OF SPECIES IN THE BROWSER</title>
                <meta charset="utf-8">
                </head>
                <body style="background-color: orange;">
                """
                contents += f"<p>The total number of species is :{len(species)}</p>"

                if not limit_value[1] == '':
                    contents += f"<p>The limit you have selected is: {limit_value[-1]}</p>"
                contents += f"<p>The name of the species are: "
                for item in list_species:
                    contents+=f"<p>-{item}</p>"
                contents += '<a href="/">Main Page</a>'
                contents += "</body></html>"

            elif resource == '/karyotype':
                new_arg = arguments
                specie = new_arg[1]
                specie_name = specie.split("=")
                if '&' in specie_name[1]:
                    specie_argument = (specie_name[1]).split('&')
                    specie_argument = specie_argument[0]
                else:
                    specie_argument = specie_name[-1]
                endpoint = '/info/assembly/'
                params = specie_argument + PARAMS
                conn.request("GET", endpoint + params)
                response = conn.getresponse()
                data = response.read().decode("utf-8")
                ensembl_data = json.loads(data)
                karyotype_list = []
                for item in ensembl_data['karyotype']:
                    karyotype_list.append(item)

                contents = """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>KARYOTYPE</title>
                        </head>
                        <body style="background-color: lightgreen;">
                        """
                contents += f"<h2> The karyotype of the specie {specie_name[-1]} is: </h2>"
                for chromosomes in karyotype_list:
                    contents += f"<p>{chromosomes}</p>"
                contents += '<a href="/">Main page</a>'
                contents += "</body></html>"
                self.send_response(200)
            elif resource == "/chromosomeLength":
                new_argument = arguments[1]
                chromo_n = new_argument.split("=")
                specie_n = chromo_n[1].split("&")
                chromosome = chromo_n[-1]

                endpoint = '/info/assembly/'
                params = specie_n[0] + PARAMS
                conn.request("GET", endpoint + params)
                response = conn.getresponse()
                data = response.read().decode("utf-8")
                ensembl_data = json.loads(data)
                chromosome_length = ''
                for item in ensembl_data['top_level_region']:
                    if item['name'] == chromosome:
                        chromosome_length = str(item['length'])
                contents = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                    <meta charset="utf-8">
                    <title>CHROMOSOME LENGTH</title>
                    </head>
                    <body style="background-color: pink;">
                    """
                contents += f"<p>The length of the {specie_n[0]} chromosome {chromo_n[-1]} is: {chromosome_length}</p>"
                contents += '<a href="/">Main page</a>'
                contents += "</body></html>"
                self.send_response(200)
            elif resource == "/geneList":
                endpoint = '/overlap/region/human/'
                new_argument = arguments[1]
                sequence_argument = new_argument.split("&")

                contents = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>CHROMOSOME LENGTH</title>
                    </head>
                    <body style="background-color: yellow;">
                    """
                for i in sequence_argument:
                    i = i.split('=')
                    values_for_params.append(i[-1])
                PARAMS = values_for_params[0] + ':' + values_for_params[1] + '-' + values_for_params[
                    2] + "?feature=gene;content-type=application/json"
                conn.request("GET", endpoint + PARAMS)
                response_1 = conn.getresponse()
                data_1 = response_1.read().decode("utf-8")
                ensembl_gene = json.loads(data_1)
                contents += f"<h2>The genes in the chromosome {values_for_params[0]} that start at {values_for_params[1]} and end at {values_for_params[2]} are:</h2> "
                gene_list = []
                for item in ensembl_gene:
                    contents += f"<p>{item['external_name']}</p>"
                    gene_list.append(item['external_name'])
                contents += '<a href="/">Main page</a>'
                contents += "</body></html>"
                self.send_response(200)
            else:
                    endpoint_1 = '/xrefs/symbol/homo_sapiens/'
                    new_argument = arguments[1]
                    sequence_arguments = new_argument.split("=")
                    gene_name = sequence_arguments[1]

                    params_1 = gene_name + PARAMS
                    conn.request("GET", endpoint_1 + params_1)
                    response_1 = conn.getresponse()
                    data_1 = response_1.read().decode("utf-8")
                    ensembl_data_id = json.loads(data_1)
                    gene_id = ensembl_data_id[0]
                    gene_id = gene_id['id']
                    endpoint_2 = '/sequence/id/'
                    params_2 = gene_id + PARAMS
                    conn.request("GET", endpoint_2 + params_2)
                    response_2 = conn.getresponse()
                    data_2 = response_2.read().decode("utf-8")
                    ensembl_data = json.loads(data_2)
                    contents = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>GENE</title>
                    </head>
                    <body style="background-color: lightblue;">
                    """
                    if resource == "/geneSeq":
                        gene_seq = ''
                        gene_seq += ensembl_data['seq']
                        contents += f"<h2>The sequence of the gene {gene_name} is : </h2>"
                        contents += f"<textarea readonly rows = 20 cols = 90>{gene_seq}</textarea>"
                        contents += '<a href="/">Main page</a>'
                        contents += "</body></html>"
                    if resource == '/geneInfo':
                        endpoint_3 = '/lookup/id/'
                        params_3 = gene_id + PARAMS
                        conn.request("GET", endpoint_3 + params_3)
                        response = conn.getresponse()
                        data = response.read().decode("utf-8")
                        ensembl_seq = json.loads(data)
                        sequence = Seq(ensembl_data['seq'])
                        contents += f"<h2>Information about the gene: {gene_name}</h2>"
                        contents += f"<p>Start: {ensembl_seq['start']}</p>"
                        contents += f"<p>End: {ensembl_seq['end']}</p>"
                        contents += f"<p>Length: {sequence.len()}</p>"
                        contents += f"<p>In chromosome: {ensembl_seq['seq_region_name']}</p>"
                        contents += f"<p>ID: {gene_id}</p>"
                        contents += '<a href="/">Main page</a>'
                        contents += "</body></html>"
                    if resource == "/geneCalc":
                        sequence = Seq(ensembl_data['seq'])
                        contents += f"<h2>Calculations of the gene: {gene_name}</h2>"
                        contents += f"<p>Length: {sequence.len()}</p>"
                        for element in bases:
                            contents += f"<p>{element} : {sequence.count_base(element)} ({round(sequence.count_base(element) * (100 / sequence.len()), 3)}%)</p>"
                    self.send_response(200)

        except(KeyError, ValueError, IndexError, TypeError):
            contents = Path('Error.html').read_text()
        else:
            self.send_header('Content-Type', 'text/html')
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

