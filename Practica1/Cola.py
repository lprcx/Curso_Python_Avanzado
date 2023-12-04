
class Queue:
    def __init__(self, size =1000) -> None:
        self.q = [None]*size 
        self.capacity = size
        self.front = 0 
        self.rear = -1 
        self.count = 0 

    def enqueue(self, value):
        if self.is_full():
            print("La cola esta llena")
            return
        print("Insertando elemento...", value)
        self.rear = (self.rear+1)%self.capacity
        self.q[self.rear] = value
        self.count +=1

    def dequeue(self):
        if self.is_empty():
            print("La cola esta vacía")
            return
        aux = self.q[self.front]
        print("El elemento eliminado fue: ", aux)
        self.front = (self.front +1)%self.capacity
        self.count -= 1
        return aux
    
    def verificacion(self):
        if self.is_empty():
            print("La cola está vacía")
        else:
            print("La cola no está vacía")

    def vaciar(self):
        if self.is_empty():
            print("La cola está vacía")
        else:
            for i in range(cola.size):
                cola.dequeue()


    def is_full(self) -> bool:
        return self.count == self.capacity
        

    def is_empty(self) -> bool:
        return self.count == 0
        print("La cola está vacía")

    @property
    def size(self) ->int:
        return self.count
    

#crear una cola
cola = Queue()
print("Se creó una cola")

#Agregar los siguientes elementos a la cola: 10, 20, 30, 40, 50
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)
cola.enqueue(50)

#Imprimir el tamaño de la cola.
print("el tamaño de la cola es:", cola.size)

#Eliminar el elemento en la parte frontal de la cola e imprimir
cola.dequeue()

# Verificar si la cola está vacía.
cola.verificacion()

#Agregar 60 y 70 a la cola
cola.enqueue(60)
cola.enqueue(70)

#Imprimir el tamaño de la cola nuevamente.
print("el tamaño de la cola es", cola.size)

# Eliminar y mostrar todos los elementos de la cola uno por uno.
cola.vaciar()
print("La cola está vacía")