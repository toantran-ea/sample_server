
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    def dataReceived(self, data):
        print "dataReceived >> " + data
        for c in self.factory.clients:
            c.message(data)

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