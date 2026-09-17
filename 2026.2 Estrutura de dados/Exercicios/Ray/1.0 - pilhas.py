import os


class Pilha:
    _tamanho: int
    _topo: int
    _pilha: list

    def __init__(self, tamanho):
        self._tamanho = tamanho
        self._topo = -1
        self._pilha = [None] * tamanho

    def pilhaVazia(self):
        return True if self._topo == -1 else False

    def pilhaCheia(self):
        return True if self._topo == self._tamanho - 1 else False

    def empilha(self, valor):
        if self.pilhaCheia():
            print("Pilha Cheia!!")
            return
        self._topo += 1
        self._pilha[self._topo] = valor
        return self._topo

    def desempilha(self):
        if self.pilhaVazia():
            print("Pilha Vazia!!")
            return None
        valorRemovido = self._pilha[self._topo]
        self._pilha[self._topo] = None
        self._topo -= 1
        return valorRemovido

    def topoPilha(self):
        if self.pilhaVazia():
            print("Pilha Vazia!!")
            return None
        return self._pilha[self._topo]

    def mostrarPilha(self):
        if self.pilhaVazia():
            print("Pilha Vazia!!")
            return
        auxiliar = Pilha(self._tamanho)
        while not self.pilhaVazia():
            valor = self.desempilha()
            auxiliar.empilha(valor)
        posicao = 0
        while not auxiliar.pilhaVazia():
            valor = auxiliar.desempilha()
            print(f"posição [{posicao}]: valor = {valor}")
            self.empilha(valor)
            posicao += 1


class Menu:
    def exibirAcoes(self):
        print("""Operações disponiveis para fazer com sua pilha
1 - Empilhar
2 - Desempilhar
3 - Exibir Pilha
4 - Exibir Topo Pilha
0 - Sair\n""")

    def lerInteiro(self, mensagem):
        while(True):
            try:
                valorDigitado = int(input(mensagem))
                return valorDigitado
            except ValueError:
                print("O valor digitado não é um número inteiro!\n")
            except Exception as e:
                print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    try:
        minhaPilha = Pilha(10)
        menu = Menu()
        while(True):
            menu.exibirAcoes()
            opcaoEscolhida = menu.lerInteiro("Escolha uma opção ou CTRL + C para sair:\n")
            os.system("cls")
            match opcaoEscolhida:
                case 1:
                    valor = menu.lerInteiro("Digite o valor que deseja empilhar ou CTRL + C para sair do sistema:\n")
                    minhaPilha.empilha(valor)
                case 2:
                    valorRemovido = minhaPilha.desempilha()
                    if valorRemovido is not None:
                        print(f"Valor removido: {valorRemovido}\n")
                case 3:
                    minhaPilha.mostrarPilha()
                case 4:
                    valorTopo = minhaPilha.topoPilha()
                    if valorTopo is not None:
                        print(f"O valor que está no topo da pilha é {valorTopo}!\n")
                case 0:
                    print("Obrigado por utilizar o sistema!\n")
                    break
                case _:
                    print("opção não encontrada!\n")

    except KeyboardInterrupt:
        print("Obrigado por utilizar o sistema!\n")