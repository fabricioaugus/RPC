import xmlrpc.client
if __name__== "__main__":
    proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
    numero = int(input("Informe um inteiro para que será sequencia de fibonacci: "))
    for x in range(1,(numero+1)):
        res = proxy.fibonacci(x)
        print(f"numero é:  {x} e seu valor é : {res}")
