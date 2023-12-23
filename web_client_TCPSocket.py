import sys
from urllib.parse import urlparse
from socket import *

# Get entries from command line
# These can be replaced with any input method
param_url = sys.argv[1]
param_file = sys.argv[2]

# We pass the user entered url and allow it to be parsed
# validation of user input could also be done if needed
url_parsed = urlparse(param_url)

# We setup TCP "SOCK_STEAM" socket
s = socket(AF_INET, SOCK_STREAM)

# 1. construct the IP address and port number
if url_parsed.port == None:
    port = 80
else:
    pass

# 2. Create the http get request manually
http_GET = f"GET {url_parsed.path} HTTP/1.1\r\nHost: {url_parsed.hostname}\r\n\r\n"
# Leaving the below format for readability
# http_GET = 'GET ' + url_parsed.path + ' HTTP/1.1\r\n' + \
#     'Host: ' + url_parsed.hostname + '\r\n\r\n'

# print the http GET request to check the output formating
print(http_GET)

# 3. Connect to destination and read the response given
s.connect((url_parsed.hostname, port))
s.send(http_GET.encode())

# Create a bytes variable and get response
response = b""
resp = s.recv(1024)
# We want to make sure we get to the end of the stream with an empty byte
while not resp == b"":
    print(resp.decode())
    response += resp
    resp = s.recv(1024)
    
# 4. Save the http response to file from command line input
# We split the byte response into header and body values
[header, body] = response.split(b"\r\n\r\n")
# We will now split the header and get all lines from the header split
resp_line = header.decode().split("\r\n")[0]

# allows us to see the body of the document
print(body.decode())

# Create a file based on the output
with open(param_file, 'wb') as f:
    # only create body record if response is healthy like 200 OK
    if '200 OK' in resp_line:
        f.write(body)
    # We will write the header line as the body if not usable
    else:
        f.write(resp_line.encode())

# Close and notify user of completion 
s.close()

print("\nFinished Downloading")