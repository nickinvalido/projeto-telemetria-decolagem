# Sistema de Telemetria para Decolagem

## 1. Descrição do projeto

Este projeto simula um sistema de telemetria de uma nave antes da decolagem. O programa recebe dados dos sensores, verifica as faixas de segurança predefinidas, realiza uma análise energética e decide entre **PRONTO PARA DECOLAGEM** e **DECOLAGEM ABORTADA**.

## 2. Organização e descrição da telemetria

O sistema interpreta os seguintes dados:

| Parâmetro | Critério |
|---|---|
| Temperatura interna | 10 a 35 °C |
| Temperatura externa | 20 a 50 °C |
| Integridade estrutural | 0 ou 1 |
| Nível de energia | mínimo de 40% |
| Pressão dos tanques | 1 a 4 bar |
| Status dos módulos críticos | 0 ou 1 |

Para integridade e módulos críticos:
- `1` = condição OK
- `0` = condição de falha/corrompida

## 3. Análise energética

A atividade solicita a análise da autonomia/condição energética considerando:

- capacidade total em kWh;
- carga atual em %;
- consumo estimado na decolagem em kWh;
- perdas energéticas em %.

### Cálculos utilizados

**Energia disponível inicialmente:**

`energia_inicial = capacidade_total × (carga_atual / 100)`

**Energia perdida:**

`energia_perdida = energia_inicial × (perdas_energeticas / 100)`

**Energia após perdas:**

`energia_apos_perdas = energia_inicial - energia_perdida`

**Saldo após o consumo da decolagem:**

`saldo_apos_decolagem = energia_apos_perdas - consumo_decolagem`

Se o saldo for maior ou igual a zero, a energia é suficiente para a decolagem. Se for negativo, a decolagem é abortada.

## 4. Algoritmo de verificação

O algoritmo verifica todos os parâmetros da missão e armazena os problemas encontrados em uma lista de alertas. Ao final, se a lista estiver vazia e o saldo energético for suficiente, o resultado é **PRONTO PARA DECOLAGEM**. Caso contrário, o resultado é **DECOLAGEM ABORTADA**, acompanhado dos alertas.

O pseudocódigo está disponível em `pseudocodigo.txt`.

## 5. Arquivos do projeto

- `sistema_telemetria.py` — script Python funcional.
- `sistema_telemetria.ipynb` — Notebook Python.
- `relatorio_telemetria.pdf` — relatório da atividade.
- `pseudocodigo.txt` — algoritmo em pseudocódigo.
- `testes/` — exemplos de testes de execução.
- `README.md` — documentação do projeto.

## 6. Como executar

### Pelo Python

1. Instale o Python 3.
2. Abra o terminal na pasta do projeto.
3. Execute:

`python sistema_telemetria.py`

4. Digite os dados solicitados.
5. Confira a análise energética e o resultado final.

### Pelo Jupyter Notebook

1. Abra o Jupyter Notebook ou JupyterLab.
2. Abra `sistema_telemetria.ipynb`.
3. Execute as células em ordem.

## 7. Teste recomendado — PRONTO PARA DECOLAGEM

Use:

- Temperatura interna: `25`
- Temperatura externa: `30`
- Integridade: `1`
- Nível de energia: `80`
- Pressão: `2.5`
- Módulos críticos: `1`
- Capacidade total: `100`
- Carga atual: `80`
- Consumo na decolagem: `20`
- Perdas energéticas: `10`

Cálculo:

- Energia inicial = 100 × 80/100 = **80 kWh**
- Perdas = 80 × 10/100 = **8 kWh**
- Energia após perdas = 80 - 8 = **72 kWh**
- Saldo após decolagem = 72 - 20 = **52 kWh**

Resultado esperado: **PRONTO PARA DECOLAGEM**.

## 8. Teste recomendado — DECOLAGEM ABORTADA

Use:

- Temperatura interna: `5`
- Temperatura externa: `55`
- Integridade: `0`
- Nível de energia: `30`
- Pressão: `5`
- Módulos críticos: `0`
- Capacidade total: `100`
- Carga atual: `30`
- Consumo na decolagem: `35`
- Perdas energéticas: `10`

Cálculo:

- Energia inicial = 100 × 30/100 = **30 kWh**
- Perdas = 30 × 10/100 = **3 kWh**
- Energia após perdas = 30 - 3 = **27 kWh**
- Saldo após decolagem = 27 - 35 = **-8 kWh**

Resultado esperado: **DECOLAGEM ABORTADA**, com alertas de telemetria e energia insuficiente.

## 9. Repositório

Repositório público no GitHub:

https://github.com/nickinvalido/projeto-telemetria-decolagem

## 10. Prints da execução

A pasta `testes/` contém os exemplos de saída. Para a entrega final, recomenda-se substituir/acompanhar esses arquivos por prints reais feitos durante a execução no computador.

## 11. Entregáveis

O projeto foi organizado para atender aos itens indicados na atividade:

- relatório em PDF;
- repositório público no GitHub;
- Notebook Python (`.ipynb`);
- README com explicação do projeto;
- prints/exemplos de execução;
- instruções de execução do código.
