import socket
import sys


# Create socket (allows 2 computers to connect)

def socket_create():
    try:
        global host
        global port
        global s

        host = ""
        port = 9997
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error." + str(msg))

# Bind the socket to the port and wait for connection to the client.


def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))

        # Listen in the own machine on port 9999
        s.bind((host, port))
        # Begin accepting connections, the numbers specifies how many connections to accept
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\nRetrying...")
        socket_bind()

# Accept connection with client (socket must be listening!)


def socket_accept():
    conn, address = s.accept()
    # conn is the connection itself
    # address is the information about who is connected.
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        # Gather input from the terminal
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        # encode will convert from str to byte, so that the terminal can read it.
        # Only send if there is actual data, not a simple \n
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")

            # print without the newline
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
