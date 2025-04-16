#include <stdio.h>
 
int main() {
    int opcao;
    float tomate, extrato, peso, calculo1, calculo2;
 
    do {
        printf("1. Carboidratos por grama de tomate\n2. Carboidratos em uma colher de sopa de extrato de tomate\n3. Carboidrato no molho\n4. Quatidade de tomates para fazer molho artesanal\n5. Sair\n");
        printf("\nEscolha a opcao: \t");
        scanf("%d", &opcao);
 
        switch(opcao) {
            case 1:
                printf("\nDigite o peso dos tomates (g): \t"); scanf("%f", &peso);
                printf("%.2f g de tomates possui %.2f g de carboidrato.\n\n", peso,  peso * 0.031);
                break;
 
            case 2:
                printf("\nQuantidade de carboidrato em 1 colher de sopa\n(15 g) de extrato de tomate: %.2f g.\n\n", 2.0);
                break;
 
            case 3:
                printf("\nDigite a quantidade do tomate (g): \t"); scanf("%f", &tomate);
                printf("Digite a quantidade do extrato (g): \t"); scanf("%f", &extrato);
                
                calculo1 = tomate * 0.031;
                calculo2 = extrato * (4.0 / 30.0);
                
                printf("\nTotal de carboidrato: %.2f g\n", calculo1 + calculo2);
                printf("%s para os carboidratos do molho\n\n", calculo1 > calculo2 ? "O tomate contribuiu mais" : (calculo2 > calculo1 ? "O extrato contribuiu mais" : "Ambos contribuiram"));
                break;
 
            case 4:
                printf("\nDigite a capacidade do recipiente (g): \t"); scanf("%f", &peso);
                printf("\nTomates necessarios: %.2fg\n\n", peso * (600 / 100));
                break;
 
            case 5:
                printf("\nSaindo...");
                break;
 
            default:
                printf("\nPor favor, selecione um valor valido.\n\n");
        }
    } while (opcao != 5);
 
    return 0;
}
