#Construa um algoritmo de ordenação, utilizando o método bubble sort estudado. 
# (Lembre-se que se trata de uma série de instruções que devem ser seguidas passo a passo).
#Para isso, você deve criar um método em que o tamanho do vetor seja dez e deve estar em ordem crescente.

#O vetor deverá:
#- comparar seus elementos dois a dois adjacentes;
#- se os elementos não estiverem em ordem, então ordenar;
#- senão, avançar para o próximo par;
#- repetir a operação até que nenhuma troca possa ser feita no vetor inteiro.


def sort(array):

    for final in range(len(array), 0, -1):
        for current in range(0, final -1):
    if array[current] > array[current + 1]:
        array[current], array[current + 1] = array[current + 1], array[current]


array = [8,3,4,2,1,5,7,9,6,10]
sort(array)
print(array)