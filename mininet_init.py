#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
import time

class SingleSwitchTopo(Topo):
	# "Single switch connected to n hosts."
	def __init__(self, n=2, **opts):

		# Initialize topology and default options
		Topo.__init__(self, **opts)
		switch = self.addSwitch('s1')

		# Python's range(N) generates 0...N-1
		for h in range(n):
			host = self.addHost('h%s'%(h+1))
		self.addLink(host, switch)

def exampleBrokerTest():
	#"Create and test a simple network"
	topo = SingleSwitchTopo(n=4)
	net = Mininet(topo)
	net.start()
	print("Dumping host connections")
	dumpNodeConnections(net.hosts)
	print("Testing network connectivity")
	net.pingAll()
	net.stop()

def simpleTest():
	topo = Topo()  # Create an empty topology
	topo.addSwitch("s1")  # Add switches and hosts to the topology
	topo.addHost("h1")
	topo.addHost("h2")
	topo.addLink("h1", "s1")  # Wire the switches and hosts together with links
	topo.addLink("h2", "s1")
	net = Mininet(topo)  # Create the Mininet, start it and try some stuff
	net.start()
	net.pingAll()
	net.iperf()
	net.stop()

def simpleBrokerTest():
	#"Create and test a simple network"
	#topo = SingleSwitchTopo(n=4)
	#net = Mininet(topo)

	topo = Topo()
	topo.addSwitch("s1")  # Add switches and hosts to the topology
	topo.addHost("h1")
	topo.addHost("h2")
	topo.addHost("h3")
	topo.addHost("h4")
	topo.addLink("h1", "s1")  # Wire the switches and hosts together with links
	topo.addLink("h2", "s1")
	topo.addLink("h3", "s1")
	topo.addLink("h4", "s1")
	net = Mininet(topo)  # Create the Mininet, start it and try some stuff
	net.start()

	print("Starting host connections")
	#dumpNodeConnections(net.hosts)

	#Set the IPs for each of the hosts
	h1 = net.get('h1')
	result1 = h1.cmd('python3 ./middleware/broker.py')
	print(result1)
	print("Host", h1.name, "has IP address", h1.IP())

	#h1.sendCmd('python3 ./middleware/broker.py')

	h2 = net.get('h2')
	h2.cmd('python3 ./middleware/subscriber.py MSFT True')
	print("Host", h2.name, "has IP address", h2.IP())

	h3 = net.get('h3')
	h3.cmd('python3 ./middleware/listener.py True')
	print("Host", h3.name, "has IP address", h3.IP())

	h4 = net.get('h4')
	h4.cmd('python3 ./middleware/publisher.py 1 MSFT True')
	print("Host", h4.name, "has IP address", h4.IP())

	time.sleep(5)
	net.stop()

def complexBrokerTest():
	#"Create and test a simple network"
	topo = SingleSwitchTopo(n=4)
	net = Mininet(topo)
	net.start()
	print("Dumping host connections")
	dumpNodeConnections(net.hosts)
	print("Testing network connectivity")
	net.pingAll()
	net.stop()

def simpleFloodTest():
	#"Create and test a simple network"
	topo = SingleSwitchTopo(n=4)
	net = Mininet(topo)
	net.start()
	print("Dumping host connections")
	dumpNodeConnections(net.hosts)
	print("Testing network connectivity")
	net.pingAll()
	net.stop()

def complexFloodTest():
	#"Create and test a simple network"
	topo = SingleSwitchTopo(n=4)
	net = Mininet(topo)
	net.start()
	print("Dumping host connections")
	dumpNodeConnections(net.hosts)
	print("Testing network connectivity")
	net.pingAll()
	net.stop()

if __name__=='__main__':
	# Tell mininet to print useful information
	setLogLevel('info')
	simpleBrokerTest()