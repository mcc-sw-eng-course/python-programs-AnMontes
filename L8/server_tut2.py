import socket
import time

# AF_INET, stands for IPv4 type
# SOCK_STREAM, stands for TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HEADERSIZE = 10

# socket.gethostname() gets the host of this current machine.
# 1234 is the port number
s.bind((socket.gethostname(), 1234))

s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established.")

	msg = "Welcome to the server!"
	msg = f"{len(msg):<{HEADERSIZE}}" + msg

	clientsocket.send(bytes(msg, "utf-8"))
	# s.close()

	while True:
		# 3 seconds
		time.sleep(3)
		msg = f"The time is {time.time()}"
		msg = f"{len(msg):<{HEADERSIZE}}" + msg

		clientsocket.send(bytes(msg, "utf-8"))
