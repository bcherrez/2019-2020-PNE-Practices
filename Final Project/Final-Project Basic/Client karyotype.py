
# http://rest.ensembl.org/info/assembly/homo_sapiens?content-type=application/json


import http.client
import http.server
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
ensembl_data=json.loads(data)
print(f"Response received!: {response.status} {response.reason}\n")

specie=input("Select the specie ")
# chromosome = ensembl_data['karyotype']

if specie == "Human":
     print("The name of the chromosomes are :")
     for chromosomes in ensembl_data['karyotype']:
        print(chromosomes)
else:
    print("Error html")
