#include <stdio.h>

struct Cliente {
    int codigo;
    char nome[100];
};

int lerInteiro(char *mensagem)
{
    int valor;
    while (1) {
        printf("%s", mensagem);
        if (scanf("%d", &valor) == 1) {
            break;
        } else {
            printf("Valor Inválido! Digite um número inteiro!\n");
            while (getchar() != '\n');
        }
    }
    return valor;
}

void exibirClientes(struct Cliente clientes[], int tamanho)
{
    printf("\n\nCodigo  |  Nome\n");
    for (int i = 0; i < tamanho; i++) {
        printf("%d  |  %s\n", clientes[i].codigo, clientes[i].nome);
    }
}

int main()
{
    int tamanho = 10;
    struct Cliente clientes[10];

    for (int i = 0; i < tamanho; i++) {
        printf("Digite o nome do cliente: \n");
        scanf("%49s", clientes[i].nome);

        char mensagem[100] = "Digite o código do cliente: \n";
        clientes[i].codigo = lerInteiro(mensagem);
    }

    exibirClientes(clientes, tamanho);
    return 0;
}