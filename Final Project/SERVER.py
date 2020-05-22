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


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # Analize the request line
        request_line = self.requestline.split(' ')
        # Generating the response message
        arguments = (request_line[1]).split("?")
        resource = arguments[0]
        error_code = 404

        try:
            if resource == "/":
                contents = Path('Main page.html').read_text()
                self.send_response(200)
            elif resource == '/listSpecies':
                new_argument = arguments
                limit = new_argument[1]
                limit_value = limit.split("=")
                list_species = []
                endpoint = '/info/species'
                conn.request("GET", endpoint + PARAMS)
                response = conn.getresponse()
                data = response.read().decode("utf-8")
                ensembl_data = json.loads(data)
                species = ensembl_data['species']
                if limit_value[1] == '':
                    for item in species:
                        list_species.append(item['common_name'])
                else:
                    count = 0
                    for item in species:
                        if count < int(limit_value[1]):
                            list_species.append(item['common_name'])
                            count += 1
                if 'json=1' in request_line[1]:
                    if limit_value[1] == '':
                        json_data ={'ListSpecies': list_species}
                        contents = json.dumps(json_data)
                        self.send_response(200)
                    else:
                        json_data = {'ListSpecies': {'Limit': limit_value[0], 'Species': list_species}}
                        contents = json.dumps(json_data)
                        self.send_response(200)
                else:
                    contents = Path("list species.html").read_text()
                    contents += f"<p>The total number of species is :{len(species)}</p>"
                    if not limit_value[1] == '':
                        contents += f"<p>The limit you have selected is: {limit_value[-1]}</p>"
                    contents += f"<p>The name of the species are: "
                    for item in list_species:
                        contents += f"<p>-{item}</p>"
                    self.send_response(200)
            elif resource == '/karyotype':
                new_argument = arguments
                specie = new_argument[1]
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
                if 'json=1' in request_line[1]:
                    json_data = {'species': {specie_argument: {'chromosomes': karyotype_list}}}
                    contents = json.dumps(json_data)
                else:
                    contents = Path("karyotype.html").read_text()
                    contents += f"<h2> The karyotype of the specie {specie_name[-1]} is: </h2>"
                    for chromosomes in karyotype_list:
                        contents += f"<p>{chromosomes}</p>"
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
                if 'json=1' in request_line[1]:
                    json_data = {'species': {specie_n[0]: {
                        'Chromosome': {chromosome: {'The length of the chromosome is:': chromosome_length}}}}}
                    contents = json.dumps(json_data)
                else:
                    contents = Path("chromosome length.html").read_text()
                    contents += f"<p>The length of the {specie_n[0]} chromosome {chromo_n[-1]} is: {chromosome_length}</p>"
                self.send_response(200)

            elif resource == "/geneList":
                new_argument = arguments[1]
                seq_argument = new_argument.split("&")
                params_n = []
                for e in seq_argument:
                    e = e.split('=')
                    params_n.append(e[-1])

                endpoint = "/overlap/region/human/"
                params = params_n[0] + ":" + params_n[1] + "-" + params_n[
                    2] + "?feature=gene;content-type=application/json"
                conn.request("GET", endpoint + params)
                response_g = conn.getresponse()
                data_g = response_g.read().decode("utf-8")
                gene_d = json.loads(data_g)
                gene_list = []
                for element in gene_d:
                    gene_list.append(element['external_name'])
                contents = Path("gene list.html").read_text()
                contents += f"<h2>The genes in the chromosome {params_n[0]} starting at {params_n[1]} and ending at {params_n[2]} are:</h2>"
                for genes in gene_list:
                    contents += f"<p>{genes}</p>"
                if 'json=1' in request_line[1]:
                    json_data = {'Chromosome': params_n[0], 'Start': params_n[1],
                                 'End': params_n[2], 'Genes': gene_list}
                    contents = json.dumps(json_data)
                self.send_response(200)

            else:
                new_argument = arguments[1]
                sequence_arguments = new_argument.split("=")
                gene_name = sequence_arguments[1]
                if 'json' in sequence_arguments[1]:
                    arguments_json = sequence_arguments[1].split('&')
                    gene_name = arguments_json[0]

                endpoint_1 = '/xrefs/symbol/homo_sapiens/'
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
                contents = Path("human gene.html").read_text()
                self.send_response(200)

                if resource == "/geneSeq":
                    gene_seq = ''
                    gene_seq += ensembl_data['seq']
                    if 'json=1' in request_line[1]:
                        json_data = {'Gene name:': {gene_name: {'Sequence': gene_seq}}}
                        contents =json.dumps(json_data)
                    else:
                        contents += f"<h2>The sequence of the gene {gene_name} is : </h2>"
                        contents += f"<textarea readonly rows = 20 cols = 90>{gene_seq}</textarea>"
                if resource == '/geneInfo':
                    endpoint_3 = '/lookup/id/'
                    params_3 = gene_id + PARAMS
                    conn.request("GET", endpoint_3 + params_3)
                    response_3 = conn.getresponse()
                    data = response_3.read().decode("utf-8")
                    ensembl_seq = json.loads(data)
                    sequence = Seq(ensembl_data['seq'])
                    if 'json=1' in request_line[1]:
                        json_data = {'Gene': gene_name, 'Start': ensembl_seq ['start'],
                                     'End': ensembl_seq ['end'],
                                     'Length': sequence.len(), 'Chromosome': ensembl_seq ['seq_region_name'],
                                     'ID': gene_id}
                        contents = json.dumps(json_data)
                    else:
                        contents += f"<h2>Information about the gene: {gene_name}</h2>"
                        contents += f"<p>Start: {ensembl_seq['start']}</p>"
                        contents += f"<p>End: {ensembl_seq['end']}</p>"
                        contents += f"<p>Length: {sequence.len()}</p>"
                        contents += f"<p>In chromosome: {ensembl_seq['seq_region_name']}</p>"
                        contents += f"<p>ID: {gene_id}</p>"
                if resource == "/geneCalc":
                    sequence = Seq(ensembl_data['seq'])
                    if 'json=1' in request_line[1]:
                        for item in bases:
                            contents += f"<p>{item} : {sequence.count_base(item)} ({round(sequence.count_base(item) * (100 / sequence.len()), 2)}%)</p> "
                        json_data = {'Gene': gene_name, 'Length': sequence.len(), 'A': {sequence.count_base('A'): {
                                'Percentage': (round(sequence.count_base('A') * (100 / sequence.len()), 2))}}, 'C': {
                            sequence.count_base('C'): {
                                'Percentage': (round(sequence.count_base('C') * (100 / sequence.len()), 2))}}, 'T': {
                            sequence.count_base('T'): {
                                'Percentage': (round(sequence.count_base('T') * (100 / sequence.len()), 2))}}, 'G': {
                            sequence.count_base('G'): {
                                'Percentage': (round(sequence.count_base('G') * (100 / sequence.len()), 2))}}}
                        contents = json.dumps(json_data)
                    else:
                        contents += f"<h2>Calculations of the gene: {gene_name}</h2>"
                        contents += f"<p>Length: {sequence.len()}</p>"
                        for item in bases:
                            contents += f"<p>{item} : {sequence.count_base(item)} ({round(sequence.count_base(item) * (100 / sequence.len()), 3)}%)</p>"
                self.send_response(200)

        except(KeyError, ValueError, IndexError, TypeError):
            # Generating the response message
            contents = Path('Error.html').read_text()
            self.send_response(error_code)
        if 'json=1' in request_line[1]:
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', len(str.encode(contents)))
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

    # -- Main loop: Attend the client. Whenever there is a new client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
