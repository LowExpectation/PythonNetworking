# TCP from the server side application

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverPort = 12000
serverSocket = s  # socket(AF_INET, SOCK_STREAM)
# We explicitly set the server port number for this socket
serverSocket.bind(("", serverPort))
# Increase this to allow for more connections to be made in parallel
serverSocket.listen(1)
print("The server is ready to receive")
# Server is up and waiting for connection requests
while True:
    # A new socket is created for the client 1 to 1 handshake
    connectionSocket, addr = serverSocket.accept()
    # Receives the client data
    sentence = connectionSocket.recv(1024).decode()
    # Transforms the data. We can make our translations here to see on client side
    capitalizedSentence = sentence.upper()
    # Send the tranlated data back to the client
    connectionSocket.send(capitalizedSentence.encode())
    # This closes the connection FIN, ACK or FIN
    # We could probably enhance to allow for a longer conversation
    connectionSocket.close()
