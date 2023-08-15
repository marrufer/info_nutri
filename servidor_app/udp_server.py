
import socketserver
from modelo_server import Ac
objeto_base=Ac()
global PORT


class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        
        data = self.request[0].strip()
        socket = self.request[1]
        datos=data.decode("UTF-8")
        objeto_base.alta_servidor(datos)
        
        value2 = "Alta recibida"
        value3=value2.encode()
        
        socket.sendto(value3, self.client_address)
        
      


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()