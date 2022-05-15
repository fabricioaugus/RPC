import xmlrpc.client
if __name__== "__main__":
    # Uma ServerProxy instância possui um método correspondente a cada chamada de procedimento remoto
    #  aceita pelo servidor XML-RPC. Chamar o método executa um RPC, despachado por nome e assinatura
    #  de argumento (por exemplo, o mesmo nome de método pode ser sobrecarregado com várias assinaturas
    #  de argumento).
    proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
    numero = int(input("Informe um inteiro para que será sequencia de fibonacci: "))
    for x in range(1,(numero+1)):
        res = proxy.fibonacci(x)
        print(f"numero é:  {x} e seu valor é : {res}")
