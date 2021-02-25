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
			topic, price, time_started = string.split()

			#time_received = (datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds()
			#time_received = (datetime.datetime.now().strftime("%H:%M:%S.%f"))
			time_received = (datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds()
			latency = format((1000*(float(time_received) - float(time_started))), '.5f')
			print(topic, price, latency, 'ms')
			with open("./results/latency_{}.csv".format(topic), "a") as f:
				f.write(str(latency) + "\n")

	def leave(self):
		self.joined = False
		print('sub ' + self.topic + ' leaving')

def main():
	topic = sys.argv[1]
	method = sys.argv[2]

	if not str(topic) or len(topic) != 4:
		print("Invalid Stock Ticker")
		sys.exit(-1)

	#Should try to check whether method is boolean

	sub = subscriber(topic, method)
	sub.start()
	#while True:
		#sub.start()
		#time.sleep(1)

if __name__=='__main__':
	main()