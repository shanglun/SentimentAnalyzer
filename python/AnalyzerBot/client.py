from sentiment import SentimentAnalysisService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class SentimentClient:
    def __init__(self, server='localhost', socket=9090):
        transport = TSocket.TSocket(server, socket)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.transport = transport
        self.client = SentimentAnalysisService.Client(protocol)
        self.transport.open()

    def __del__(self):
        self.transport.close()

    def analyze(self, sentence):
        return self.client.sentimentAnalyze(sentence)

if __name__ == '__main__':
    client = SentimentClient()
    print(client.analyze('Hello'))
