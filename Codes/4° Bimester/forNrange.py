# for percorre, elemento a elemento, qualquer iterável (lista, string, dicionários e etc...)
# modelo mental: Para cada elemento em sequencia, faça...

# Objetivo: padronizar nomes para busca e exibição
#produtos = [" mouse óptico", " Teclado mecânico ", " cabo HDMI 2m ", "Notebook    "]

#for nome in produtos:
    #nome_limpo = nome.strip()
    #nome_busca = nome_limpo.lower()
    #nome_exibicao = nome_limpo.title()
    #print(f"Original: {nome} | Busca: {nome_busca} | Exibição {nome_exibicao}")

# Objetivo: contar provedores de e-mail mais comuns
emails = ["ana@gmail.com", "joao@outlook.com", "suporte@empresa.com.br", "vendas@yahoo.com", "contato@gmail.com", "RH@OUTLOOK.COM", 
          "felipe@hotmail.com", "faq@empresa.com.br"]

gmail = outlook = yahoo = outros = 0

for e in emails:
    e_norm = e.strip().lower()
    if "@gmail.com" in e_norm:
        gmail += 1
    elif "@outlook.com" in e_norm or "@hotmail.com" in e_norm:
        outlook += 1
    elif "@yahoo.com" in e_norm:
        yahoo += 1
    else:
        outros += 1
print(f"Gmail:  {gmail} | Outlook/Hotmail: {outlook} | Yahoo: {yahoo} | Outros: {outros} ")

#Objetivo: sinalizar cargos proibidos
#registros = [
 #   {"nome": "Paula", "cargo": "Assistente de compras"},
  #  {"nome": "Rogério", "cargo": "Gerente"},
   # {"nome": "Iasmin", "cargo": "Estagiaria"},
    #{"nome": "Bruno", "cargo": "Analista Sênior"}
#]

#proibidos = ["estagiaria", "temporario"]

#for r in registros:
 #   cargo = r["cargo"].strip().lower()
  #  bloqueio = False
   # for termo in proibidos:
    #    if termo in cargo:
     #      bloqueio = True
      #     break
#print(
 #   f"{'BLOQUEIO' if bloqueio else 'OK'}: {r['nome']}"
  #  f"{' - Cargo não autorizado para aprovar pedidos.' if bloqueio else ' - Pode aprovar.'}"
#)