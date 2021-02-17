import sys
import zmq
from threading import Thread
import random
import time
import publisher
import subscriber
import listener

#initializing the individual pubs, sub, and listener
def main():

	s1 = subscriber('MSFT', True)
	s1.start()

	s2 = subscriber('AAPL', True)
	s2.start()

	s3 = subscriber('IBM', True)
	s3.start()

	p1 = publisher(1, True)
	p1.start()

	p2 = publisher(2, True)
	p2.start()

	p3 = publisher(3, True)
	p3.start()

	l1 = listener(True)
	l1.start()

	p3.leave()

if __name__ == "__main__":
    main()