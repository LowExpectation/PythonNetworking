import sys
import getopt
import time
import random
import os
import math

import Checksum
import BasicSender

'''
This is a skeleton sender class. Create a fantastic transport protocol here.
'''
class Sender(BasicSender.BasicSender):
    def __init__(self, dest, port, filename, debug=False):
        super(Sender, self).__init__(dest, port, filename, debug)
        
    def handle_response(self,response_packet):
        if Checksum.validate_checksum(response_packet):
            print("recv: %s" % response_packet)
        else:
            print("recv: %s <--- CHECKSUM FAILED" % response_packet)

    # Main sending loop.
    def start(self):
        seqno = 0
        msg = self.infile.read(1000).decode() # from 500
        msg_type = None
        while not msg_type == 'end':
            next_msg = self.infile.read(1000).decode() # from 500

            msg_type = 'data'
            if seqno == 0:
                msg_type = 'start'
            elif next_msg == "":
                msg_type = 'end'

            packet = self.make_packet(msg_type,seqno,msg)
            self.send(packet.encode())
            print("sent: %s" % packet)
            
            # 500 bytes stock was changes to 1000 in the start method
            # time out set for .5 seconds for response
            # delay testing was done with assumption of 1 second maxiumum
            response = self.receive(0.5)
            
            # 4 delay for missing response
            if response == None:
                time.sleep(1.0)
                response = self.receive(0.5)
            # 1. loss # 2. corruption checking
                counter = 1       
                while response == None or Checksum.validate_checksum(response.decode()) == False:
                    print(f"\npacket(s) lost or corrupted: {counter}")
                    # 4. delay for missing response
                    print("\nwaiting for packet...")
                    time.sleep(1.0)          
                    self.send(packet.encode())
                    response = self.receive(0.5)
                    counter += 1        
            
            # 3. duplication or corruption of AKS
            ACKType, ACKNumber, data, checksum = self.split_packet(response.decode())
            counter = 1
            while not int(ACKNumber) == seqno + 1:
                print(f"ack number duplicated or incorrect. Number of retries: {counter}")
                # keep sending and receiving until ack number is correct expected
                self.send(packet.encode())
                response = self.receive(0.5) 
                ACKType, ACKNumber, data, checksum = self.split_packet(response.decode())
                counter += 1
            
            resp_str = response.decode()
              
            # validate the checksum
            self.handle_response(resp_str)
            msg = next_msg
            seqno += 1

        self.infile.close()
 

'''
This will be run if you run this script from the command line. You should not
change any of this; the grader may rely on the behavior here to test your
submission.
'''
if __name__ == "__main__":
    def usage():
        print("BEARDOWN-TP Sender")
        print("-f FILE | --file=FILE The file to transfer; if empty reads from STDIN")
        print("-p PORT | --port=PORT The destination port, defaults to 33122")
        print("-a ADDRESS | --address=ADDRESS The receiver address or hostname, defaults to localhost")
        print("-d | --debug Print debug messages")
        print("-h | --help Print this usage message")

    try:
        opts, args = getopt.getopt(sys.argv[1:],
                               "f:p:a:d", ["file=", "port=", "address=", "debug="])
    except:
        usage()
        exit()

    port = 33122
    dest = "localhost"
    filename = None
    debug = False

    for o,a in opts:
        if o in ("-f", "--file="):
            filename = a
        elif o in ("-p", "--port="):
            port = int(a)
        elif o in ("-a", "--address="):
            dest = a
        elif o in ("-d", "--debug="):
            debug = True

    s = Sender(dest,port,filename,debug)
    try:
        s.start()
    except (KeyboardInterrupt, SystemExit):
        exit()
