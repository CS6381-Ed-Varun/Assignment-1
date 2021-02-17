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
			string = sub.recv()
			topic, messagedata = string.split()
			print (topic, messagedata)

	def leave(self):
		self.joined = False
		print('sub ' + self.topic + ' leaving')