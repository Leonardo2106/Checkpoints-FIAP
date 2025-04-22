## 🎇 Checkpoint 2 - Modelagem Matemática e Computacional

### Questão 1: Juros Simples


1a) Traduza a fórmula de juros simples **(Equação 1)** para uma função de Python 

1b) Suponha que o Capital inicial $C$ seja de R\$1000, que a taxa de juros $r$ seja de $15\%$ (lembre-se de converter para decimal) e que o número de períodos $n$ seja referente aos meses.  

Ao final de 12 meses, qual será o montante?  
Utilize a sua implementação de Python de 1a) para calcular.  

1c) Gere um array de números inteiros entre 1 e 12, representando os meses do ano. Agora, calcule o montante mês a mês e gere um gráfico disso.

---

### Questão 2: Juros Compostos

2a) Traduza a fórmula de juros compostos **(Equação 2)** para uma função de Python  

2b) Suponha que o Capital inicial $C$ seja de R\$1000, que a taxa de juros $r$ seja de $15\%$ (lembre-se de converter para decimal) e que o número de períodos $t$ seja referente aos anos.  

Ao final de 10 anos, qual será o montante?  
Utilize a sua implementação de Python de 2a) para calcular.  

2c) Gere um array de números inteiros entre 1 e 10, representando os anos. Agora, calcule o montante para cada ano e gere um gráfico disso.

---

### Questão 3: Cobrança cada vez mais rápida de juros

3a) Traduza a nova fórmula de juros compostos **(Equação 3)** para uma função de Python

3b) Suponha que o Capital inicial $C$ seja de apenas um real, isto é, R\$1.00. E que a taxa de juros $r$ seja de $\mathbf{100\%}$ (lembre-se de converter para decimal)

No período de 1 ano (t = 1), calcule o montante final para cada $n$ indicado:

 - $n$ = 1: anual
 - $n$ = 12: mensal
 - $n$ = 52: semanal
 - $n$ = 365: diário

 3c) O que está acontecendo com o valor, na medida que a incidência de juros é mais rápida?

---

### Questão 4: O que o número de Euler tem a ver com tudo isso?

4a) Vamos utilizar a **Equação 3** e considerar que:

- Capital inicial $C$ seja  R\$1.00
- A taxa de juros $r$ seja  $\mathbf{100\%}$
- O período $t$ seja de 1 ano (t = 1)
- A frequência de composição $n$ seja muito grande, por exemplo $n = 10000000$.

Qual é o resultado?

4b) Compare com o número de euler np.e. Há semelhanças e diferenças?

4c) Compare com o resultado da função np.exp(1). Há semelhanças ou diferenças?

---

### 📦 Instalação
```
bash

git clone https://github.com/Leonardo2106/Checkpoints-FIAP
cd modelagem_matematica_e_computacional
cd checkpoint2
pip install -r requirements.txt
python checkpoint2.py
```
