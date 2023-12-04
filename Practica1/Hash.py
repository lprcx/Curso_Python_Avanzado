# Tabla Hash
import hashlib


class HashTable:
    def __init__(self, _capacity=127) -> None:
        self.capacity = _capacity
        self.table = [[] for _ in range(_capacity)]

    def hash_function(self, value) -> int:
        aux = hashlib.md5(value.encode()).hexdigest()
        key = 0
        for i in range(0, len(aux)):
            key += ord(aux[i])
        return key % self.capacity

    def insert(self, contact):
        hash = self.hash_function(contact.nombre)
        self.table[hash].append(contact)

    def search(self, calificacion):
        hash = self.hash_function(calificacion)
        if len(self.table[hash]) > 0:
            _lista = []
            for contact in self.table[hash]:
                if calificacion == contact.calificacion:
                    _lista.append(str(contact))
            return _lista
        return None
    
    def remove(self, value):
        hash = self.hash_func(value)
        if len(self.table[hash])>0:
            for i in range(len(self.table[hash])):
                if self.table[hash][i]==value:
                    del self.table[hash][i]
                    print("Elemento con valor: ", value, " ha sido eliminado")
                    return
        print("No hay elementos con el valor: ", value)
    

class Estudiante():
    def __init__(self, nombre, calificacion) -> None:
        self.nombre = nombre
        self.calificacion = calificacion

    def __str__(self) -> str:
        return str({"nombre": self.nombre, "calificacion": self.calificacion})


est1 = Estudiante("Manuel Castillo", 99)
est2 = Estudiante("Lourdes Reyes", 85)
est3 = Estudiante("Pedro Silva", 80)
est4 = Estudiante("Pablo Suarez", 95)
est5 = Estudiante("Luisa Ramirez", 90)



lista_contactos = HashTable()
lista_contactos.insert(est1)
lista_contactos.insert(est2)
lista_contactos.insert(est3)
lista_contactos.insert(est4)
lista_contactos.insert(est5)

busqueda = lista_contactos.search("Lourdes Reyes")
print(str(busqueda))

