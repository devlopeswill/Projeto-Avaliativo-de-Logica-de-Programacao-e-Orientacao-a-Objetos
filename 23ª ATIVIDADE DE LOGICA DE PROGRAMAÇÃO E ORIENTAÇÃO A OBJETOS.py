class PA:

    def __init__(self):
        self.__peso = None
        self.__altura = None
    
    def set_peso(self, peso):
        self.__peso = peso

    def get_peso(self):
        print ("PESO:", self.__peso)
        return self.__peso

    def set_altura(self, altura):
        self.__altura = altura

    def get_altura(self):
        print ("ALTURA:", self.__altura)
        return self.__altura


guy1 = PA()
guy1.set_peso("65")
guy1.get_peso()

guy1.set_altura("180")
guy1.get_altura()


        

        