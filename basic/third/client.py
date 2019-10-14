#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Пример клиента на Twisted
#
from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver


class Client(LineOnlyReceiver):
    def connectionMade(self):
        self.sendLine("login:admin".encode())

    def lineReceived(self, line):
        print(line)


class Connector(ClientFactory):
    protocol = Client


reactor.connectTCP("localhost", 7410, Connector())
reactor.run()
