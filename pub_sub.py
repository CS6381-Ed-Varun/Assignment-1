import sys
import zmq
from threading import Thread
import random
import time

class subscriber(Thread):

	def __init__(self, topic, flood):
		super().__init__()
		self.topic = topic
		self.flood = flood

	def run(self):
		print('starting sub ' + self.topic)
		context = zmq.Context()
		sub = context.socket(zmq.SUB)
		if self.flood == True:
			for i in range(1,6):
				port = str(5558 + i)
				sub.connect("tcp://*:" + port)
				sub.setsockopt_string(zmq.SUBSCRIBE, self.topic)
		else:
			sub.connect("tcp://*:5559")
		self.joined = True
		while self.joined:
			string = sub.recv()
			topic, messagedata = string.split()
			print (topic, messagedata)

	def leave(self):
		self.joined = False
		print('sub ' + self.topic + ' leaving')

class publisher(Thread):

	def __init__(self, id, flood):
		super().__init__()
		self.id = id
		self.flood = flood

	def run(self):
		print('starting publisher number ' + str(self.id))
		context = zmq.Context()
		pub = context.socket(zmq.PUB)
		if self.flood == True:
			pub.bind("tcp://*:" + str(5558 + self.id))
		else:
			pub.connect("tcp://*:5560")
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

if __name__ == "__main__":
    main()

