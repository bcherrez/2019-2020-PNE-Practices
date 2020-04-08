from Client0 import Client


PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

# Configure the client
clnt = Client(IP, PORT)
print(clnt)


print("* Testing PING...")
print(clnt.talk("PING"))


print("* Testing GET...")
for i in range(5):
    comand = f"GET {i}"
    print(f"{comand}: {clnt.talk(comand)}", end="")


# Sequence 0 for testing
seq = clnt.talk("GET 0")
print()
print("* Testing INFO...")
comand = f"INFO {seq}"
print(c.talk(comand))


print("* Testing COMP...")
comand = f"COMP {seq}"
print(comand, end="")
print(clnt.talk(comand))


print("* Testing REV...")
comand = f"REV {seq}"
print(comand, end="")
print(clnt.talk(comand))


print("* Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    comand = f"GENE {gene}"
    print(comand)
    print(clnt.talk(comand))