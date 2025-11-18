# Estrutura sintática básica de uma função:
#def nome_da_funcao():
    # Bloco de código

# Código linear (função):
#print("Iniciando cálculo de comissão...")
#venda = 1500
#comissao = venda * 0.1
#print("Comissão calculada: ", comissao)

#print("Iniciando cálculo de comissão...")
#venda = 2300
#comissao = venda * 0.2
#print("Comissão calculada: ", comissao)

# Código funcional com função
#def calcular_comissao(valor_venda):
   # comissao = valor_venda * 0.1
   # print("A comissão é: ", comissao)

#calcular_comissao(1500)
#calcular_comissao(2300)
#calcular_comissao(5200)

# Função simples
#def mensagem_boas_vindas():
#    print("Sistena de cadastro inciado.")
#    print("Conectando ao servidor principal...")
#    print("Ambiente pronto para uso.")

#mensagem_boas_vindas()

# Função Intermediárioo[
#def registrar_usuario(nome, setor):
#    print("Usuário cadastrado: ", nome)
#    print("Setor associado: ", setor)
#    print("Cadastrado realizado com sucesso.\n")

#registrar_usuario("Mariana Silva", "Financeiro")
#registrar_usuario("José Antônio", "Logística")

# Função avançado
#def calcular_desconto(valor_compra):
#    if valor_compra > 1000:
#        desconto = valor_compra * 0.1
#
#    elif valor_compra >= 500:
#        desconto + valor_compra * 0.05
#    
#    else
#        desconto = 0
#
#    return valor_compra - desconto

#valor_final = calcular_desconto(1200)
#print("Valor final após desconto: ", valor_final)

# Função avançado
def verificar_dados(nome, idade):
    if nome == "" or idade <= 0:
        return False
    return True

def calcular_idade_apos_anos(idade, anos):
    return idade + anos

def cadastrar_funcionario(nome, idade, anos):
    if verificar_dados(nome, idade):
        nova_idade = calcular_idade_apos_anos
        print(f"Funcionário {nome.titler()} cadastro. Idade atualizada: {nova_idade} anos.") 
    else:
        print("Erro no cadastro: dados inválidos.")

cadastrar_funcionario("Felipe", 29, 6)
cadastrar_funcionario("", 22, 2)