# We are executing these samples on a Mininet-emulated environment
#
#
#   Weather update server
#   Binds PUB socket to tcp://*:5556
#   Publishes random stock prices
#

import zmq
from random import randrange

context = zmq.Context()

# The difference here is that this is a publisher and its aim in life is
# to just publish some value. The binding is as before.

socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:2000")

# keeps publishing
stock_list = ["GOOG", "AAPL", "MSFT", "IBM", "AMD", "CLII", "EXO", "NFLX", "CME", "CKA"]

#select a random stock ticker, assign a random positive price to it
while True:
    index = randrange(0, len(stock_list))
    #ticker = stock_list[index]
    ticker = "MSFT"
    price = randrange(20, 60)

    socket.send_string("%s %i" % (ticker, price))
