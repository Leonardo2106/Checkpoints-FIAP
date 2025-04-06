#include <stdio.h>
#include <stdlib.h>

#define carbo_tomate 0.031
#define extrato_carbo 0.1333

int main(){
    int opcao, tomate, extrato;
    float extrato_recipiente;

    printf("MENU - Extrato de Tomate\n");
    printf("Escolha uma opção (1-4):\t");
    scanf("%i", &opcao);

    switch(opcao){
        case 1:
            printf("\nOpção: A\n");

            printf("\nDigite o peso do tomate (em gramas):\t");
            scanf("%i", &tomate);

            float calculo1 = tomate * carbo_tomate;

            printf("\n%i g de tomate possui %.2f g de carboidrato.\n", tomate, calculo1);
            break;

        case 2:
            printf("\nOpção: B\n");

            printf("\nQuantidade de carboidrato em 1 colher de sopa\n(15 g) de extrato de tomate: %.2f g.\n", extrato_carbo * 15);
            break;

        case 3:
            printf("\nOpção: C\n");

            printf("\nDigite o peso do tomate (em gramas):\t");
            scanf("%i", &tomate);
            printf("Digite o peso do extrato (em gramas):\t");
            scanf("%i", &extrato);

            float calculo_tomate = tomate * carbo_tomate;
            float calculo_extrato = extrato * extrato_carbo;

            printf("\nTotal de carboidrato no molho: %.2f g.\n", calculo_tomate + calculo_extrato);

            if(calculo_tomate > calculo_extrato){
                printf("\nO tomate contribuiu mais com os carboidratos do molho.\n");
            }else {
                printf("\nO extrato de tomate contribuiu mais com os\ncarboidratos do molho.\n");
            }
            break;

        case 4:
            printf("\nOpção: D\n");

            printf("\nDigite a capacidade do recipiente (em gramas):\t");
            scanf("%f", &extrato_recipiente);

            float calculo2 = extrato_recipiente * (600.0 / 100.0);

            printf("\nSerão necessarios aproximadamente %.2f g de\ntomates para fazer %.2f g de extrato\nartesanal.\n", calculo2, extrato_recipiente);
            break;
    }
}
