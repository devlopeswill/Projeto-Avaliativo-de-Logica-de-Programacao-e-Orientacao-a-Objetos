#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
# No início, o programa mostrará a seguinte lista de operações:
#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. 
# Depois precisa executar a operação e mostrar o resultado na tela. 
# Quando o usuário escolher a opção “Sair”, o sistema irá parar. 

#É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

#calculadora

numero1 = 0
numero2 = 0
operacao = ''
resultado = 0
sair = 1 


def calculadora ():
    While True:
        print(" 1:SOMA\n 2:SUBTRACAO\n 3:MULTIPLICACAO\n 4:DIVISAO\n")
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
        elif operacao == "0":
            print(" Até logo... :( ")
            break

    print (str(numero1) + ' ' + str(operacao) + ' ' + str(numero2) + ' = ' + str(resultado))

