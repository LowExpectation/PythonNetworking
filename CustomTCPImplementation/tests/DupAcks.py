import random

from .BasicTest import *

"""
This test sends too many dupacks. Sometimes it will drop all of the packets in the queue.
"""
class DupAcks(BasicTest):
    def handle_packet(self):
        for p in self.forwarder.in_queue:
            if random.randint(0,1):
                for i in range(3):
                    self.forwarder.out_queue.append(p)
            else:
                self.forwarder.out_queue.append(p)

        # empty out the in_queue
        self.forwarder.in_queue = []