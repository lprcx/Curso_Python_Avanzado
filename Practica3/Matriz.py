import numpy as np

def crear_matriz():
    mat = np.random.randint(1,100, size=(4, 4))
    print(mat)

matriz = [[5, 6, 7],
          [8, 9, 4],
          [1, 2, 3]]
    
def imprimir_matriz(matriz):
    dibujo = ''
    _fila = 0

    for fila in matriz:
        dibujo += '['
        for columna in fila:
            dibujo += f'{str(columna)},'
        dibujo = dibujo[:len(dibujo) - 1]
        dibujo += f'] \n'
        _fila += 1

    return dibujo



# Suma de matrices
def sumar_matrices():
    matriz1 = [[32, 43, 65],
            [83, 43, 27],
            [93, 32, 74]]  
    matriz2 = [[32, 10, 39],
            [92, 54, 43],
            [48, 73, 37]] 

    np_matriz1 = np.array(matriz1)
    np_matriz2 = np.array(matriz2)

    np_result = np_matriz1 + np_matriz2
    print(np_result)

def multiplicar_matrices():
    matriz1 = [[3, 4, 6],
            [8, 4, 2],
            [9, 3, 7]]  
    matriz2 = [[3, 1],
            [2, 4],
            [4, 7]] 
    
    np_matriz1 = np.array(matriz1)
    np_matriz2 = np.array(matriz2)

    np_result = np.dot(np_matriz1, np_matriz2)
    print(np_result)

print("Crear Matriz")
crear_matriz()
print("Imprimir Matriz")
print(imprimir_matriz(matriz))
print("Suma de matrices")
sumar_matrices()
print("Multiplicar Matrices")
multiplicar_matrices()