

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
#for item in ensembl_data['species']:
    #print(item)
    #common_name = item['common_name']
    #print(common_name)

Limit = input("limit:")
print("The limit you have selected is:", Limit)
if Limit == None :
    for item in ensembl_data['species']:
        common_name = item['common_name']
        print(common_name)
else:
    for item in ensembl_data['species']:
        for item in range(0,Limit ):
            common_name = item['common_name']
            print(common_name)




# rest.ensembl.org/info/species?content-type=application/json
# href en html y una vez obtenido datos jugar con ellos(esta en el client) y print los contents as a html response
# en principio el server no deberia cambiar
# conseguir que si no tiene un dato vaya a error


# -- Send the Gene
clnt.debug_talk(f"Sending {GENE} Gene to the server...")
clnt.debug_talk(str(s))
#  it prints on the console both the message sent to the server and the response received