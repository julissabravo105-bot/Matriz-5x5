#Crear la matriz de 3 filas y 4 columnas con todo los asientos libres(0) reservado(1)
asientos=[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
print("BIENVENIDO🌟")
#Solicitar al usuario la fila del asiento a reservar
#Convertimos la entrada a entero con int()
fila= int(input("Ingrese el número de fila (0 a 2):"))
columna=int(input("Ingrese el numero de columna (0 a 3):"))
#Marcar el asiento seleccionado como reservado (cambiar de o a 1)
asientos[fila][columna] = 1
 

print("Estado de la sala:")
#Recorrer cada fila de la sala
for fila in asientos: 
 #Recorrer cada asiento dentro de la fila actual
 for asientos in fila: 
  print(asientos, end=" ")#Imprime sin salto de línea
 print() 
