#Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. 
#Depois, desenvolva três ou mais objetos para testar o código.

class Candidato:  
    
    def __init__(self, nome, numero, voto, leis):
        self.nome = nome
        self.numero = numero
        self.voto = voto
        self.leis = leis
    
def leis():
    print("Candidato_X // Leis aprovadas:", candidato_X.leis)
    print("Candidato_Y // Leis aprovadas:", candidato_Y.leis)
    print("Candidato_Z // Leis aprovadas:", candidato_Z.leis)



candidato_X = Candidato ("Candidato_X",  889, 0, 20)
candidato_Y = Candidato ("Candidato_Y", 847, 0, 40)
candidato_Z = Candidato ("Candidato_Z", 515, 0, 2)
brancos = 0
nulos = 0

def menu():

    print("ELEIÇÃO")
    print( "Nome:", candidato_X.nome, "Numero:", candidato_X.numero)
    print( "Nome:", candidato_Y.nome, "Numero:", candidato_Y.numero)
    print( "Nome:", candidato_Z.nome, "Numero:", candidato_Z.numero)
    print( "Branco", "0")

menu()  
        
leis()
        
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