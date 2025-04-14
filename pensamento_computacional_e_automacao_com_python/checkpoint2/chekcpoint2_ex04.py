import pandas as pd

valores = []

def funcao_geral(nome, idade, renda, valor, parcelas):
    # verificar idade
    if idade < 18:
        return (f'\n{nome}, você precisa ter mais de 18 anos para realizar o empréstimo.'
                f'\nStatus: Empréstimo Negado.')

    # verificar se o valor so emprestimo é 15 vezes maior
    if valor > 15 * renda:
        return (f'\n{nome}, o empréstimo ultrapassou 15x a sua renda mensal.'
                f'\nNão podemos realizar o empréstimo: R${valor:.2f}'
                f'\nStatus: Empréstimo Negado.')

    valor_parcela = valor / parcelas # calculo das parcelas

    # verificar se a parcela está entre 100 e 2000
    if valor_parcela < 100 or valor_parcela > 2000:
        return (f'\n{nome}, cada parcela deve ter valor entre R$ 100.00 e R$ 2000.00.'
                f'\nStatus: Empréstimo Negado.')

    # calculo da taxa dos juros
    if parcelas <= 6:
        taxa_juros = valor * 0.05
    elif parcelas <= 12:
        taxa_juros = valor * 0.08
    elif parcelas <= 24:
        taxa_juros = valor * 0.10
    else:
        return (f'{nome}, o número máximo de parcelas permitido é 24.'
                f'\nStatus: Empréstimo Negado.')

    valor_total = valor + taxa_juros
    valor_parcela_corrigida = valor_total / parcelas
    juros_totais = taxa_juros

    valores.append([nome, valor_total, parcelas, valor_parcela_corrigida, juros_totais])


nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
renda = float(input('Digite sua renda mensal: R$ '))

valor = float(input('\nDigite o empréstimo necessário: R$ '))
parcelas = int(input(f'\nDigite a quantidade de parcelas (R${valor:.2f})'
                     f'\nParcelas (3 até 24): '))

alerta = funcao_geral(nome, idade, renda, valor, parcelas)
print(alerta) # printar o alerta se tiver algum impedimento

if valores: # para imprimir o dataframe (se tudo der OK)
    df = pd.DataFrame(valores, columns=["Nome", "Valor Total", "Parcelas", "Valor Parcela", "Juros Totais"])
    print(f'\n{nome}, o seu empréstimo foi aprovado!')
    print(f'\n{df}')
