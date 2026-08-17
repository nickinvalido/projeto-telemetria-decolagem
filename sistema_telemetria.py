# Dados de telemetria

print("========= CRITERIOS PARA DECOLAGEM =========")
print("Temperatura interna: 10 a 35 °C")
print("Temperatura externa: 20 a 50 °C")
print("Integridade: 0 ou 1")
print("Energia: mínimo 40%")
print("Pressão: 1 a 4 bar")
print("Módulos críticos: 0 ou 1")
print("===============================================")

print("========== DIGITE OS VALORES PEDIDOS ==========")
print("===============================================")


def obter_telemetria():
    return {
        'temperatura': temperatura,
        'temperatura_externa': temperatura_externa,
        'integridade': integridade,
        'nivel_energia': energia,
        'pressao': pressao,
        'status_modulos_criticos': status_modulos_criticos,
    }


# TEMPERATURA
while True:
    try:
        temperatura = float(input("Digite a Temperatura interna da Nave: "))
        if temperatura >= 0:
            break
        else:
            print("A temperatura não pode ser negativa.")
    except ValueError:
        print("Insira um número válido!!!")


# TEMPERATURA EXTERNA
while True:
    try:
        temperatura_externa = float(input("Digite a temperatura externa da nave: "))
        if temperatura_externa >= 0:
            break
        else:
            print("Temperatura negativa.")
    except ValueError:
        print("Insira um número válido!!!")


# INTEGRIDADE
while True:
    try:
        integridade = int(input("Digite a integridade estrutural (0 ou 1): "))
        if integridade == 0 or integridade == 1:
            break
        else:
            print("Integridade deve ser 0 ou 1.")
    except ValueError:
        print("Insira um número válido!!!")


# ENERGIA
while True:
    try:
        energia = int(input("Digite o Nivel de Energia (%): "))
        if 0 <= energia <= 100:
            break
        else:
            print("Energia deve estar entre 0 a 100")
    except ValueError:
        print("Insira um número válido!!!")


# PRESSÃO
while True:
    try:
        pressao = float(input("Digite a pressão dos tanques (bar): "))
        if pressao >= 0:
            break
        else:
            print("A pressão precisa ser positiva!!!")
    except ValueError:
        print("Insira um número válido!!!")


# MÓDULOS CRÍTICOS
while True:
    try:
        status_modulos_criticos = int(
            input("Digite o status dos módulos críticos (1 para OK, 0 para falha): ")
        )
        if status_modulos_criticos in [0, 1]:
            break
        else:
            print("Status dos módulos críticos deve ser 0 ou 1.")
    except ValueError:
        print("Insira um número válido!!!")


# VERIFICAÇÃO
def verificar_decolagem(telemetria):
    alertas = []

    if telemetria['temperatura'] > 35:
        alertas.append("Alerta: Temperatura interna acima do limite seguro!")

    if telemetria['temperatura'] < 10:
        alertas.append("Alerta: Temperatura interna abaixo do limite seguro!")

    if telemetria['temperatura_externa'] < 20:
        alertas.append("Alerta: Temperatura externa abaixo do limite seguro!")

    if telemetria['temperatura_externa'] > 50:
        alertas.append("Alerta: Temperatura externa acima do limite seguro!")

    if telemetria['integridade'] == 0:
        alertas.append("Alerta: Integridade estrutural corrompida!")

    if telemetria['nivel_energia'] < 40:
        alertas.append("Alerta: Nível de energia crítico!")

    if telemetria['pressao'] < 1:
        alertas.append("Alerta: Pressão abaixo do limite seguro!")

    if telemetria['pressao'] > 4:
        alertas.append("Alerta: Pressão acima do limite seguro!")

    if telemetria['status_modulos_criticos'] == 0:
        alertas.append("Alerta: Falha em módulos críticos!")

    consumo_por_hora = 10
    tempo_missao = 4
    energia_necessaria = consumo_por_hora * tempo_missao

    print("\n===== ANÁLISE ENERGÉTICA =====")
    print(f"Consumo por hora: {consumo_por_hora}%")
    print(f"Tempo da missão: {tempo_missao} horas")
    print(f"Energia necessária: {energia_necessaria}%")
    print(f"Energia disponível: {telemetria['nivel_energia']}%")

    if telemetria['nivel_energia'] >= energia_necessaria:
        margem = telemetria['nivel_energia'] - energia_necessaria
        print(f"Margem de energia: {margem}%")
        print("ANÁLISE: Energia suficiente para a missão.")
    else:
        falta = energia_necessaria - telemetria['nivel_energia']
        print(f"Energia faltante: {falta}%")
        print("ANÁLISE: Energia insuficiente para a missão.")
        alertas.append("Energia insuficiente para completar a missão!")

    if len(alertas) == 0:
        return "Todos os sistemas estão operando dentro dos parâmetros normais, decolagem aprovada."

    resultado = "DECOLAGEM REJEITADA!\n"
    resultado += "ALERTAS ENCONTRADOS:\n"

    for alerta in alertas:
        resultado += f"- {alerta}\n"

    return resultado


telemetria = obter_telemetria()
print("===============================================")

resultado = verificar_decolagem(telemetria)

print("\n===== RESULTADO DA TELEMETRIA =====")
print("===================================")
print(f"> temperatura: {telemetria['temperatura']} °C <")
print(f"> temperatura externa: {telemetria['temperatura_externa']} °C <")
print(f"> integridade: {telemetria['integridade']} <")
print(f"> nível de energia: {telemetria['nivel_energia']} % <")
print(f"> pressão: {telemetria['pressao']} bar <")
print(f"> status dos módulos críticos: {telemetria['status_modulos_criticos']} <")
print("===================================")
print(f"RESULTADO DA TELEMETRIA: {resultado}")
