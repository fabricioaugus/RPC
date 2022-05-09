from xmlrpc.server import SimpleXMLRPCServer
def fibonacci(num):
  if num < 0:
    print("Não é possível obter o fibonacci de um numero negativo.")
  if ((num == 0) or (num == 1)):
    return num
  else:
    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__== "__main__":
  server = SimpleXMLRPCServer(( "localhost" , 6789))
  server.register_function(fibonacci,"fibonacci")
  server.serve_forever()
