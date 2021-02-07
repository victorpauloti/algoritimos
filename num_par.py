num = input('Digite um numero: ')
num = int(num)

# saber o resto da divisao se for 0 e par
divisao = num % 2

if divisao == 0:
    print("O numero " + str(num) + " e PAR")
else:
    print("O numero " + str(num) + " e IMPAR")
