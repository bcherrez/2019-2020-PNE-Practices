import http.client
SERVER = 'localhost'
PORT = 8080
# ---endpoints tested in reports
endpoints = ['/', '/listSpecies?limit=10','/listSpecies?limit=hola', '/listSpecies?limit=',
             '/karyotype?specie=human', '/karyotype?specie=human&json=1',
             '/karyotype?specie=zebrafish', '/karyotype?specie=zebrafish&json=1',
             "/karyotype?specie=covid-19","/karyotype?specie=covid-19&json=1",
             '/chromosomeLength?specie=mouse&chromo=1','/chromosomeLength?specie=mouse&chromo=1&json=1',
             '/chromosomeLength?specie=pig&chromo=1', '/chromosomeLength?specie=pig&chromo=1&json=1',
             '/chromosomeLength?specie=plant&chromo=18',  '/chromosomeLength?specie=plant&chromo=18&json=1',
             '/geneSeq?gene=FRAT1', '/geneSeq?gene=FRAT1&json=1',
             '/geneSeq?gene=U5', '/geneSeq?gene=U5&json=1',
             '/geneSeq?gene=FGFR3', '/geneSeq?gene=FGFR3&json=1',
             '/geneInfo?gene=FXN', '/geneInfo?gene=FXN&json=1',
             '/geneInfo?gene=FGFR3', '/geneInfo?gene=FGFR3&json=1',
             '/geneInfo?gene=allgene', '/geneInfo?gene=allgene&json=1',
             '/geneCalc?gene=MIR633','/geneCalc?gene=MIR633&json=1',
             '/geneCalc?gene=RNU6_269P', '/geneCalc?gene=RNU6_269P&json=1',
             '/geneCalc?gene=', '/geneCalc?gene=&json=1',
             '/geneList?chromo=3&start=0&end=30000', '/geneList?chromo=3&start=0&end=30000&json=1',
             '/geneList?chromo=1&start=0&end=30000', '/geneList?chromo=1&start=0&end=30000&json=1',
             '/geneList?chromo=33&start=0&end=30000', '/geneList?chromo=33&start=0&end=30000&json=1', ]

counter = 0
# ----Iterate through the endpoints
for ENDPOINT in endpoints:
    counter += 1
    URL = SERVER + ENDPOINT

    print()
    print('* TEST', counter, ':\n')
    print('\t * INPUT: ')
    print('\t', URL, '\n')
    print('\t * OUTPUT: ')

    # ---Connect with the server
    conn = http.client.HTTPConnection(SERVER, PORT)

    # -- Send the request message, using the GET method.
    try:
        conn.request("GET", ENDPOINT)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()
    # -- Print the status line
    print(f"\t Response received!: {r1.status} {r1.reason}\n")
    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    # ---Print the information on the console
    print(data1, '\n')





