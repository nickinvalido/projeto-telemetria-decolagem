# Sistema de Telemetria para Decolagem

## 1. Descrição do projeto
Este projeto simula um sistema de verificação de telemetria de uma nave espacial antes da decolagem. O programa recebe dados dos sensores, verifica se cada parâmetro está dentro dos limites de segurança e informa se a decolagem deve ser aprovada ou rejeitada.

## 2. Dados analisados
- Temperatura interna: 10 a 35 °C
- Temperatura externa: 20 a 50 °C
- Integridade estrutural: 0 ou 1
- Nível de energia: mínimo de 40%
- Pressão dos tanques: 1 a 4 bar
- Status dos módulos críticos: 0 ou 1

## 3. Análise energética
O sistema considera consumo de 10% de energia por hora durante uma missão de 4 horas.

Energia necessária = 10 × 4 = 40%.

Além da verificação dos parâmetros, o programa informa a margem de energia quando ela é suficiente ou a quantidade faltante quando não é.

## 4. Lógica de decisão
A decolagem é aprovada somente quando não houver nenhum alerta. Caso um ou mais parâmetros estejam fora dos limites, a decolagem é rejeitada e os alertas são apresentados.

## 5. Estrutura do projeto
- `sistema_telemetria.py` — código principal.
- `sistema_telemetria.ipynb` — notebook Python para execução/apresentação.
- `relatorio_telemetria.pdf` — relatório com requisitos, pseudocódigo, fluxograma e análise.
- `prints_execucao/` — exemplos de saídas para conferência.

## 6. Como executar
### Python
1. Instale o Python 3.
2. Abra o terminal na pasta do projeto.
3. Execute:
   `python sistema_telemetria.py`
4. Digite os valores solicitados.
5. Confira a análise energética e o resultado da telemetria.

### Jupyter Notebook
1. Abra o Jupyter Notebook/JupyterLab.
2. Abra `sistema_telemetria.ipynb`.
3. Execute as células em ordem.

## 7. Teste recomendado — decolagem aprovada
- Temperatura interna: 25
- Temperatura externa: 30
- Integridade: 1
- Energia: 80
- Pressão: 2.5
- Módulos críticos: 1

Resultado esperado: decolagem aprovada.

## 8. Teste recomendado — decolagem rejeitada
- Temperatura interna: 5
- Temperatura externa: 55
- Integridade: 0
- Energia: 30
- Pressão: 5
- Módulos críticos: 0

Resultado esperado: decolagem rejeitada, com vários alertas.


## 9. GitHub
`https://github.com/nickinvalido/projeto-telemetria-decolagem`
