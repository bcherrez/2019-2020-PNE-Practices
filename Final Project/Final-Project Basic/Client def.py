
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


response = conn.getresponse()
data = response.read().decode()
ensembl_data=json.loads(data)
print(f"Response received!: {response.status} {response.reason}\n")

# print the species of there is no limit specified
# first key is species
for item in ensembl_data['species']:
    # print(item)
    common_name = item['common_name']
    print(common_name)


