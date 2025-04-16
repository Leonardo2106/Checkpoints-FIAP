import pandas as pd
valores = []

def filtro(nome, idade, genero, data_consulta):
    # dicionarios
    precos = {
        "Clínico Geral": 120.00,
        "Ginecologista": 350.00,
        "Odontologista": 200.00,
        "Pediatra": 180.00,
        "Dermatologista": 250.00
    }
    consultas = {
        1: "Clínico Geral",
        2: "Ginecologista",
        3: "Odontologista",
        4: "Pediatra",
        5: "Dermatologista"
    }
    formas = {
        1: "Cartão de crédito",
        2: "Cartão de débito",
        3: "Dinheiro",
        4: "Pix"
    }

    while True:
        """
        Filtrando para que não apareça ginecologista quando for  M
        e nao aparecer pediatra quando for maior de 18
        """
        print('\nAgendamentos disponíveis: ')
        for num, valor in consultas.items():
            if valor == 'Ginecologista' and genero == 'M' or valor == 'Pediatra' and idade > 17:
                continue
            print(f"{num}. {valor}")

        #garantindo que o usuario escolha tudo corretamente
        try:
            opcao = int(input(f'\n{nome}, escolha a consulta desejada: '))
            if opcao not in consultas:
                print('\nPor favor, digite um número válido.')
                continue

            consulta = consultas[opcao]
            if (consulta == 'Ginecologista' and genero == 'M'):
                print('A opçao de "Ginecologista" não está disponível para o gênero masculino.')
                continue
            if (consulta == "Pediatra" and idade >= 18):
                print('A opcao de "Pediatra" não está disponível para pacientes menores de 18 anos.')
                continue
            break
        except ValueError:
            print('Por favor, digite um número válido.')

    valor_consulta = precos[consulta] # localizando o preço de acordo com a consulta marcada
    print(f'\n{nome}, a sua consulta com o {consulta} foi marcada para {data_consulta}.'
          f'\nO valor da consulta é de R$ {valor_consulta:.2f}.')

    # area de confirmação de pagamenmto
    confirmacao = input('\nDeseja prosseguir?(S/N): ').upper()
    while confirmacao not in ['S', 'N']:
        print('Por favor, insira S para Sim ou N para Não.')
        confirmacao = input("\nDeseja prosseguir? (S/N): ").upper()

    if confirmacao == 'S':
        print('\nFormas de pagamento:'
              '\n1. Cartão de crédito\n2. Cartão de débito\n3. Dinheiro\n4. Pix')
        while True:
            try:
                opcao_pagamento = int(input('\nEscolha uma opção de pagamento: '))
                if opcao_pagamento < 1 or opcao_pagamento > 4:
                    print('Por favor, escolha entre 1 e 4.')
                    continue
                break
            except ValueError:
                print('Por favor, insira um número válido.')

        # adicionando os valores na lista
        valores.append([nome, consulta, data_consulta, valor_consulta, formas[opcao_pagamento]])

    else: # caso tenha cancelado
        exit('\nVocê cancelou o agendamento\nCaso tenha sido um erro, repita o processo')

# começo
print('\nBem-vindo(a) ao Sistema de autoatendimento do Hospital Sr.Consultas!')
print('Para registrarmos o seu agendamento, é necessário preencher todos os espaços solicitados'
      ' com as informações do paciente.\n')

# separando a parte da entrada do usuário da função para poluir menos o código ;)
while True:
    nome_completo = input('Digite o nome completo do paciente: ')
    nome = nome_completo.split()[0]

    idade = int(input(f'{nome}, digite sua idade: '))

    """
    garantindo que o genero fique em maiusculo e tambem
    garantindo que ele será digitado m ou f
    """
    genero = input(f'{nome}, informe o seu gênero (M/F): ').upper()
    while genero not in ['M', 'F']:
        print("Por favor, selecione o gênero do paciente, sendo M para Masculino e F para Feminino.")
        genero = input("Gênero (M/F): ").upper()

    data_consulta = input('Digite a data da consulta (dd/mm): ')
    dia, mes = map(int, data_consulta.split('/')) # transformar a str em int e divir ela em dia e mes

    filtro(nome, idade, genero, data_consulta)

    # criando um dataFrame para organizar o resumo da consulta
    df = pd.DataFrame(valores, columns=['Paciente', 'Consulta', 'Data', 'Valor', 'Pagamento'])
    print(f'\nAtendimento finalizado. Obrigado!')
    print(f'\n{df}')
    break