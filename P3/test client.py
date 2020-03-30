from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

# Configure the client
c = Client(IP, PORT)
print(c)


print("* Testing PING...")
print(c.talk("PING"))


print("* Testing GET...")
for i in range(5):
    cmd = f"GET {i}"
    print(f"{cmd}: {c.talk(cmd)}", end="")


# Sequence 0 for testing
seq = c.talk("GET 0")
print()
print("* Testing INFO...")
cmd = f"INFO {seq}"
print(c.talk(cmd))


print("* Testing COMP...")
cmd = f"COMP {seq}"
print(cmd, end="")
print(c.talk(cmd))


print("* Testing REV...")
cmd = f"REV {seq}"
print(cmd, end="")
print(c.talk(cmd))


print("* Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    cmd = f"GENE {gene}"
    print(cmd)
    print(c.talk(cmd))