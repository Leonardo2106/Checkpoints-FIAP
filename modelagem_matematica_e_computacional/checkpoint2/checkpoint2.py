import numpy as np
import matplotlib.pyplot as plt

def ex1():
    print('Exercício 1:')
    def juros_simples(capital, taxa, tempo):
        return capital * (1 + taxa * tempo)

    print(f'Montante depois de 12 meses: R$ {juros_simples(1000, 0.15, 12):.2f}\n')

    meses = np.arange(1, 13)
    montante = [juros_simples(1000, 0.15, t) for t in meses]

    plt.plot(meses, montante, color='b')
    plt.title('montante acumulado com juros simples (15% ao mês)')
    plt.xlabel('mês')
    plt.ylabel('montante (R$)')
    plt.grid()
    plt.xticks(meses)
    plt.show()

def ex2():
    print('Exercício 2:')
    def juros_composto(capital, taxa, tempo):
        return capital * (1 + taxa) ** tempo

    print(f'Montante após 10 anos: R$ {juros_composto(1000, 0.15, 10):.2f}\n')

    anos = np.arange(1, 11)
    montante = [juros_composto(1000, 0.15, t) for t in anos]

    plt.plot(anos, montante, color='b')
    plt.title('montante acumulado com juros composto (15% ao ano)')
    plt.xlabel('ano')
    plt.ylabel('montante (R$)')
    plt.grid()
    plt.xticks(anos)
    plt.show()

def ex3():
    print('Exercício 3:')
    def juros_composto(capital, taxa, tempo, frequencia):
        return capital * (1 + (taxa / frequencia)) ** (tempo * frequencia)

    print(f'Montante final em 1 ano: R$ {juros_composto(1.00, 1.0, 1, 1):.2f}\n'
          f'Montante final em 12 meses: R$ {juros_composto(1.00, 1.0, 1, 12):.2f}\n'
          f'Montante final em 52 semanas: R$ {juros_composto(1.00, 1.0, 1, 52):.2f}\n'
          f'Montante final em 365 dias: R$ {juros_composto(1.00, 1.0, 1, 365):.2f}\n')

def ex4():
    print('Exercício 4:')
    def juros_composto(capital, taxa, tempo, frequencia):
        return capital * (1 + (taxa / frequencia)) ** (tempo * frequencia)

    print(f'Resultado (n = 10000000): R$ {juros_composto(1.00, 1.0, 1, 10000000):.2f}\n')

    print(f' ---------- Comparação ---------- \n'
          f'Número de Euler: {np.e}\n'
          f'Função exp(1): {np.exp(1)}\n'
          f'Juros Composto: R$ {juros_composto(1.00, 1.0, 1, 10000000)}')

ex1()
ex2()
ex3()
ex4()