import socket
import termcolor
from pathlib import Path



IP = "127.0.0.1"
PORT = 8080


def get_resource(path):
    response = ""

    if path == "/info/A":
        response = Path("A.html").read_text()
    elif path == "/info/C":
        resp = Path("C.html").read_text()

    return response


def process_client(n):

    request_raw = n.recv(2000)
    request = request_raw.decode()

    print("Message FROM CLIENT: ")

    lines = request.split('\n')


    request_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(request_line, "green")


    words = request_line.split(' ')


    method = words[0]
    path = words[1]

    print(f"Method: {method}")
    print(f"Path: {path}")


    response_body = ""

    if method == "GET":
        response_body = get_resource(path)

    status_line = "HTTP/1.1 200 OK\n"

    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(response_body)}\n"
    response_message = status_line + header + "\r\n" + response_body
    client_socket.send(response_message.encode())



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen()

print("SEQ Server configured!")


while True:
    print("Waiting for clients....")
    try:
        (client_socket, client_ip_port) = s.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        s.close()
        exit()
    else:
        process_client(client_socket)
        client_socket.close()
