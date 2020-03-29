import socket
import termcolor



IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Generate the response message
    # body
    body = "Hello from my first web server!\n"

    # Status line
    status_line = "HTTP/1.1 200 OK\n"

    # Content-Type header
    header = "Content-Type: text/plain\n"

    # Content-Length
    header += f"Content-Length: {len(body)}\n"

    # Build the message
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())



ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))


ls.listen()

print("SEQ Server configured!")


while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()