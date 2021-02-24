import sys
import zmq
from threading import Thread
import datetime
import os
import random
import time

class subscriber(Thread):

	def __init__(self, topic, flood):
		super().__init__()
		self.topic = topic
		self.flood = flood
		self.joined = True

	def run(self):
		print('starting sub ' + self.topic)
		context = zmq.Context()
		sub = context.socket(zmq.SUB)
		if self.flood == True:
			for i in range(1,6):
				port = str(5558 + i)
				sub.connect("tcp://127.0.0.1:" + port)
				sub.setsockopt_string(zmq.SUBSCRIBE, self.topic)
		else:
			sub.connect("tcp://127.0.0.1:5559")
			sub.setsockopt_string(zmq.SUBSCRIBE, self.topic)
		while self.joined:
			string = sub.recv_string()
			ticker, price, time = string.split()

			time_received = (datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds()
			latency = time_received - float(time)
			print(ticker, price, latency, 'ms')
			with open("latency_{}.txt".format(ticker), "a") as f:
				f.write(str(latency) + "\n")

	def leave(self):
		self.joined = False
		print('sub ' + self.topic + ' leaving')

def main():
	ticker = sys.argv[0]
	method = sys.argv[1]

	sub = subscriber(ticker, method)
	while True:
		sub.run()
		time.sleep(1)

if __name__=='__main__':
	main()