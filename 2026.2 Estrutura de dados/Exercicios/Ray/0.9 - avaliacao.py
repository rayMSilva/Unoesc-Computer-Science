import os

class Lista:
    _f: int
    _tamanho: int
    _lista: list

    def __init__(self, tamanho: int):
        self._f = -1
        self._tamanho = tamanho
        self._lista = [None] * self._tamanho

    def listaVazia(self):
        return True if self._f == -1 else False

    def validaInsercao(self):
        return True if self._f + 1 < self._tamanho else False

    def validaLimite(self, k: int, limite: int = None):
        if limite is None:
            limite = self._f
        return True if k >= 0 and k <= limite else False

    def inserirInicio(self, valor: int):
        if not self.validaInsercao():
            print("Lista cheia!!\n")
            return
        i = self._f
        while i >= 0:
            self._lista[i+1] = self._lista[i]
            i -= 1
        self._lista[0] = valor
        self._f += 1
        return

    def inserirFim(self, valor: int):
        if not self.validaInsercao():
            print("Lista Cheia!!\n")
            return
        self._f += 1
        self._lista[self._f] = valor
        return

    def inserirKesimo(self, valor: int, posicao: int):
        if not self.validaInsercao():
            print("Lista Cheia!!\n")
            return
        elif not self.validaLimite(k=posicao, limite=self._f + 1):
            print("Posição inválida!!\n")
            return
        else:
            i = self._f
            while i >= posicao:
                self._lista[i+1] = self._lista[i]
                i -= 1
            self._lista[posicao] = valor
            self._f += 1
        return

    def removerinicio(self):
        if not self.validaLimite(k=0):
            print("Lista vazia\n")
            return
        else:
            valorRemovido = self._lista[0]
            i = 0
            while i < self._f:
                self._lista[i] = self._lista[i + 1]
                i = i + 1
            self._lista[self._f] = None
            self._f -= 1
            return valorRemovido

    def removerfim(self):
        if not self.validaLimite(self._f):
            print("Lista vazia\n")
            return
        else:
            valorRemovido = self._lista[self._f]
            self._lista[self._f] = None
            self._f -= 1
            return valorRemovido

    def removerkesimo(self, posicao: int):
        if not self.validaLimite(posicao):
            print("Posição Invalida\n")
            return
        else:
            valorRemovido = self._lista[posicao]
            i = posicao
            while i < self._f:
                self._lista[i] = self._lista[i + 1]
                i += 1
            self._lista[self._f] = None
            self._f -= 1
            return valorRemovido

    def exibirLista(self):
        if self.listaVazia():
            print("Lista vazia!")
        else:
            for i in range(self._f + 1):
                print(f"posição [{i}]: valor = {self._lista[i]}")


class Menu:
    def exibirAcoes(self):
        print("""Operações disponiveis para fazer com sua lista
            1 - Inserir no inicio
            2 - Inserir no fim
            3 - Inserir no K
            4 - Remover no Inicio
            5 - Remover no Fim
            6 - Remover no K
            7 - Exibir lista
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
        minhaLista = Lista(10)
        menu = Menu()
        while(True):
            menu.exibirAcoes()
            opcaoEscolhida = menu.lerInteiro("Escolha uma opção ou CTRL + C para sair:\n")
            os.system("cls")
            match opcaoEscolhida:
                case 1:
                    valor = menu.lerInteiro("Digite o valor que deseja inserir no ínicio ou CTRL + C para sair do sistema:\n")
                    minhaLista.inserirInicio(valor)
                case 2:
                    valor = menu.lerInteiro("Digite o valor que deseja inserir no fim ou CTRL + C para sair do sistema:\n")
                    minhaLista.inserirFim(valor)
                case 3:
                    valor = menu.lerInteiro("Digite o valor que deseja inserir no késimo ou CTRL + C para sair do sistema:\n")
                    posicao = menu.lerInteiro("Digite a posicao que deseja inserir no késimo ou CTRL + C para sair do sistema:\n")
                    minhaLista.inserirKesimo(valor, posicao)
                case 4:
                    valorRemovido = minhaLista.removerinicio()
                    if valorRemovido is not None:
                        print(f"Valor removido: {valorRemovido}\n")
                case 5:
                    valorRemovido = minhaLista.removerfim()
                    if valorRemovido is not None:
                        print(f"Valor removido: {valorRemovido}\n")
                case 6:
                    posicao = menu.lerInteiro("Digite a posicao que deseja remover no késimo ou CTRL + C para sair do sistema:\n")
                    valorRemovido = minhaLista.removerkesimo(posicao)
                    if valorRemovido is not None:
                        print(f"Valor removido: {valorRemovido}\n")
                case 7:
                    minhaLista.exibirLista()
                case 0:
                    print("Obrigado por utilizar o sistema!\n")
                    break
                case _:
                    print("opção não encontrada!\n")

    except KeyboardInterrupt:
        print("Obrigado por utilizar o sistema!\n")