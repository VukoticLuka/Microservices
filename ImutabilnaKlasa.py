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





#generic binary tree





if __name__ == "__main__":
    
    l1 = Lista([x for x in range(6)])
    l2 = Lista([int(x / 5) for x in range(50)])

    print(l1)
    print(Lista.get_broj_Lista())
