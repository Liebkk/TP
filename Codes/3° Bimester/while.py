# O laço while executa uma sequência de comandos de forma repetida, enquanto a condição estabelecida permanece verdadeira.
# sintaxe:
# while condição:
# Bloco de código executado repetidamente
# Loop de contagem automática

#contador = 1
#while contador <= 5:
    #print("Número: ", contador)
    #contador += 1

# Validação de entrada
#resposta = ""

#while resposta.strip().lower() != "sim":
#    resposta = input("Deseja continuar?(sim/não): ")
    
#print("Programa iniciando.")

# Menu interativo com multiplas ações

#opcao = ""
#while opcao != "sair":
    #print("\n Menu de opções")
    #print("[1] Cadastrar")
    #print("[2] Listar")
    #print("[3] Sair")

#opcao = input("Escolha uma opção: ").strip().lower()

#if opcao == "1" or opcao == "cadastrar":
    #print("usuário cadastrado com sucesso.")
#elif opcao == "2" or opcao == "listar":
    #print("Listando usuários...")
#elif opcao == "3" or opcao == "sair":
    #print("Encerrando sistema...")
    #break
#else:
    #print("Opção inválida. Tente novamente!")

print(" SISTEMA DE COMPRAS")
#Inicia o loop principal do sistema

while True:
    #Solicita o nome do produto
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ").strip()
    #Verifica se o usuário deseja sair
    if produto.lower() == "sair":
        print("Encerrando o sistema...")
        break #Sai do loop
#Solicita o preço do produto e converte para Float
preco = float(input("Digite o preço do produto: "))
#a Calcula um imposto ficticio de 8
Imposto = preco * 0.08
#Soma o valor total com Imposto
total = preco + imposto

#Solicita a senha de segurança (entrada simalada)
senha = input("Digite a senha de segurança: ").strip()
#Lista de senhas autorizadas
senhas_autorizadas = ["admin123", "supervisor", "gerente"]

#Validação da senha com presença na lista
if senha.lower() in senhas_autorizadas:
#Condicional com operadores aritméticos e logicos

    if total > 100 and total < 500:
        print("compra aprovada com valor médio.")

    elif total >- 500:
        print("Compra aprovada com valor alto.")
    else:
        print("Compra aprovada com valor baixo.")

else:
    #Senha não está autorizada
    print("Senha incorreta. A compra foi bloqueada.")

print("Resumo da operação:")
print("Produto:", produto)
print("Valor bruto: RS", preco)
print("Imposto aplicado: $", imposto)
print("Total com imposto: R$", total)
print("-" * 40) #Separador visual