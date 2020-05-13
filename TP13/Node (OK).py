#DEFINITION DE LA CLASSE
class Node :

    #CONSTRUCTEUR
    def __init__(self,val,right,left):
        self.__val = val
        self.__right = right
        self.__left = left

    #GETTERS ET SETTERS
    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def getVal(self):
        return self.__val

    def setVal(self,val):
        self.__val = val

    #AUTRES METHODES
    def print(self):
        print(self.getVal())
        print(self.getRight())
        print(self.getLeft())

#PROGRAMME PRINCIPAL
Ob = Node (3,2,1)
Ob.print()
