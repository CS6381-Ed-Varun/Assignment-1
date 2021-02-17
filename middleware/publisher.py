class publisher(Thread):

	def __init__(self, id, flood):
		super().__init__()
		self.id = id
		self.flood = flood
		self.joined = True

	def run(self):
		print('starting publisher number ' + str(self.id))
		context = zmq.Context()
		pub = context.socket(zmq.PUB)
		if self.flood == True:
			pub.bind("tcp://127.0.0.1:" + str(5558 + self.id))
		else:
			pub.connect("tcp://127.0.0.1:5560")
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