
import http.client
import http.server
import json

PORT = 8080
SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/assembly/homo_sapiens'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", ENDPOINT + PARAMS)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()


response = conn.getresponse()
data = response.read().decode()
ensembl_data=json.loads(data)
print(f"Response received!: {response.status} {response.reason}\n")



    # http: // rest.ensembl.org / lookup / id / ENSG00000157764?content - type = application / json;
    # http://rest.ensembl.org / info / genomes / nanoarchaeum_equitans_kin4_m?content - type = application / json
    # http: // rest.ensembl.org / regulatory / species / homo_sapiens / epigenome?content - type = application / json
    # http: // rest.ensembl.org / info / genomes / division / EnsemblPlants?content - type = application / json
    # https://docs.python.org/3/library/http.server.html#module-http.server