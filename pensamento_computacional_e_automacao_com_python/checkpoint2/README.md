## 🎇 Checkpoint 2 - Pensamento Computacional e Automação com Python

### 🎆 Exercício 1:
#### Faça um programa que recebe: 

- O código do estado de origem da carga de um caminhão, supondo que é um 
número inteiro de 1 a 5  
- O peso da carga do caminhão em toneladas 
- O código da carga, supondo que é um número inteiro de 10 e 40

#### Seu programa deve calcular: 

- O peso da carga do caminhão convertido em quilos 
- O preço da carga do caminhão 
- valor do imposto que e cobrado com base no preço da carga e do estado de 
origem 
- O valor total transportado pelo caminhão (carga + impostos)

#### Utilize as tabelas abaixo:
| Estado | Imposto |  | Código da Carga | Preço por Kg |
| - | - | - | - | - |
| 1 | 35% |  | 10 a 20 | R$ 100,00 |
| 2 | 25% |  | 21 a 30 | R$ 250,00 |
| 3 | 15% |  | 31 a 40 | R$ 340,00 |
| 4 | 5% |  | - | - |
| 5 | isento  |  | - | - |

---

### 🎆 Exercício 2:
Faça um programa que leia 3 valores que representam os lados de um triângulo A, 
B e C e ordene-os em ordem decrescente, de modo que o lado A representa o 
maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados 
formam, com base nos seguintes casos:  

Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;  
Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;  
Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;  
Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO;  

Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;  
Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO
ISOSCELES;

---

### 🎆 Exercício 3:
Você foi contratado para criar um sistema de RH que calcula o salário final de um 
funcionário com base em diversos fatores: cargo, horas extras, faltas, bônus e 
descontos.  
#### Requisitos: 
#### 1. O programa deve solicitar: 
  - Nome do funcionário 
  - Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário) 
  - Salário base (float) 
  - Total de horas extras trabalhadas 
  - Total de faltas no mês 
  - Se recebeu bônus por desempenho (s ou n)

#### 2. Regras de cálculo: 
  - Valor da hora extra: 
▪ 1.5% do salário base por hora extra 
  - Desconto por falta: 
▪ 2% do salário base por falta 
  - Bônus (se aplicável):  
▪ Gerente: R$ 1000  
▪ Analista: R$ 500  
▪ Assistente: R$ 300  
▪ Estagiário: R$ 100

#### 3. O sistema deve: 
  - Calcular e mostrar:  
▪ Salário bruto  
▪ Total de acréscimos (horas extras + bônus)  
▪ Total de descontos (faltas)  
▪ Salário final

---

### 🎆 Exercício 4:
Você vai desenvolver um sistema para um banco que analisa se o cliente pode 
pegar um empréstimo, e se sim, calcula os juros e parcelas de acordo com o 
perfil.

#### Requisitos:
#### 1. O programa deve solicitar:
  - Nome do cliente
  - Idade
  - Renda mensal
  - Valor desejado do empréstimo
  - Número de parcelas (3 até 24)

#### 2. Regras:
  - Para ser aprovado:
      - Ter mais de 18 anos
      - Valor do empréstimo não pode ultrapassar 15x a renda mensal
      - Parcelas devem ser no mínimo R$ 100,00 e no máximo R$ 2000,00
  - Taxa de Juros:
      - Se o número de parcelas <= 6 -> 5% ao mês
      - 7 a 12 parcelas -> 8% ao mês
      - 13 a 24 parcelas -> 10% ao mês

#### 3. O sistema deve:
  - Informar se o empréstimo foi aprovado ou negado
  - Se aprovado:
    - Mostrar o valor total com juros
    - Valor de cada parcela
    - Juros totais pagos
   
---

📦 **Instalação**  
```bash
git clone https://github.com/Leonardo2106/Checkpoints-FIAP 
cd pensamento_computacional_e_automacao_com_python
cd checkpoint2
pip install -r requirements.txt
```

---

### 🎇 Checkpoint - Professor [Alexandre Russi Jr.](https://github.com/alexandrerussi)
