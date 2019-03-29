import socket
import time
import pickle


# AF_INET, stands for IPv4 type
# SOCK_STREAM, stands for TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HEADERSIZE = 10

# socket.gethostname() gets the host of this current machine.
# 1234 is the port number
s.bind((socket.gethostname(), 1235))

s.listen(5)
try:
	while True:
		clientsocket, address = s.accept()
		print(f"Connection from {address} has been established.")

		# Dictionary to send
		d = {1: "Hey", 2: "There"}
		# Pickle up the msg
		msg = pickle.dumps(d)


		msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

		clientsocket.send(msg)
		# s.close()

		while True:
			# 3 seconds
			time.sleep(3)
			d = f"The time is {time.time()}"
			msg = pickle.dumps(d)

			msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

			clientsocket.send(msg)

except:
	clientsocket.close()
