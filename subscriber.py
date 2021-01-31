import sys
import zmq

#  Socket to talk to server
context = zmq.Context()

# Since we are the subscriber, we use the SUB type of the socket
socket = context.socket(zmq.SUB)

# Here we assume publisher runs locally unless we
# send a command line arg like 10.0.0.1
connect_str = "tcp://127.0.0.1:2000"

print("Collecting stock updates...")
socket.connect(connect_str)

# Subscribe to MSFT updates
ticker_filter = "MSFT"
socket.setsockopt_string(zmq.SUBSCRIBE, ticker_filter)

# Process 10 updates
total_price = 0
for update_nbr in range(10):
    string = socket.recv_string()
    ticker, price = string.split()
    total_price += int(price)
    print(ticker + " " + price)

print("Average price for stock '%s' was %d" % (
      ticker_filter, total_price / (update_nbr+1))
)
