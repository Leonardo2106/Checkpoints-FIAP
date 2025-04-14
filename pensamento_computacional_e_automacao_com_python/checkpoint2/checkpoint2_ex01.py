import pandas as pd

valores = []

def calculo_kg(codigo_estado ,peso_cargo, codigo_carga):
    imposto = [0.35, 0.25, 0.15, 0.05, 0]
    # toneladas para kg
    kg = peso_cargo * 1000.0

    # preço da carga
    if codigo_carga >= 10 and codigo_carga <= 20:
        preco_carga = kg * 100.0
    elif codigo_carga >= 21 and codigo_carga <= 30:
        preco_carga = kg * 250.0
    elif codigo_carga >= 31 and codigo_carga <= 40:
        preco_carga = kg * 340.0
    else:
        return '\nDigite um valor válido!'

    # valor do imposto
    valor_imposto = preco_carga * imposto[codigo_estado -1]

    # total
    total = preco_carga + valor_imposto
    valores.append([kg, preco_carga, valor_imposto, total])

codigo_estado = int(input('Digite o código do estado de origem da carga (1-5): '))
peso_carga = float(input('Digite o peso da carga (em toneladas): '))
codigo_carga = int(input('Digite o código da carga (10-40): '))

calculo_kg(codigo_estado, peso_carga, codigo_carga)

# dataframe para organizar em um gráfico ;)
df = pd.DataFrame(valores, columns=['Peso da Carga (Kg)', 'Preço da Carga (R$)', 'Imposto (R$)', 'Total (R$)'])
print(f'\n{df}')