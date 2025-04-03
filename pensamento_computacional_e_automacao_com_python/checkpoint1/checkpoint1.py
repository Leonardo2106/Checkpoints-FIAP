def exercicio1():
    print('\nBem-vindo(a) ao conversor de moedas')

    reais = float(input('\nDigite o valor: R$ '))

    print(f'\n(BRL) Real: R${reais:.2f}\n'
          f'(USD) Dólar Americano: ${reais * 0.1736:.2f}\n'
          f'(EUR) Euro: £{reais * 0.1603:.2f}\n'
          f'(ARS) Peso Argentino: ${reais * 185.9:.2f}\n'
          f'(GBP) Libra Esterlina: £{reais * 0.1341:.2f}\n'
          f'(JPY) Iene: ¥{reais * 26.01:.2f}\n')

def exercicio2():
    print('\nBem-vindo(a)')
    numero = int(input('\nDigite um número (até 999): '))

    print(f'\nCentena: {int(numero // 100 * 100)}'
          f'\nDezena: {int(numero // 10 % 10 * 10)}'
          f'\nUnidade: {int(numero % 10)}\n')

def exercicio3():
    print('\nBem-vindo(a)')

    idade = int(input('\nQuantos anos você tem: '))
    meses = int(input('Quantos meses você viveu após seu aniversário: '))
    dias = int(input('Quantos dias você viveu após seu aniversário: '))

    print(f'\nAtualmente você tem {idade} anos, {meses} meses e {dias} dias de vida'
          f'\nVocê viveu aproximadamente: {(idade * 365) + (meses * 30) + dias} dias\n')

def exercicio4():
    print('\nBem-vindo(a)')
    dias_info = int(input('\nQuantos dias de vida vc tem até agora: '))

    print(f'Atualmente você tem {int(dias_info / 365)} anos,'
          f' {int((dias_info % 365) / 30)} meses e'
          f' {dias_info % 365 % 30} dias de vida\n')

exercicio1()
exercicio2()
exercicio3()
exercicio4()