import Node from Node (OK)

#DEFINITION DE LA CLASSE
class BinaryTree(Node) :

    #CONSTRUCTEUR
    def __init__(self,root):
        self.__root = root

    #GETTERS ET SETTERS
    def getRoot(self):
        return self.__root

    #AUTRES METHODES
    def createTree(self):
        Node(self.__root,)

    def isRoot(self,Node):
        self.__root == Node

    def Size(self):
        if Node == None :
            return 0
        else :
            return self.Size(Node.getRight()) + self.Size(Node.getLeft()) + 1

    def printValues(self, node):
        if node is None:
            return "arbre vide"
        else:
            return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())

    def sumValues(self, Node):
        if Node is None:
            return 0
        else:
            return self.sumValues(Node.getLeft()) + Node.getVal() + self.sumValues(Node.getRight())

    def numberLeaves(self,Node):
        counter = 0
        if self.getRight == None and self.getLeft == None :
            counter += 1
            self.numberLeaves(Node.getRight()) + self.numberLeaves(Node.getLeft())
        else :
            self.numberLeaves(Node.getRight()) + self.numberLeaves(Node.getLeft())
        return counter

    def numberInternalNode(self,Node):
        counter = 0
        if self.getRight == None and self.getLeft == None :
            self.numberLeaves(Node.getRight()) and self.numberLeaves(Node.getLeft())
        else :
            counter +=1
            self.numberLeaves(Node.getRight()) and self.numberLeaves(Node.getLeft())
        return counter

    def height(self,Node):
        counter = 0
        if self.getRight() == None :
            self.height(Node.getLeft())
            counter+=1
        elif self.getLeft()==None:
            self.height(Node.getRight())
            counter += 1
        elif self.getLeft() == None and self.getRight() == None :
            return counter
        else :
            self.height(Node.getRight()) and self.height(Node.getLeft())
            counter += 1

    def belongs(self,Node,val):
        if Node is None:
            return 0
        elif Node.getVal() == val and self.isRoot(Node):
            return True
        elif Node.getVal() == val:
            return 1
        else:
            return (self.belongs(Node.getLeft(), val) + self.belongs(Node.getRight(), val)) > 0

    def ancestors(self,Node,val):
        if Node == None or Node.getVal() == val:
            return ""
        else:
            if self.belongs(Node.getLeft(), val):
                return str(Node.getVal()) + " " + str(self.ancestors(Node.getLeft(), val))
            elif self.belongs(Node.getRight(), val):
                return str(Node.getVal()) + " " + str(self.ancestors(Node.getRight(), val))

    def descendants(self,Node,val):
        if self.getRight() == None :
            A = self.descendants(Node.getLeft())
            return A.getVal()
        elif self.getLeft() == None :
            B = self.descendants(Node.getRight())
            return B.getVal()
        elif self.getLeft() == None and self.getRight() == None :
            return "Ce noeud n'a pas de descendants"
        else :
            C = self.descendants(Node.getRight())
            D = self.descedants(Node.getLeft())
            return C.getVal() and D.getVal()

    def prefixe(self, Node):
        if Node == None:
            return ""
        else:
            return str(Node.getVal()) + " " + str(self.prefixe(Node.getLeft())) + str(self.prefixe(Node.getRight()))

    def infixe(self,Node):
        if Node == None:
            return ""
        else:
            return str(self.infixe(Node.getLeft())) + str(Node.getVal()) + " " + str(self.infixe(Node.getRight()))

    def postfixe(self,Node):
         if Node == None:
            return ""
         else:
            return str(self.postfixe(Node.getLeft())) + str(self.postfixe(Node.getRight())) + str(Node.getVal()) + " "

    #def parcourLargeur(self,Node):

#PROGRAMME PRINCIPAL
N21 = Node(21, None, None)
N18 = Node(18, None, None)
N3 = Node(3, None, None)

N19 = Node(19, N21, N18)
N4 = Node(4, None, N3)
N6 = Node(6, None, None)

N17 = Node(17, N19, None)
N5 = Node(5, N6, N4)

N12 = Node(12, N17, N5)
Tree = BinaryTree(N12)

object = Tree.Size()
print(object)
