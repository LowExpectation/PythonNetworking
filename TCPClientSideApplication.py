# TCP client side application
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverName = "servername"
serverPort = 12000
# Here we see that SOCK_STREAM shows we are using TCP instead of UDP
clientSocket = s  # socket(AF_INET, SOCK_STREAM)
# This allows for a handshake to be requested from prospective servers
clientSocket.connect((serverName, serverPort))
# This is the payload data in the segement
sentence = input("Input lowercase sentence then press enter:")
sentence = sentence.lower() + "/r"
# The data is simply dropped into the created connect socket
# We dont need to imply addresses or ports like UDP
clientSocket.send(sentence.encode())
# This handles response from the server side
# We should see our translations show up here from server side
modifiedSentence = clientSocket.recv(1024)
print("From Server: ", modifiedSentence.decode())
# This guy will send the FIN or FIN, ACK request
clientSocket.close()
