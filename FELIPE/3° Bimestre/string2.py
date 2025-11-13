# Sistema de menu simples que aceita variação de capitalização

#print("==== MENU DE OPÇÕES ====")
#print("Digite uma das opções baixo: ")
#print(" - Iniciar")
#print(" - Pausar")
#print(" - Sair")

#Entrada do usuário com tratamento de letras
#opcao = input("Escolha sua opção: ")

#Transformar para minusculas para padronizar
#opcao = opcao.lower().strip()

#Comparção já com o texto padronizado
#if opcao == "Iniciar":
 #   print("O programa foi iniciado com sucesso!")
#elif opcao == "Pausar":
 #   print("O programa foi pausado!")
#elif opcao == "Sair":
 #   print("Finalizando o programa. Até mais!")
#else:
 #   print("Comando inválido! Tente novamente")

#Sistema de geração de identificador com prefixo em caixa alta

#nome = input("Digite seu primeiro nome: ")
#sobrenome = input("DIgite seu sobrenome: ")

#Criar código do usuário em letras maiúsculas
#codigo = (nome[0] + sobrenome).upper()

#print(f"Seu código de acesso gerado é: {codigo}")

#Sitema de autenticação com limpeza de espaços

usuario_esperado = "admin"
senha_esperada = "123456"

print("==== Sitema de Login ====")
usuario_digitado = input("Usuário: ").strip()
senha_digitado = input("Senha: ").strip()

if usuario_digitado == usuario_esperado and senha_digitado == senha_esperada:
    print("Acesso liberado!")
else:
    print("Usuário ou senha incorreto!")