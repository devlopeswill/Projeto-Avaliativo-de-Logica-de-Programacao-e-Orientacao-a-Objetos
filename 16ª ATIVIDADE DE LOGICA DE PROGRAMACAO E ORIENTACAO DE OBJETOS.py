#Faça um algoritmo de ordenação utilizando o método insertion sort.
#Crie um método que execute as seguintes operações:

#- Tamanho do vetor: 30;
#- Utilize números ímpares;
#- Opere em ordem crescente.

import array

def sort(array):

    for c in range(0, len(array)):
        while c > 0:
            if array[c - 1] > array[c]:
                array[c], array[c - 1] = array[c - 1], array[c]
            c -= 1


array = [43, 31, 3, 9, 55, 23, 15, 11, 7, 27, 41, 19, 21, 29, 45, 57, 25, 59, 39, 51, 13, 47, 37, 17, 49, 35, 53, 5, 1, 33]

sort(array)    
print(array)   