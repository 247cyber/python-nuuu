import numpy as np
# materias de estudiantes 
materias = np.array(
    [   # notas materias de cada estudiante
        [2.7, 3.5, 4.0], #angy
        [4.5, 3.8, 4.2], #luis
        [3.9, 4.1, 3.7], #kevin
        [3.3, 3.6, 3.4]  #carlos
    ]  
)
print("Promedio Estudiantes:", materias.mean(axis=1))
print("Promedio Materias:   ", materias.mean(axis=0))

