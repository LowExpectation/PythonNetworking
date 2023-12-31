import random

from .BasicTest import *

"""
This tests random packet duplications. We randomly decide to duplicate about 
half of the packets that go through the forwarder in either direction. The 
number of the extra packets sent is randomly chosen between 1 and 3. The "true"
case is for when the duplication occurs, and "false" is otherwise.

Note that to implement this we just needed to override the handle_packet()
method -- this gives you an example of how to extend the basic test case to
create your own.
"""
class RandomDuplicateTest(BasicTest):

    def handle_packet(self):
        for p in self.forwarder.in_queue:
            if random.choice([True, False]):
                self.forwarder.out_queue.append(p)

            self.forwarder.out_queue.append(p)

        # empty out the in_queue
        self.forwarder.in_queue = []