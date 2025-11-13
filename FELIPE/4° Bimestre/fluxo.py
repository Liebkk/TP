# sintaxe
#for elemento in sequencia:
    #if condicao_de_parada:
    #    break

#-------------------------------------

#Interrompendo uma contagem
#for numero in range(1, 11):
    #print("Número: ", numero)
    #if numero == 5:
        #break

#----------------------------------------------

# Busca condicional em base de dados simulada
#pedidos = [101, 102, 103, 104, 105, 106]

# Pedido com erro detectado
#pedido_com_erro = 104

#for pedido in pedidos:
    #print("Verificando pedido: ", pedido)
    #if pedido == pedido_com_erro:
    #    print("Erro detectado! Interromper verificação.")
    #    break

#print("Fluxo de auditoria encerrado.")

#-------------------------------------------------------------

# sintaxe
#for elemento in sequencia:
    #if condicao_para_ignorar:
    #    continue
    # codigo executa apenas se a condição for falsa

# ignorando números pares
#for numero in range(1, 8):
    #if numero % 2 == 0:
    #    continue
    #print("Número ímpar: ", numero)

# ignorando cadastros vazios
#cadastros = ["Felipe", "", "Vinicius", " ", "Gerson", ""]
#for nome in cadastros:
    #nome = nome.strip()
    #if nome == "":
    #    continue
    #print("Cadastro válido: ", nome)

#--------------------------------------------------------------------

# comando pass
# definição técnica: O comando pass é uma instrução nula. Ele não faz nada, mas é necessário quando a sintaxe
#exige um comando, e ainda não há lógica a ser implementada 

#estrutura planejada
#0for produto in ["Mouse", "Tecladp", "Monitor"]:
    #pass

#----------------------------------------------------------------------

# integração prática: Controle logístico com fluxo condicional

produtos = [
    {"id": 1, "nome": "Notebook", "Status:": "ok"},
    {"id": 2, "nome": "Mouse", "Status:": "ok"},
    {"id": 3, "nome": "Teclado", "Status:": "pedente"},
    {"id": 4, "nome": "Monitor", "Status:": "falha"},
    {"id": 5, "nome": "Webcam", "Status:": "ok"},
]
for produto in produtos:
    if produto["Status"] == "falha":
        print("Erro grave no produto: ", produto ["nome"])
        print("Interrompendo inspeção para revisão técnica.")
        break

    if produto["Status"] == "pendente":
        print("Produto ", produto["nome"], "aguardando verificação.")
        continue

    pass
    print("Produto verificado com sucesso: ", produto["nome"])
print("Processo de inspeção concluído!")