Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


#calculadora

numero1 = 0
numero2 = 0
operacao = ''
resultado = 0

numero1 = int(input("DIGITE O PRIMEIRO NUMERO"))
numero2 = int(input("DIGITE O SEGUNDO NUMERO"))
operacao = input("DIGITE A OPERAÇAO A SER EFETUADA")

if operacao == "1":
    resultado = numero1+numero2
elif operacao == "2":
    resultado = numero1-numero2
elif operacao == "3":
    resultado = numero1*numero2
elif operacao == "4":
    resultado = numero1/numero2
else:
    resultado = 0

print (str(numero1) + ' ' + str(operacao) + ' ' + str(numero2) + ' = ' + str(resultado))