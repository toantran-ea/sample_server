
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol
from threading import Thread
from time import sleep
from message_handler import MessageHandler

class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    def __init__(self):
        self.message_handler = MessageHandler()

    def dataReceived(self, data):
        message = self.message_handler.handle(data)
        for c in self.factory.clients:
            c.message(message)

    def connectionMade(self):
        self.factory.clients.append(self)
        print "clients are ", self.factory.clients

    def connectionLost(self, reason="aaaa"):
        print "client disconnected >>>>>>"
        self.factory.clients.remove(self) 

    def message(self, message):
        self.transport.write(message + '\n')

def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    factory.clients = []
    reactor.listenTCP(1212,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()