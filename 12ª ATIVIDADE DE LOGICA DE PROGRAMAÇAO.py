#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. 
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

#cadastro_nome_idade


nome = input(" Digite seu nome completo ")


while True: 

    try:
        ano_nascimento = int(input(" Digite o seu ano de nascimento: "))
        if ano_nascimento < 1992 or ano_nascimento > 2021:
            print ("Só são validos anos de nascimento entre 1992 e 2021")
            continue
        break
     
    except:
        print(" Digite caracteres validos ")
        
data = 2022
idade = data - ano_nascimento

print("Seu nome é", nome, "e sua idade é", idade)
        
        