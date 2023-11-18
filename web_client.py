# Simple HTTP Client handling
# web_client.py
# https://docs.python.org/3.11/library/urllib.request.html

import os, sys, urllib.request

# Parse the initial URL
url = sys.argv[1]

# Create file name
filename = sys.argv[2]

try:
    # Write the file to current working directory
    filename, headers = urllib.request.urlretrieve(
        url, os.path.join(os.getcwd(), filename)
    )
except urllib.error.HTTPError as http_error:
    # Write a file that contains the non handled 404 etc
    with open(os.path.join(os.getcwd(), filename), "w") as file:
        file.write(str(f"The URL returned: {http_error.code}, {http_error.reason}."))
        filename = os.path.join(os.getcwd(), filename)

# Write the output file name to stdout
print("\nFinishing downloading ...")
print(f"File created at {filename}")
