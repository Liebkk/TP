#Operadores de atribuição composta
#O que são operadores de atribuição composta
#(+=, -=, *=, /=)
#É a reatribuição de resultados à própria variável
#Exemplo:
#x = x + 1 - Pode ser reescrito como:
#x += 1

#Incremeneto de 1 unidade
#num = 5
#num += 1
#print(num)

#decremento de 1 unidade
#estoque = 10
#estoque -= 1
#print(estoque)

#Multiplicação acumulada
#fator = 3
#fator *= 2
#print(fator)

#Sequência de incrementos
#pontuacao = 0
#pontuacao += 1
#pontuacao += 2
#print(pontuacao)

#Controle de saldo de compra
#saldo = 1000
#saldo -= 200
#saldo += 100
#print("Saldo atual: ", saldo)

#Dobra de valor com *= (Investimento)
#investimento = saldo
#investimento *= 2
#print("Novo valor: ", investimento) 

#Energia incial do personagem
#energia = 100

#O jogador deve escolher o que acontece na aventura
#evento = input("O que aconteceu com o personagem? (Pocao / Batalha / Descanso / Armadilha): ")

#Cada evento altera a energia usando um operador de atribuição composta diferente
#if evento == "pocao":
    #energia += 20
#elif evento == "batalha":
    #energia -= 30
#elif evento == "descanso":
    #energia /= 0.2
#else:
    #energia *=0.8
    
#exibir o valor final da energia
#print("Energia final do personagem: ", energia)

#Simulação de ajuste de preço em três etapas
preco = 100
preco += 10
preco -= 5
preco *= 1.1
print("Preço final: ", preco)