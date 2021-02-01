import zmq
import random
import sys
import time

port = "5559"

context = zmq.Context()

#change to xpub when doing multiple
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:%s" % port)




while True:

	#select a stock
	stock_list = ["GOOG", "AAPL", "MSFT", "IBM", "AMD", "CLII", "EXO", "NFLX", "CME", "CKA"]
	index = random.randrange(1,10)
	ticker = stock_list[index]

	#generate a random price
	price = random.randrange(20, 60)
	print (ticker + " " + str(price))

	#send ticker + price to broker
	socket.send_string("%s %i" % (ticker, price))
	time.sleep(1)