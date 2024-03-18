# import OS module to fetch the command line arguments
# url_parse.py

import os
import sys
from urllib.parse import urlparse

print("Testing")


# function definition to parse url and store in file
def url_parser(param_url, filename):
    # parse the url using urlparse from the standard Python library
    # you can obtain the following attributes from url_parsed
    # param_url = 'http://www.eller.arizona.edu:2016/index.html'
    # url_parsed.hostname: Hostname = 'www.eller.arizona.edu'
    # url_parsed.port: port number = 2016
    # url_parsed.path: path of the file = '/index.html'
    # check out the full document of the urlparse module at https://docs.python.org/3.10/library/urllib.parse.html

    # Write your code here
    # obtain the attributes: host,port and path from the urlparsed
    url_parsed_list = []
    url_parsed = urlparse(param_url)
    url_parsed_list.append("url: {}".format(param_url))
    url_parsed_list.append("host: {}".format(url_parsed.netloc))
    url_parsed_list.append("path: {}".format(url_parsed.path))
    # handle the port requirement for type None
    if url_parsed.port == None:
        url_parsed_list.append("port: {}".format("80"))
    else:
        url_parsed_list.append("port: {}".format(str(url_parsed.port)))

    # Write your code here
    # Open the file (filename from function parameter)
    # write the url, host, port and path to file
    output_file_and_path = os.path.join(os.getcwd(), filename)
    output_file = open(output_file_and_path, "w")
    
    # loop and split the integers into file lines
    for attribute in url_parsed_list:
        output_file.write("{}\n".format(str(attribute))) 
            
    # Close and the file for editing
    output_file.close()

    # return the filename
    return output_file_and_path


# obtain the command line parameters for url and filename
url = sys.argv[1]
file2save = sys.argv[2]

# function call to parse the url and store in file
stored_file = url_parser(url, file2save)

# display the filename which contains the parsed attributes of the url
print(f"The parsed attributes are stored in: {stored_file}")
