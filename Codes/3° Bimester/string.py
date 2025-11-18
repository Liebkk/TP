# .lower() - conversão para minúsculas
# nome completo: str.lower()
# tradução técnica: converte todos os caracteres de uma string para letras minúsculas

#resposta = input("Deseja continuar? (sim / não): ")
#if resposta.lower() == "sim":
   # print("Continuar...")
#else:
    #print("Encerrando...")

# .upper() - conversão para maiúsculas
# nome completo: str.upper()
# tradução técnica: transforma todos os caracteres de uma string para letra maiúscula
curso = "python" 
print(curso.upper())

curso = "python"
resultado = curso.upper()
print ("Saída final: ", resultado)

# .strip() - remoção de espaços em branco
# Nome completo: str.strip()
# Tradução técnica: elimina espaços em branco no início e fim da string

login = input("Digite seu login: ").strip()
if login == "Admin":
    print("Login reconhecido")
else:
    print("Usuário inválido")

# .replace() - substituição de conteúdo
# Nome técnico: str.replace(old, new)
# Tradução técnica: substitui todas as ocorrências de um techo antigo por um novo 

frase = "Olá aluno!"
print(frase)

nova_frase = frase.replace("aluno", "professor")
print(nova_frase)

# in e not in - Operadores de presença
# Nome completo: operadores de membro (membership operators)
# Tradução Técnica: Verificam se uma substring está ou não presente em uma string

email = input("Digite seu email: ").lower().strip()
if "@gmail.com" in email:
    print("Email do Gmail detectado.")
else:
    print("Email nulo!")

# len() - Tamanho da string
# Nome completo: len() - É uma função nativa da linguagem
# Tradução técnica: retorna a quantidade de caracteres de uma string

senha = input("Crie uma senha: ")
if len(senha) < 6:
    print("Senha muito curta!")

# Fatiamento de string [início: fim]
# Nome completo: string slicing
# Tradução técnica: Permite acessar parte de uma string por indices

texto = "Programação com python"
print (texto[0:11])
