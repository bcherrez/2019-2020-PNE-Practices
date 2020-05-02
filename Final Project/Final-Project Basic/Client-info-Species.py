
# import socketserver
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
## limit = input("limit")
# print("The limit you have selected is:", limit)
species = len(ensembl_data['species'])




# print the species of there is no limit specified
# first key is species
for item in ensembl_data['species']:
    # print(item)
    # if limit is None:
    common_name = item['common_name']
    print(common_name)
    # else:
        # for common_name in range
        # common_name = item['common_name']
        # print(common_name)


# rest.ensembl.org/info/species?content-type=application/json
# href en html y una vez obtenido datos jugar con ellos(esta en el client) y print los contents as a html response
# en principio el server no deberia cambiar
# conseguir que si no tiene un dato vaya a error