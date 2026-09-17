def cadastrarVetor(vetor, qtdElementos):
    for i in range(qtdElementos):
        while(True):
            try:
                vetor[i] = int(input(f"Digite o valor inteiro da posição V[{i}]:\n"))
                break
            except ValueError:
                print("valor digitado precisa ser um inteiro! Digite novamente\n")
            except Exception:
                print("erro. Digite novamente\n")
    
def mostrarVetor(vetor, elementos):
    for i in range(elementos):
        print(f"posição V[{i}]: valor {vetor[i]}" if i != elementos - 1 else f"posição V[{i}]: valor {vetor[i]}\n\n")

def AlterarVetor(vetor, elementos, procurado, novoValor):
    alteracoes = 0
    for i in range(elementos):
        if (vetor[i] == procurado):
            vetor[i] = novoValor
            alteracoes+=1
    return alteracoes


def exibirAcoes():
    print("""Operações disponpíveis para realizar com seu vetor ou CTRL + C para SAIR!!
1 - Alterar Vetor
2 - Mostrar Vetor\n""")
    

if __name__ == "__main__":
    tam = 10
    vetor = [0] * 10
    print(f"Bem vindo ao sistema de gerenciamento de vetores!")
    print(f"Para sair do sistema use CTRL + C!!\n\n")
    try:
        cadastrarVetor(vetor, tam)
        mostrarVetor(vetor, tam)
        while(True):
            exibirAcoes()
            acao = str(input("Digite a ação desejada:\n"))
            if acao == "1":
                valorProcurado = None
                while True:
                    try:
                        valorProcurado = int(input("Digite um valor inteiro que deseja procurar no vetor cadastrado!\n"))
                        break
                    except ValueError:
                        print("Valor inválido! Digite um número inteiro.\n")

                novoValor = None
                while True:
                    try:
                        novoValor = int(input("Digite um valor inteiro que deseja substituir o valor procurado no vetor cadastrado!\n"))
                        break
                    except ValueError:
                        print("Valor inválido! Digite um número inteiro.\n")

                totalAlterado = AlterarVetor(vetor, tam, valorProcurado, novoValor)
                if (totalAlterado > 0):
                    print(f"Elementos alterados com sucesso, foram alteradas {totalAlterado} posições!\n")
                else:
                    print("O valor não foi encontrado. Nenhuma posição foi alterada!\n")
            elif acao == "2":
                mostrarVetor(vetor, tam)
            else: 
                print("Valor inserido não é uma operação válida!!\n")
    except KeyboardInterrupt:
        print("Obrigado por utilizar o sistema!\n")
    