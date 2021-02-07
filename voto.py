# 1.8 - FORMATACAO DE STRING
# idade = 29
# print("Com " + str(idade) + " anos, voce e obrigado a votar")
# print("Com ", idade, " anos e obrigado a votar")
# # formacao de strings
# print(f"Com {idade} anos, e obrigado a votar") - nao deu certo
# ------
idade = input('Digite sua idade: ')
idade = int(idade)

if idade >= 18 and idade < 70:
    print("Com " + str(idade) + " anos, seu voto e obrigatorio")
elif idade >= 16:
    print("Com " + str(idade) + " anos, seu voto e facultativo")
else:
    print("Com " + str(idade) + " anos, voce nao pode votar")


# idade = 16
# # condicao q entrar na primeira etapa ja fica definido
# if idade >= 18 and idade < 70:
#     print("e obrigado a votar")
# elif idade >= 16:  # or idade >= 70:
#     print("voto facultativo")
# else:
#     print("nao pode votar")


# aula 1.7 - ENTRADA DE DADOS
# numero = input('Digite um numero: ')
# numero = int(numero)
# print(numero + 4)

# idade = input('Digite sua idade: ')
# idade = int(idade)

# if idade >= 18 and idade < 70:
#     print("e obrigado a votar")
# elif idade >= 16:  # or idade >= 70:
#     print("voto facultativo")
# else:
#     print("nao pode votar")


# #int:  inteiro/integer
# idade = 29
# # Ponto flutuante - floating point(f6
# loat)2
# - separado por ponto(.)
# preco = 33.50
# # str: - texto/string - vem de cadeia de caracteres(string[of characters])
# mensagem = "o voto e obrigatorio"
# # bool: booleano/boolean - verdadeiro ou falso
# situacao_regular = True
# print(idade)
# print(preco)
# print(mensagem)
# print(situacao_regular)

# Controle de fluxo (if, else, elif)
# situacao_regular = False
# if situacao_regular:
#     print("condicao e verdadeira")
#     print(8+2)
# else:
#     print("a condicao e falsa")

# print("fora do if")

# OPERACOES COM DADOS
# print(4+7)
# print(42 / 7)  #
# print(42 % 5)  # para saber o resto da divisao - op. de modulo
# print(42 // 5)  # saber a parte inteira da divisao

# CONVERSAO DE TIPO DE DADOS
# numero = '4'
# print(int(numero) + 7)
# print(float(numero) + 7)
# print(str(7) + ' ' + 'biscoito' + 's')
# # exibir o tipo de dados das variaveis
# print(type(7))
