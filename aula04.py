'''
# try:
#     diadasemana = int(input("Qual seu melhor dia?"))
#     match diadasemana:
#         case 1:
#             print("Domingo")
#         case 2:
#             print("Segunda")
#         case 3:
#             print("Terça")
#         case 4:
#             print("Quarta")
#         case 5:
#             print("Quinta")
#         case 6:
#             print("Sexta")
#         case 7:
#             print("Sábado")
#         case _:
#             print("Invalido")   
# except ValueError:
#     print("Digite um numero inteiro")
'''


'''. Cálculo de Lâmpadas: OK
Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
3m² existe um bocal para uma lâmpada.'''
'''area =int(input("Quantos metros quadrados  voce deseja iluminar?:"))
watts = 3
print(F"A quantidade  de lampada é {area/watts}")
'''



'''2. Quantidade de Caixas de Azulejos:
Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
todas as suas paredes (considere que não será descontada a área ocupada por portas e
janelas). Cada caixa de azulejos possui 1,5 m²
'''
'''#area_azulejada = int(input("Qual area deseja azulejar?") )
#caixa = 1.5
#print (F"Precisamos Dessa quantidade de caixa de piso {area_azulejada/ caixa}")
'''
'''3. Rendimento do Taxista:
Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
média do consumo em km/L e o lucro (líquido) do dia.'''
Consumo_por_litro = 13
preco = 6.5
Hodometro_INICIAL= float(input("Quando começou a trabalhar quantos KM Estava?"))
Hodometro__FINAL = float(input("Quanto tá agora no final"))

resultado_hodometro = (Hodometro_INICIAL-Hodometro__FINAL)


'''4. Código de Origem do Produto:
Escreva um programa que leia o código de origem de um produto e imprima na tela a região
de sua procedência, conforme a tabela abaixo:
'''



# 5. Média do Aluno com Optativa:
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:
# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6
#Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
#resultado final.


#nota01 = float(input("Digite sua nota")
#nota02 = float(input("Digite sua nota"))

'''6. Positivo ou Negativo: OK
Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
valor zero como positivo
'''
'''valor = int(input("digite um numero"))
if valor >= 0:
    print("Positivo")
else:
    print("Negativo")
'''






    
