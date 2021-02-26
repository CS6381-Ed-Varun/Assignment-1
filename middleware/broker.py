import sys
import zmq
from threading import Thread
import random
import time

def main():
    context = zmq.Context()

    # pub side
    frontend = context.socket(zmq.XPUB)
    frontend.bind("tcp://10.0.0.1:5559")

    # sub side
    backend = context.socket(zmq.XSUB)
    backend.bind("tcp://10.0.0.1:5560")

    zmq.device(zmq.FORWARDER, frontend, backend)

if __name__ == "__main__":
    main()