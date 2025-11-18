#Verificar se número é positivo
#num = 10

#if num > 0:
    #print ("número positivo")
    
#if num > -5:
    #print ("Número positivo")
    
#--------------------------------------------------------------------------
#Decisões binárias com else

#num = 5

#if num >= 0:
    #print("Número positivo ou 0")
#else:
    #print("Número negativo")

#---------------------------------------------------------------------------
#Múltiplas condições com elif

#temp = 1045.95

#if temp > 39:
    #print ("Febre alta!")
#elif temp > 37.5:
    #print("Febre leve")
#elif temp > 35:
    #print ("Temperatura normal")
#else:
    #print ("Hipotermia")
#Lógica de decisão em cadeia: o programa avalia de cima para baixo. Ao encontrar a primeira condição 
#verdadeira executa e ignora as outras

#-----------------------------------------------------------------------------
#Verificação de entrada com autorização

#idade = int(input("Idade: "))
#autorizado = input("Está autorizado? (sim/não): ") =="sim", "Sim", "SIM", "S", "s"
#if idade >= 18 or autorizado:
    #print ("Pode entrar!")
#else:
    #print ("Acesso negado!")

#-----------------------------------------------------------------------------------
#Usando operadores relacionais e lógicos

#Situação escolar
nota = float(input("Nota final: "))
frequencia = int(input("Frequência (%): "))

if nota >= 6.0 and frequencia >= 75:
    print("Aluno aprovado!")
elif nota < 6.0 and frequencia >= 75:
    print("Aluno reprovado por nota!") 
elif nota >= 6.0 and frequencia < 75:
    print("Aluno reprovado por frequência!")
else:
    print("Reprovado por nota e frequência!")
