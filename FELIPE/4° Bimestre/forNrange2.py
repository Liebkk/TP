# etiquetas 1..N
# Título do script; indica que vamos imprimir etiquetas de 1 a N

n = 5
# Define N (quantidade de etiquetas) como 5. Poderia vir de input ou banco de dados; aqui está fixo para exemplo.

for numero in range(1, n + 1):
    # Laço que percorre de 1 até N (incclusive).
    # O n+1 é usado porque range é exclusivo no final
    # Situação típica: geração sequencial de ID's, etiquetas, posições, senhas provisórias e etc.
    print(f"Etiqueta : {numero}")
    # Exibe a etiqueta atual. f-string permite inserir o valor da variável 'numero' dentro do texto
    

#janela de horário comercial
#indica que o código percorre os horários úteis do dia

for hora in range (9, 18): #9..17
    # Percorre números de 9 até 17, pois 18 é exclusivo no range.
    # Usado para representar o período de funcionamento padrão (9h ás 17h)
    # Pode ser aplicado para gerar horários de reunião, agendamento, lembretes etc
    print(f"Agendar lembrete às {hora}h")
    # Exibe o horário do lembrete para cada hora dentro do intervalo




# mascarar CPF (últimos 3)
# Objetivo: ocultar todos os dígitos, exceto os três finais, mantendo a privacidade do dado
cpf = "12345678901"
# CPF usado no exemplo. Em um sistema real, viria de uma entrada de usuário ou de um banco de dados
mascarado = ""
# string vazia que será usada para armazenar o CPF parcialmente mascarado.
for i in range(len(cpf)):
    # percorre os indices de 0 até o último indice da string cpf
    # a posição é necessária para decidir se o caractere deve ser mascarado ou mantido
    mascarado += "*" if i < len(cpf) - 3 else cpf[i]
    # se o indice for menor que o comprimento total menos 3, substitui por "*"
    # caso contrário, mantém o dígito original (os 3 últimos)
    # usado para exibir CPFs de forma segura conforme boas práticas de privacidade
print(f"CPF mascarado: {mascarado}")
# mostra o CPF final, com todos os dígitos mascarados, exceto os 3 últimos


# paginação de 3 em 3 - demonstra como dividir uma lista de registros em blocos (páginas) de tamanho fixo

registros = ["r1", "r2", "r3", "r4", "r5", "r6", "r7"]
# lista de registros. em um sistema real, viria de uma base de dados ou leitura de arquivo
tamanho = 3
# define o tamanho máximo de registros por página
total = len(registros)
# calcula o total de registros disponíveis para controle do laço
for inicio in range(0, total, tamanho):
    # laço com incremento de 'tamanho' (0, 3 , 6, ...). Cada valor de 'inicio' representa o indice inicial de uma nova página
    pagina = registros[inicio:inicio+tamanho]
    # Cria uma fatia (slice) da lista contendo apenas os elementos da página atual. Exemplo prático: mostrar resultados paginados em telas ou relatórios longos
    print(f"Página: {pagina}")
    # exibe os registros que compõem a página


# processamento em lotes - demonstra como normalizar nomes de produtos em blocos para otimizar o processamento

catalogo = [" Produto A", "PRODUTO B", "produto C ",
            " Produto D", " Produto E", "produto F ",
            "gadget X ", " gadget Y"]
# lista com produtos em formatos variados (maiusculas, minusculas e espacos extras)
lote = 4
# Define o tamanho de cada lote. cada lote é processamento de forma independente
total = len(catalogo)
# obtém o número total de itens do catálogo
for inicio in range(0, total, lote):
    # percorre a lista em passos do tamanho do lote (0, 4, 8, ...)
    bloco = catalogo[inicio:inicio+lote]
    # cria uma sublista contendo apenas os itens do lote atual.
    print(f"Processamento bloco: {inicio} a {min(inicio+lote, total)-1}")
    # exibe o intervalo de indices do lote sendo processado. o min() evita que o indice ultrapasse o total de itens na última iteração
    for item in bloco:
        # percorre cada produto dentro do lote atual
        print(f" - normalizado: {item.strip().title()}")
        # strip() remove espaços extras no inicio e fim. title() converte o texto para o formato "Título" (primeira letra maiuscula). resultado: nomes padronizados e prontos para exibição e comparação
        