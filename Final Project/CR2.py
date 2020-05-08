import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import json

SERVER = 'rest.ensembl.org'
INITIAL_PARAMETERS = '?content-type=application/json'
conn = http.client.HTTPConnection(SERVER)
# Define the Server's port
PORT = 8080
bases = ['A', 'C', 'T', 'G']

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

seq_args = ''

values_for_params = []


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
# Print the request line
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method in the HTTP protocol request"""
        global seq_args
        termcolor.cprint(self.requestline, 'green')

        req_line = self.requestline.split(' ')

        args = (req_line[1]).split("?")
        first_arg = args[0]

        self.send_response(404)

        try:
            if first_arg == "/":
                contents = Path('listspecies.html').read_text()
                contents += Path('karyotype.html').read_text()
                contents += Path('chromosomelength.html').read_text()
                contents += Path('geneseq.html').read_text()
                contents += Path('geneinfo.html').read_text()
                contents += Path('geneCalc.html').read_text()
                contents += Path('genelist.html').read_text()
                self.send_response(200)
            else:
                if first_arg in '/listSpecies':
                    endpoint = '/info/species'
                    conn.request("GET", endpoint + INITIAL_PARAMETERS)
                    resp1 = conn.getresponse()
                    data_read = resp1.read().decode("utf-8")
                    api_info = json.loads(data_read)
                    if len(args) > 1:
                        args_2 = args
                        second_arg = args_2[1]
                        seq_args = second_arg.split("=")
                    list_species = []
                    if seq_args[1] == '' or (len(seq_args[1]) == 5 and 'json' in seq_args[1]):
                        for e in api_info['species']:
                            list_species.append(e['display_name'])
                    else:
                        if len(seq_args) == 3:
                            seq_args = (seq_args[1]).split('&')
                            sp_name = api_info['species']
                            counter = 0
                            for i in sp_name:
                                if counter < int(seq_args[0]):
                                    list_species.append(i['display_name'])
                                    counter += 1
                        else:
                            sp_name = api_info['species']
                            counter = 0
                            for i in sp_name:
                                if counter < int(seq_args[1]):
                                    list_species.append(i['display_name'])
                                    counter += 1
                    if 'json=1' in req_line[1]:
                        if len(args) == 1 or ('0123456789' not in seq_args[1]):
                            dict_json = {'ListSpecies': list_species}
                            contents = json.dumps(dict_json)
                            self.send_response(200)
                        else:
                            dict_json = {'ListSpecies': {'Limit': seq_args[0], 'Species': list_species}}
                            contents = json.dumps(dict_json)
                            self.send_response(200)
                    else:
                        contents = """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>LIST OF SPECIES</title>
                        </head>
                        <body style="background-color: yellow;">
                        """
                        contents += f"<h2> Species List</h2>"
                        contents += f"<p>The total number of species in ensemble is: {len(api_info['species'])}</p>"
                        if not len(args) == 1 or ((args[1])[-1] == '='):
                            contents += f"<p>Limit: {seq_args[-1]}</p>"
                        for i in list_species:
                            contents += f"<p>-{i}</p>"
                        contents += '<a href="/">Main Page</a>'
                        contents += "</body></html>"
                        self.send_response(200)
                elif first_arg in '/karyotype':
                    second_arg = args[1]
                    seq_args = second_arg.split("=")
                    if '&' in seq_args[1]:
                        sp_arg = (seq_args[1]).split('&')
                        sp_arg = sp_arg[0]
                    else:
                        sp_arg = seq_args[-1]
                    endpoint = '/info/assembly/'
                    params = sp_arg + INITIAL_PARAMETERS
                    conn.request("GET", endpoint + params)
                    resp1 = conn.getresponse()
                    data_read = resp1.read().decode("utf-8")
                    api_info = json.loads(data_read)
                    karyotype_list = []
                    for i in api_info['karyotype']:
                        karyotype_list.append(i)
                    if 'json=1' in req_line[1]:
                        dict_json = {'species': {sp_arg: {'chromosomes': karyotype_list}}}
                        contents = json.dumps(dict_json)
                    else:
                        contents = """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>KARYOTYPE</title>
                        </head>
                        <body style="background-color: yellow;">
                        """
                        contents += f"<h2> Karyotype of the species: {seq_args[-1]}</h2>"
                        for n in karyotype_list:
                            contents += f"<p>{n}</p>"
                        contents += '<a href="/">Main page</a>'
                        contents += "</body></html>"
                    self.send_response(200)
                elif first_arg in "/chromosomeLength":
                    second_arg = args[1]
                    seq_args = second_arg.split("=")
                    args_def = seq_args[1].split("&")
                    chromosome = seq_args[-1]
                    if 'json' in seq_args[2]:
                        args_json = seq_args[2].split('&')
                        chromosome = args_json[0]
                    endpoint = '/info/assembly/'
                    params = args_def[0] + INITIAL_PARAMETERS
                    conn.request("GET", endpoint + params)
                    resp1 = conn.getresponse()
                    data_read = resp1.read().decode("utf-8")
                    api_info = json.loads(data_read)
                    chromosome_length = ''
                    for e in api_info['top_level_region']:
                        if e['name'] == chromosome:
                            chromosome_length += str(e['length'])
                    if 'json=1' in req_line[1]:
                        dict_json = {'species': {args_def[0]: {
                            'Chromosome': {chromosome: {'The length of the chromosome is:': chromosome_length}}}}}
                        contents = json.dumps(dict_json)
                    else:
                        contents = """
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>CHROMOSOME LENGTH</title>
                        </head>
                        <body style="background-color: yellow;">
                        """
                        contents += f"<h2> Chromosome: {seq_args[-1]} Species: {args_def[0]}</h2>"
                        contents += f"<p>The length of the chromosome is:   {chromosome_length}</p>"
                        contents += '<a href="/">Main page</a>'
                        contents += "</body></html>"
                    self.send_response(200)
                elif first_arg == "/geneList":
                    endpoint = '/overlap/region/human/'
                    second_arg = args[1]
                    seq_args = second_arg.split("&")

                    contents = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>CHROMOSOME LENGTH</title>
                    </head>
                    <body style="background-color: yellow;">
                    """
                    for e in seq_args:
                        e = e.split('=')
                        values_for_params.append(e[-1])
                    params = values_for_params[0] + ':' + values_for_params[1] + '-' + values_for_params[2] + '?feature=gene;content-type=application/json '
                    conn.request("GET", endpoint + params)
                    resp1 = conn.getresponse()
                    data_1 = resp1.read().decode("utf-8")
                    api_info_of_genelist = json.loads(data_1)
                    contents += f"<h2>The genes in the chromosome {values_for_params[0]} that start at {values_for_params[1]} and end at {values_for_params[2]} are:</h2> "
                    gene_in_chromosome = []
                    for i in api_info_of_genelist:
                        contents += f"<p>{i['external_name']}</p>"
                        gene_in_chromosome.append(i['external_name'])
                    contents += '<a href="/">Main page</a>'
                    contents += "</body></html>"
                    if 'json=1' in req_line[1]:
                        dict_json = {'chromosome': values_for_params[0], 'Start': values_for_params[1],
                                     'End': values_for_params[2], 'Genes': gene_in_chromosome}
                        contents = json.dumps(dict_json)
                    self.send_response(200)
                else:
                    endpoint_1 = '/xrefs/symbol/homo_sapiens/'
                    second_arg = args[1]
                    seq_args = second_arg.split("=")
                    gene_name = seq_args[1]
                    if 'json' in seq_args[1]:
                        args_json = seq_args[1].split('&')
                        gene_name = args_json[0]
                    params_1 = gene_name + INITIAL_PARAMETERS
                    conn.request("GET", endpoint_1 + params_1)
                    resp1 = conn.getresponse()
                    data_1 = resp1.read().decode("utf-8")
                    api_info_id = json.loads(data_1)
                    gene_id = api_info_id[0]
                    gene_id = gene_id['id']
                    endpoint_2 = '/sequence/id/'
                    params_2 = gene_id + INITIAL_PARAMETERS
                    conn.request("GET", endpoint_2 + params_2)
                    resp2 = conn.getresponse()
                    data_2 = resp2.read().decode("utf-8")
                    api_info_seq = json.loads(data_2)
                    contents = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>GENE</title>
                    </head>
                    <body style="background-color: yellow;">
                    """
                    if first_arg == "/geneSeq":
                        gene_seq = ''
                        gene_seq += api_info_seq['seq']
                        if 'json=1' in req_line[1]:
                            dict_json = {'Gene name:': {gene_name: {'Sequence': gene_seq}}}
                            contents = json.dumps(dict_json)
                        else:
                            contents += f"<h2>The sequence of the gene {gene_name}</h2>"
                            contents += f"<textarea readonly rows = 20 cols = 80>{gene_seq}</textarea>"
                            contents += '<a href="/">Main page</a>'
                            contents += "</body></html>"
                    elif first_arg == '/geneInfo':
                        endpoint_3 = '/lookup/id/'
                        params_3 = gene_id + INITIAL_PARAMETERS
                        conn.request("GET", endpoint_3 + params_3)
                        resp3 = conn.getresponse()
                        data_3 = resp3.read().decode("utf-8")
                        api_info_gene = json.loads(data_3)
                        seq0 = Seq(api_info_seq['seq'])
                        if 'json=1' in req_line[1]:
                            dict_json = {'gene': gene_name, 'Start': api_info_gene['start'],
                                         'End': api_info_gene['end'],
                                         'Length': seq0.len(), 'Chromosome': api_info_gene['seq_region_name'],
                                         'ID': gene_id}
                            contents = json.dumps(dict_json)
                        else:
                            contents += f"<h2>Information about the gene: {gene_name}</h2>"
                            contents += f"<p>The start: {api_info_gene['start']}</p>"
                            contents += f"<p>The end: {api_info_gene['end']}</p>"
                            contents += f"<p>The length of the gene's sequence is: {seq0.len()}</p>"
                            contents += f"<p>This gene is located in the chromosome: {api_info_gene['seq_region_name']}</p>"
                            contents += f"<p>The ID of the gene is: {gene_id}</p>"
                            contents += '<a href="/">Main page</a>'
                            contents += "</body></html>"
                    elif first_arg == "/geneCalc":
                        seq0 = Seq(api_info_seq['seq'])
                        if 'json=1' in req_line[1]:
                            for e in bases:
                                contents += f"<p>{e} : {seq0.count_base(e)} ({round(seq0.count_base(e) * (100 / seq0.len()), 2)}%)</p> "
                            dict_json = {'Gene': gene_name, 'Length': seq0.len(), 'A': {seq0.count_base('A'): {
                                'Percentage': (round(seq0.count_base('A') * (100 / seq0.len()), 2))}}, 'C': {
                                seq0.count_base('C'): {
                                    'Percentage': (round(seq0.count_base('C') * (100 / seq0.len()), 2))}}, 'T': {
                                seq0.count_base('T'): {
                                    'Percentage': (round(seq0.count_base('T') * (100 / seq0.len()), 2))}}, 'G': {
                                seq0.count_base('G'): {
                                    'Percentage': (round(seq0.count_base('G') * (100 / seq0.len()), 2))}}}
                            contents = json.dumps(dict_json)
                        else:
                            contents += f"<h2>Some calculations of the gene: {gene_name}</h2>"
                            contents += f"<p>The length of the sequence is: {seq0.len()}</p>"
                            for e in bases:
                                contents += f"<p>{e} : {seq0.count_base(e)} ({round(seq0.count_base(e) * (100 / seq0.len()), 2)}%)</p>"
                    self.send_response(200)

        except (KeyError, ValueError, IndexError, TypeError):
            contents = Path('Error.html').read_text()

        if 'json=1' in req_line:
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

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

