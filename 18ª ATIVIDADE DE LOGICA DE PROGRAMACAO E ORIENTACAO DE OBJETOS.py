#Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
#O método deve:

#- calcular três números complexos;
#- realizar todas as operações básicas;
#- e imprimir as propriedades real e img do números. 

nr1 = int(input("DIGITE A PARTE REAL DO PRIMEIRO NUMERO  "))
ni1 = int(input("DIGITE A PARTE IMAGINARIA DO PRIMEIRO NUMERO  "))
nr2 = int(input("DIGITE A PARTE REAL DO SEGUNDO NUMERO  "))
ni2 = int(input("DIGITE A PARTE IMAGINARIA DO SEGUNDO NUMERO  "))
nr3 = int(input("DIGITE A PARTE REAL DO TERCEIRO NUMERO  "))
ni3 = int(input("DIGITE A PARTE IMAGINARIA DO TERCEIRO NUMERO  "))

def calcpx (nr1, ni1, nr2, ni2, nr3, ni3):

    somar = nr1 + nr2 + nr3
    somai = ni1 + ni2 + ni3
    somac = '{} + {}i'.format(somar, somai)
    subr = nr1 - nr2 - nr3
    subi = ni1 - ni2 - ni3
    subc = "{} - {}i".format(subr, subi)
    mulr = nr1 * nr2 * nr3
    muli = ni1 * nr2 * nr3
    mulc = "{} x {}i".format (mulr, muli)
    divr = nr1 / nr2 / nr3
    divi = ni1 / ni2 / ni3
    divc = "{} / {}i". format (divr, divi)


    print ("SOMA COMPLEXA {} PARTE REAL {} PARTE IMAGINARIA {}i ".format(somac, somar, somai))
    print ("SUBTRAÇÃO COMPLEXA {} PARTE REAL {} PARTE IMAGINARIA {}i ".format (subc, subr, subi))
    print ("MULTIPLICAÇÃO COMPLEXA {} PARTE REAL {} PARTE IMAGINARIA {}i".format (mulr,muli,mulc))
    print ("DIVISAO COMPLEXA {} PARTE REAL {} PARTE IMAGINARIA {}i".format (divc, divr, divi ))



calcpx (nr1, ni1, nr2, ni2, nr3, ni3)