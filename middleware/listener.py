import sys
import zmq
from threading import Thread
import random
import time

class listener(Thread):

    # init self
    def __init__(self, flood):
        super().__init__()
        self.flood = flood
        self.joined = True

    # start up the thread
    def run(self):
        print("starting listener thread")
        context = zmq.Context()
        sub = context.socket(zmq.SUB)
        #print('Flood variable is ' + self.flood)
        # Flooding version - connect to all pub networks w/o a filter
        if self.flood != True:
            #print('Flooding Approach is being monitored')
            for i in range(1, 8):
                port = str(5558 + i)
                sub.connect("tcp://10.0.0." + str(i) + ":" + port)
                sub.setsockopt_string(zmq.SUBSCRIBE, "")
        # Broker version - connect w/o filtering
        else:
            print('Broker Approach is being monitored')
            sub.connect("tcp://10.0.0.1:5559")
            sub.setsockopt_string(zmq.SUBSCRIBE, "")
        # make a list of messages and appended to it each time one arrives
        messages = []
        while self.joined:
            string = sub.recv()
            messages.append(messages)
            if (len(messages) % 10 == 0):
                print(str(len(messages)) + " messages sent by brokers")

def main():
    method = sys.argv[1]

    lis = listener(method)
    lis.start()
    #while True:
        #lis.start()

if __name__=='__main__':
    main()