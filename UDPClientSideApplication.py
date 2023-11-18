# UDP Client Side application

# Import module for networking functions

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Add IP Address or Hostname with implied DNS lookup
serverName = "hostname"
# Specify the port number on server side
serverPort = 12000
# Dynamic client socket creation
# AF_INET is the IPV4, SOCK_DGRAM is the UDP transport method
# Port number will be auto assigned on client side
clientSocket = s  # socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence and press enter:")
message = message.lower() + "/r"
# Convert message from string to byte format
# sendto creates the datagram with message, IP address, and port
clientSocket.sendto(message.encode(), (serverName, serverPort))
# The socket message is put into modifiedMessage
# The servername and port are put into the serverAddress
# recvfrom is setting a static buffer size on the server side
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# Print a string version of the message
print(modifiedMessage.decode())
# Close the output
clientSocket.close()
