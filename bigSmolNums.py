# Receba um numero do usuario -> verifique se é divisivel por 3 :
# se sim -> print é divisivel
# se nao -> print o restante

# num = int(input("NÚMERO : "))
# if (num % 3) == 0:
#     print(f"O numero {num} é divisivel por 3")
# else:
#     print(f"O numero {num} tem resto {num % 3} na divisão por 3, logo {num} = {num // 3} * 3 + {num % 3}")

# Receba dois numeros do usuario -> Verifique se o primeiro numero é divisivel pelo segundo :
# De uma mensagem clara

# isDiv = int(input("Digite o número a ser dividido : "))
# div = int(input("Digite o divisor : "))

# if (isDiv % div) == 0:
#     print(f"O numero {isDiv} é divisivel por {div}!")
# else:
#     print(f"O numero {isDiv} tem resto {isDiv % div} na divisão por {div}, logo {isDiv} = {isDiv // div} * {div} + {isDiv % div}")

# Recebe tres numeros do usuario -> print o maior dentre eles

# firstNum = float(input("Digite o primeiro numero : "))
# secondNum = float(input("Digite o segundo numero : "))
# thirdNum = float(input("Digite o terceiro numero : "))

# if (firstNum > secondNum) and (firstNum > thirdNum):
#     print(f"O primeiro numero {firstNum} é o maior dentre eles")
# elif (secondNum > firstNum) and (secondNum > thirdNum):
#     print(f"O segundo numero {secondNum} é o maior dentre eles")
# else:
#     print(f"O terceiro numero {thirdNum} é o maior dentre eles")

# if firstNum > (secondNum and thirdNum):
#     print('sim')
# else:
#     print('não')

# Recebe tres numeros do usuario -> pergunte se ele quer saber o maior ou o menor -> mostre na tela o maior ou menor dependendo da escolha do usuario

# firstNum = float(input("Digite o primeiro numero : "))
# secondNum = float(input("Digite o segundo numero : "))
# thirdNum = float(input("Digite o terceiro numero : "))

# choice = str(input("Voce quer verificar se o numero é 'MAIOR' ou se é 'MENOR'?"))

# if choice == 'MAIOR':
#     if (firstNum > secondNum) and (firstNum > thirdNum):
#         print(f"O primeiro numero {firstNum} é o maior dentre eles")

#     elif (secondNum > firstNum) and (secondNum > thirdNum):
#         print(f"O segundo numero {secondNum} é o maior dentre eles")

#     else:
#         print(f"O terceiro numero {thirdNum} é o maior dentre eles")

# elif choice == 'MENOR':
#     if (firstNum < secondNum) and (firstNum < thirdNum):
#         print(f"O primeiro numero {firstNum} é o menor dentre eles")

#     elif (secondNum < firstNum) and (secondNum < thirdNum):
#         print(f"O segundo numero {secondNum} é o menor dentre eles")

#     else:
#         print(f"O terceiro numero {thirdNum} é o menor dentre eles")

# else:
#     ('Resposta invalida, favor tentar novamente')

# Receba dois numeros do usuario -> pergunte se ele quer fazer uma soma, subtração, divisão ou multiplicação -> responda de acordo

# operacao = (input("Você gostaria de : \nsomar (+)\nsubtrair (-)\nmultiplicar (*)\ndividir (/)\n"))
#
# firstNum = float(input("Digite o primeiro numero : "))
# secondNum = float(input("Digite o segundo numero : "))
#
# if operacao == '+':
#     print(f'A soma entre {firstNum} e {secondNum} é {firstNum + secondNum}')
# elif operacao == '-':
#     print(f'A subtracao entre {firstNum} e {secondNum} é {firstNum - secondNum}')
# elif operacao == '*':
#     print(f'A multiplicao entre {firstNum} e {secondNum} é {firstNum * secondNum}')
# elif operacao == '/':
#     print(f'A divisao entre {firstNum} e {secondNum} é {firstNum / secondNum}')
# else:
#     print(f'Operador {operacao} não é uma operacao valida em nosso sistema')

i = 0
while i < 3:
    palavra += input()
