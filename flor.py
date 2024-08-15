# Atividade1

# nome = input('digite seu nome')
# cpf = input('digite seu cpf')
# endereço = input('digite seu endereço')
# email = input('digite seu email')
# telefone = input('digite seu telefone')

# cadastro = [nome,cpf,endereço,telefone]

# print('cadastro do cliente')
# print('nome',cadastro[0])
# print('email',cadastro[1])
# print('cpf',cadastro[1])

#  # comprar o produto 

# produtos = ['bola de futebol,blusa de time , chuteira original']
# preços = ['180.90, 300.90, 380.90']

# print('produtos disponiveis')
# print('1',produto[10],R$, preços[0])
# print('2',produtos[5],R$, preços[1])
# print('3',produtos[8],R$, preços[1])

#  #valor total  

#  produtos = ['1 bola de futebol, e 3 chuteira original']
#  preços = ['180.90 + 380.90']
#   print(valor total  pagar dos produto1 e produto3)



#Atividade2 

cliente1=input('digitar seu nome')
cliente1=input('digitar sua idade')

cliente2=input('digitar seu nome')
cliente2=input('digitar sua idade')

cliente3=input('digitar seu nome')
cliente3=input('digitar sua idade')

Quarto_cliente1=input('escolha seu quarto("simples , "duplo , e "luxo".)').strip().lower()
Quarto_cliente2=input('escolha seu quarto("simples , "duplo , e "luxo".)').strip().lower()
Quarto_cliente3=input('escolha seu quarto("simples , "duplo , e "luxo".)').strip().lower()

dias_cliente1= int(input('escolha quantos dias'))
dias_cliente2= int(input('escolha quantos dias'))
dias_cliente3= int(input('escolha quantos dias'))

preço_simples=100.00
preço_duplo=150.00
preço_luxo=250.00

if Quarto_cliente1 == 'simples':
    valor_cliente1=preço_simples * dias_cliente1
elif Quarto_cliente1 == 'duplo':
    valor_cliente1= preço_duplo * dias_cliente1
elif Quarto_cliente1 == 'luxo':
    valor_cliente1= preço_luxo *dias_cliente1
else:
    valor_cliente1=0


if Quarto_cliente2 == 'simples':
    valor_cliente1=preço_simples * dias_cliente1
elif Quarto_cliente2 == 'duplo':
    valor_cliente2= preço_duplo * dias_cliente2
elif Quarto_cliente2 == 'luxo':
    valor_cliente2= preço_luxo *dias_cliente2
else:
    valor_client21=0

if Quarto_cliente3 == 'simples':
    valor_cliente3=preço_simples * dias_cliente3
elif Quarto_cliente3 == 'duplo':
    valor_cliente3= preço_duplo * dias_cliente3
elif Quarto_cliente3 == 'luxo':
    valor_cliente3= preço_luxo *dias_cliente3
else:
    valor_cliente3=0


print(f'\nresumo:')
print(f"cliente_1({cliente1})): R$ {valor_cliente1:.2f}")
print(f"cliente_2({cliente2})): R$ {valor_cliente2:.2f}")
print(f"cliente_3({cliente3})): R$ {valor_cliente3:.2f}")

