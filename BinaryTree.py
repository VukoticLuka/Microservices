from typing import Callable,List,Protocol,Generic,TypeVar,Iterable
from dataclasses import dataclass

In = TypeVar('In')

class Lista(Generic[In]):

    __brojLista = 0

    def __init__(self,l : Iterable[In]) -> None:
        self.lista = l
        self.add_lista()
    
    def iterate(self):
        for x in self.lista:
            print(x)

    @classmethod
    def get_broj_Lista(cls):
        return cls.__brojLista
    @classmethod
    def add_lista(cls):
        cls.__brojLista += 1

    def __repr__(self) -> str:
        zapis = ""
        for x in self.lista:
            zapis += str(x) + " "
        return zapis




T = TypeVar('T')
#generic binary tree

class Node(Generic[T]):
    __slots__ = 'data','left','right'
    def __init__(self,data : T) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return str(self.data) + " left: " + str(self.left) + ", right: " + str(self.right)
    
    def insertRec(self,data):
        if self.data >= data:
            if self.left is not None:
                self.left.insertRec(data)
            else:
                self.left = Node(data)
        else:
            if self.right is not None:
                self.right.insertRec(data)
            else:
                self.right = Node(data)
    def printRec(self):
        if self.left:
            self.left.printRec()
        print(self.data)
        if self.right:
            self.right.printRec()


    

@dataclass(order=True)
class BinaryTree(Generic[T]):
    def __init__(self, value : T) -> None:
        self.root = Node(value)

    def insert(self,data):
        self.root.insertRec(data)

    def printTree(self):
        self.root.printRec()
    




if __name__ == "__main__":
    
    l1 = Lista([x for x in range(6)])
    l2 = Lista([int(x / 5) for x in range(50)])

    print(l1)
    print(Lista.get_broj_Lista())

    l3 = [4,3,7,-1,-2,0,5]

    t = BinaryTree(2)

    for x in l3:
        t.insert(x)

    t.printTree()
    
