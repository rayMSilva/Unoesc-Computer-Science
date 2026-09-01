clientes = [] * 10
codigo = 1
while True:
    cliente = []
    nome = str(input("Informe o nome do cliente: "))
    print("----- Nome Registrado -----")
    cliente.append(codigo)
    codigo += 1
    cliente.append(nome)
    clientes.append(cliente)
    if codigo <= 10:
        sair = int(input("Deseja sair?\n1.Sim\n0.Não\nResposta: "))
        if sair:
            break
    else:
        break
print(f"\nCódigo          Nome")
for i in range(len(clientes)):
    print(f"{clientes[i][0]}               {clientes[i][1]}")