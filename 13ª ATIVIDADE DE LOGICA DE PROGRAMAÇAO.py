#Desenvolva um código que simule uma eleição com três candidatos.
#- candidato_X => 889
#- candidato_Y => 847
#- candidato_Z => 515
#- branco => 0

#O código deve perguntar se deseja finalizar a votação depois do voto. 
#Caso o número do voto não corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo. 
#Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente.

#Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a quantidade de votos de cada candidato, os brancos e nulos 


#Eleições

class Candidato:  
    
    def __init__(self, nome, numero, voto):
        self.nome = nome
        self.numero = numero
        self.voto = voto


candidato_X = Candidato ("Candidato_X",  889, 0)
candidato_Y = Candidato ("Candidato_Y", 847, 0)
candidato_Z = Candidato ("Candidato_Z", 515, 0)
brancos = 0
nulos = 0

def menu():

    print("ELEIÇÃO")
    print( candidato_X.nome, candidato_X.numero)
    print( candidato_Y.nome, candidato_Y.numero)
    print( candidato_Z.nome, candidato_Z.numero)
    print( "branco", "0")

menu()  
        
        
while True:
    try:
        voto = int(input("DIGITE O NUMERO DO SEU CANDIDATO" ))
    
    except:
        print ("APENAS NUMEROS SÃO VALIDOS" )
    else:    
        if voto == candidato_X.numero:
            candidato_X.voto += 1
    
        elif voto == candidato_Y.numero:
            candidato_Y.voto +=1
    
        elif voto == candidato_Z.numero:
            candidato_Z.voto +=1
    
        elif voto == 0:
            brancos +=1
            nulos +=1
    
        else:
            nulos +=1
        
    fim = str(input("DESEJA FINALIZAR A ELEIÇÃO ? SIM OU NAO?"))
    if fim == "SIM":
            break

vencedor = ""

if candidato_X.voto > candidato_Y.voto and candidato_X.voto > candidato_Z.voto:
    vencedor = candidato_X.nome
    
elif candidato_Y.voto > candidato_Z.voto and candidato_Y.voto> candidato_X.voto:
    vencedor = candidato_Y.nome
    
elif candidato_Z.voto > candidato_Y.voto and candidato_Z.voto > candidato_X.voto:
    vencedor = candidato_Z.nome
        
print ("RESULTADO DA ELEIÇÃO")

print ("O VENCEDOR DA ELEIÇÃO É O", vencedor)

print ("O", candidato_X.nome, "OBTEVE", candidato_X.voto, "VOTOS")

print("O", candidato_Y.nome, "OBTEVE", candidato_Y.voto, "VOTOS")       

print("O", candidato_Z.nome, "OBTEVE", candidato_Z.voto, "VOTOS")

print(brancos, "votos foram branco")

print(nulos, "votos foram nulo")