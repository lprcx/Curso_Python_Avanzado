class Stack:
    def __init__(self) -> None:
        self.items = [] 

    def __str__(self) -> str:
        return " || ".join([str(i) for i in self.items])
    
    def push(self, value):
        self.items.append(value)
        print("Se agregó el elemento: ", value, "a la pila.")

    def pop(self):
        if self.is_empty():
            print("La pila esta vacia")
            return
        return self.items.pop()
    
    def verificar(self):
        if self.is_empty():
            print("La pila está vacía")
        else:
            print("La pila no está vacía")
    
    def vaciar(self):
        if self.is_empty():
            print("La pila está vacía.")
        else:
            for i in range(pila.size):
                print("El elemento eliminado fue: ", pila.peek())
                pila.pop()
        
    def peek(self):
        if self.is_empty():
            print("la pila esta vacia")
            return
        return self.items[-1]
        
    @property
    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size == 0
    
#Crear una pila vacía
pila = Stack()
print("Se creó una pila")

#Agregar los siguientes elementos a la pila: 10, 20, 30, 40, 50
pila.push(10)
pila.push(20)
pila.push(30)
pila.push(40)
pila.push(50)

#Imprimir el tamaño de la pila
print("El tamaño de la pila es: ", pila.size)

#Imprimir el elemento eliminado
print("El elemento eliminado es: ", pila.peek())

#Eliminar el elemento tope de la pila
pila.pop()

#Verificar si la pila está vacía
pila.verificar()

#Agregar 60 y 70 a la pila
pila.push(60)
pila.push(70)

#Imprimir el tamaño de la pila nuevamente
print("El nuevo tamaño de la pila es: ", pila.size)

#Pila
print("-----------------PILA--------------------")
print(pila)

# Eliminar y mostrar todos los elementos de la pila uno por uno.
pila.vaciar()
print("La pila está vacía")