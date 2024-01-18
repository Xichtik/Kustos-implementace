from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class Karta:
    id: str
    jmeno: str
    prijmeni: str

class AbstractKustos(ABC):
    @abstractmethod
    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Optional[Karta]:
        ...
    
    @abstractmethod
    def odeber_kartu(self, id_karty: str) -> Optional[Karta]:
        ...
    
    @abstractmethod
    def muze_vstoupit(self, id_karty: str) -> bool:
        ...

class Kustos(AbstractKustos):
    karty: dict[str, Karta] = {}

    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Optional[Karta]:
        if self.muze_vstoupit(id_karty):
            return None
        self.karty[id_karty] = Karta(id_karty, jmeno, prijmeni)
        return self.karty[id_karty]

    def odeber_kartu(self, id_karty: str) -> Optional[Karta]:
        return self.karty.pop(id_karty, None)

    def muze_vstoupit(self, id_karty: str) -> bool:
        return id_karty in self.karty

kustos = Kustos()

kustos.pridej_kartu("1234", "Svem", "Splen")
kustos.odeber_kartu("2345")
print(kustos.muze_vstoupit("1234"))
kustos.odeber_kartu("1234")
print(kustos.muze_vstoupit("1234"))