import sys
import zmq
from threading import Thread
import random
import time

class subscriber(Thread):

	def __init__(self, topic):
		super().__init__()
		self.topic = topic

	def run(self):
		print('starting sub ' + self.topic)
		context = zmq.Context()
		sub = context.socket(zmq.SUB)
		for i in range(1,6):
			port = str(5558 + i)
			sub.connect("tcp://127.0.0.1:" + port)
			sub.setsockopt_string(zmq.SUBSCRIBE, self.topic)
		self.joined = True
		while self.joined:
			string = sub.recv()
			topic, messagedata = string.split()
			print (topic, messagedata)

	def leave(self):
		self.joined = False
		print('sub ' + self.topic + ' leaving')

class publisher(Thread):

	def __init__(self, id):
		super().__init__()
		self.id = id

	def run(self):
		print('starting publisher number ' + str(self.id))
		context = zmq.Context()
		pub = context.socket(zmq.PUB)
		pub.bind("tcp://127.0.0.1:" + str(5558 + self.id))
		self.joined = True
		while self.joined:
			#select a stock
			stock_list = ["GOOG", "AAPL", "MSFT", "IBM", "AMD", "CLII", "EXO", "NFLX", "CME", "CKA"]
			index = random.randrange(1,10)
			ticker = stock_list[index]
			#generate a random price
			price = str(random.randrange(20, 60))
			#send ticker + price to broker
			pub.send_string("%s %s" % (ticker, price))
			time.sleep(1)

	def leave(self):
		self.joined = False
		print('pub leaving')

def main():

	s1 = subscriber('MSFT')
	s1.start()

	s2 = subscriber('AAPL')
	s2.start()

	s3 = subscriber('IBM')
	s3.start()

	p1 = publisher(1)
	p1.start()

	p2 = publisher(2)
	p2.start()

	p3 = publisher(3)
	p3.start()

if __name__ == "__main__":
    main()

