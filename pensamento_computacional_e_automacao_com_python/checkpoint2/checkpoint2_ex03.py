import pandas as pd

valores = []
cargos = ['Gerente', 'Analista', 'Assistente', 'Estagiário']

def calculo(nome, salario_base, horas_extras, faltas, cargo, bonus):
    # aqui calcula o valor das horas extras
    valor_hora = salario_base * 0.015
    valor_extra_hora = valor_hora * horas_extras

    # aqui calcula o desconto das faltas
    valor_falta = salario_base * 0.02
    desconto_falta = valor_falta * faltas

    # aqui vai adicionar o bonus para cada cargo
    if bonus == 's':
        if cargo == 1:
            bonus_cargo = 1000
        elif cargo == 2:
            bonus_cargo = 500
        elif cargo == 3:
            bonus_cargo = 300
        elif cargo == 4:
            bonus_cargo = 100
        else:
            print("Cargo inválido.")
            return
    else:
        bonus_cargo = 0

    nome_cargo = cargos[cargo -1] # para mostrar o cargo corretamente no dataFrame

    total_acrescimo = valor_extra_hora + bonus_cargo # calculo do total de acrescimo
    total_salario = salario_base + total_acrescimo - desconto_falta # calculo do total do salario

    # adicionando na lista
    valores.append([nome, nome_cargo, salario_base, total_acrescimo, desconto_falta, total_salario])

nome = input('Digite o nome do funcionário: ')

print('\n1. Gerente\n2. Analista\n3. Assistente\n4. Estagiário')
cargo = int(input('\nDigite o cargo (1-4): '))

salario_base = float(input('\nDigite o salário base: R$ '))
horas_extras = int(input('Digite a quantidade de horas extras: '))
faltas = int(input('Digite a quantidade de faltas: '))

bonus = input('\nPossui bônus (s/n): ').lower()

calculo(nome, salario_base, horas_extras, faltas, cargo, bonus)

df = pd.DataFrame(valores, columns=['Funcionário', 'Cargo', 'Salário Bruto', 'Acrescimos', f'Descontos({bonus})', 'Salário Final'])
print(f'\n{df}')
