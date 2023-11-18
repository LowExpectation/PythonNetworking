# UDP Server side UDP application response

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverPort = 12000
serverSocket = s  # socket(AF_INET, SOCK_DGRAM)
# The UDP protocol for port 12000 is being bound to this socket explicitly
serverSocket.bind(("", serverPort))
print("The server is ready to receive")
# The while loop allow for the UDP packets to be processed without stopping
while True:
    # The socket data is split into the payload and client information from buffer
    message, clientAddress = serverSocket.recvfrom(2048)
    # This will allow for the payload to converted to string and make upper case
    modifiedMessage = message.decode().upper()
    # The server will capitalize the data and sent back to the client
    # Here is where you can modify and add messages back to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
