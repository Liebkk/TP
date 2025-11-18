# -------------------------------
# INÍCIO DO SISTEMA DE EVENTO
# -------------------------------

# Etapa 1 - Entrada no Evento

# Pergunta se a pessoa tem ingresso
tem_ingresso = input("Você possui ingresso? (sim/nao): ")

# Pergunta se a pessoa é convidada
e_convidado = input("Você é convidado? (sim/nao): ")

# Pergunta a idade da pessoa69
idade = int(input("Qual a sua idade?: "))

# Verifica as condições de entrada
if e_convidado == "sim":
    print("Entrada liberada. Bem-vindo, convidado!")
elif tem_ingresso == "sim" and idade >= 18:
    print("Entrada liberada. Divirta-se no evento!")
elif tem_ingresso == "sim" and idade < 18:
    print("Entrada parcial permitida. Acesso limitado para menores de idade.")
else:
    print("Acesso negado. Você não possui autorização.")

# -------------------------------
# Etapa 2 - Simulação de Consumo de Energia
# -------------------------------

# Energia inicial do evento
energia = 100  # kWh

# Informa o uso predominante de energia
uso = input("Qual foi o tipo de uso predominante no evento? (chuveiro/ar-condicionado/geladeira): ")

# Reduz energia com base no tipo de uso
if uso == "chuveiro":
    energia -= 30  # reduz 30 kWh
elif uso == "ar-condicionado":
    energia -= 20  # reduz 20 kWh
elif uso == "geladeira":
    energia -= 10  # reduz 10 kWh

# Pergunta se houve economia de energia
economizou = input("Houve economia de energia? (sim/nao): ")

# Recupera parte da energia se houve economia
if economizou == "sim":
    energia += 5  # recupera 5 kWh

# Avalia o consumo final
if energia > 70:
    print("Consumo consciente de energia.")
elif energia >= 40:
    print("Consumo moderado.")
else:
    print("Alerta de consumo alto!")

# Mostra o valor final da energia restante
print("Energia restante: " + str(energia) + " kWh")

# -------------------------------
# Etapa 3 - Compras de Brindes com Desconto
# -------------------------------

# Pergunta o valor total da compra
compra = float(input("Digite o valor total da compra: R$ "))

# Aplica o desconto conforme o valor da compra
if compra > 1000:
    desconto = compra * 0.20  # 20% de desconto
elif compra >= 500:
    desconto = compra * 0.10  # 10% de desconto
else:
    desconto = compra * 0.05  # 5% de desconto

# Calcula o valor final após aplicar o desconto
valor_final = compra - desconto

# Exibe o resultado com concatenação
print("Desconto aplicado: R$ " + str(round(desconto, 2)))
print("Valor final da compra: R$ " + str(round(valor_final, 2)))
