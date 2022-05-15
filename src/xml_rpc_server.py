# 
from xmlrpc.server import SimpleXMLRPCServer
def fibonacci(num):
  if num <= 0:
    print("Não é possível obter o fibonacci de um numero negativo.")
  elif num == 1:
    return 0
  elif ((num == 2) or (num == 3)):
    return 1
  else:
    return fibonacci(num - 1) + fibonacci(num - 2)



if __name__== "__main__":
  # Cria uma nova instância do servidor. 
  # Esta classe fornece métodos para registro de funções que podem 
  # ser chamadas pelo protocolo XML-RPC. SimpleXMLRPCServer
  server = SimpleXMLRPCServer(( "localhost" , 6789))
  server.register_function(fibonacci,"fibonacci")
  server.serve_forever()
