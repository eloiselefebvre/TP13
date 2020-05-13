from BinaryTree (OK) import BinaryTree

#DEFINITION DE LA CLASSE
class BinarySearchTree(BinaryTree):

    def __init__(self,root):
        self.__root = root

#AUTRES METHODES
    #def contains(self,Node,val):

    #def findMin(self,Node):

    #def findMax(self,Node):

    #def insert(self,Node,val):

    #def equivalentsBST(self,Node1,Node2):



#PROGRAMME PRINCIPAL
N14 = (14,None,None)
N6 = (7,None,None)
N3 = (3,None,None)
N13 = (13,None,N14)
N15 = (15,N13,None)
N7 = (7,None,N6)
N20 = (20,None,12)
N12 = (12,N15,N7)
N1 = (1,None,None)
N0 = (0,None,N1)
N2 = (2,N0,N3)
N4 = (4,N20,N2)
