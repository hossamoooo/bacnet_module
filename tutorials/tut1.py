#!/usr/bin/python

import sys

from bacpypes.comm import Client, Server, bind, Debug, PDU

class MyServer(Server):
	def indication(self, arg):
		print "working on", arg
		self.response(arg.upper())

class MyClient(Client):
	def confirmation(self, pdu):
		print "thanks for the", pdu

def main():
	print "test start"
	s = MyServer()
	c = MyClient()
	d = Debug("packet")
	bind(c,d,s)
	c.request("hi")
	
	pdu = PDU("hello", source = 1, destination = 2)
	pdu.debug_contents()

if __name__ == '__main__':
	main()
