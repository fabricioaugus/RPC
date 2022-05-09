import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:6789/") 
numero = int(input("Informe um inteiro: "))
for x in range(2,numero):
    res = proxy.fibonacci(x)
    print(f"valor do numero {x} o valor {res}")

