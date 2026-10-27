import numpy as np

numeros = np.array([10, 20, 30, 40, 50])

print(numeros)
print (numeros * 2)
print (numeros + 5)

##############################################
# notas 
notas = np.array(
    [[7.5, 8.0, 6.5, 9.0, 5.5],[4.4, 6.7, 8.9, 7.2, 5.1],[9.5, 8.3, 7.1, 6.0, 5.8]]
    )
print(notas.max(axis=1))
print(notas.min(axis=1))
print(notas.mean(axis=1))


#########################
# calificaciones
calificaciones = np.array([
    [8.5, 7.0, 9.5],
    [6.0, 7.5, 8.0],
])
print("notas de los estudiantes")
print(calificaciones.shape)
print(calificaciones[0])
#carlos
print(calificaciones[:, 1])

################################################3
# celsius 

celsius = np.array([18, 22, 25, 19,30])
fahrenheit = (celsius * 9/5 + 32) 