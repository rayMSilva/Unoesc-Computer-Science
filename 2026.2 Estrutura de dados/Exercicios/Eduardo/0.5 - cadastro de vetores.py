#FUNÇÕES
def cadastrarVetor(V, N):
    for posicao in range(N):
        V[posicao] = int(input(f"Informe o valor do vetor[{posicao}]: "))

def mostrarVetor(V, N):
    for posicao in range(N):
        print(f"V[{posicao}] = {V[posicao]}")

def alterarVetor(V, N, procurado, novo, qtdeAlterF):
    for posicao in range(N):
        if V[posicao] == procurado:
            V[posicao] = novo
            qtdeAlterF += 1
    return qtdeAlterF
#DEFINIÇÃO DAS VARIÁVEIS
N = 10
V = [0] * 10
qtdeAlter = 0
cadastrado = 0


#FUNÇÃO PRINCIPAL DO SISTEMA
def __main__(N, V, qtdeAlter, cadastrado):
    
    selecao = int(input("\n| Informe qual ação deseja realizar |\n  1.Cadastrar um novo valor\n  2.Mostrar os valores atuais\n  3.Alterar os valores atuais\n\nResposta: "))
    if selecao == 1:
        if cadastrado == 0:
            cadastrarVetor(V, N)
            cadastrado = 1
        else:
            print("Listagem já cadastrada! Não é possível realizar esta ação novamente.")
            __main__(N, V, qtdeAlter, cadastrado)
    elif selecao == 2:
        mostrarVetor(V, N)
    elif selecao == 3:
        if cadastrado == 1:
            procurado = int(input("\nInforme qual valor gostaria de alterar: "))
            print("--------- Informação aceita ---------")
            novo = int(input("\nInforme o novo número: "))
            qtdeAlter = alterarVetor(V, N, procurado, novo, qtdeAlter)
            if qtdeAlter == 0:
                print("\nNúmero informado não foi encotrado, por favor verifique.")
            elif qtdeAlter == 1:
                print(f"\nSucesso! A informação desejada foi alterada")
            else:
                print(f"\nSucesso! Foram alteradas {qtdeAlter} informações")
        else:
            print("\nNão é possível realizar uma alteração. Informações não foram cadastradas.")
    else:
        print(f"\nO valor [{selecao}] não é o esperado!")
    __main__(N, V, qtdeAlter, cadastrado)
__main__(N, V, qtdeAlter, cadastrado)
