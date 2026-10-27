import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Notas de un grupo
notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 8.5])
print("Promedio:", notas.mean())
print("Máximo:", notas.max())
print("Mínimo:", notas.min())
print("Desviación estándar:", notas.std())

# 2. Ventas de una tienda (aumento del 10% sin bucles)
ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])
ventas_con_aumento = ventas * 1.10
total_semana = ventas_con_aumento.sum()
print("Ventas con aumento:", ventas_con_aumento)
print("Total de la semana:", total_semana)

# 3. Pronóstico del clima (Celsius a Fahrenheit en una línea)
celsius = np.array([18, 22, 25, 19, 30])
fahrenheit = celsius * 9/5 + 32
print("Clima en Fahrenheit:", fahrenheit)

# 4. Calificaciones por estudiante y materia
calificaciones = np.array([
    [8.5, 7.0, 9.0, 8.0], # Carlos
    [6.0, 7.5, 8.0, 7.0], # Ana
    [9.0, 8.5, 9.5, 9.0], # Luis
])
print("Promedio de cada estudiante (filas):", calificaciones.mean(axis=1))
print("Promedio de cada materia (columnas):", calificaciones.mean(axis=0))


inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}

# 5. Explorar el inventario
df_inventario = pd.DataFrame(inventario)
print("Primeras filas:")
print(df_inventario.head())
print("Forma (shape):", df_inventario.shape)
print("Columnas:", df_inventario.columns.tolist())
print("Estadísticas:")
print(df_inventario.describe())

# 6. Productos por reponer (stock < 10)
print("Productos con stock menor a 10:")
print(df_inventario[df_inventario['stock'] < 10])

# 7. Valor del inventario y columna reponer
df_inventario['valor_inventario'] = df_inventario['precio'] * df_inventario['stock']
df_inventario['reponer'] = df_inventario['stock'] < 10
print("DataFrame con nuevas columnas:")
print(df_inventario)

# 8. Ordenar del más caro al más barato y calcular precio promedio
df_ordenado = df_inventario.sort_values(by='precio', ascending=False)
print("Ordenado por precio descendente:")
print(df_ordenado)
print("Precio promedio de los productos:", df_inventario['precio'].mean())

# 9. Guardar y leer desde un archivo CSV
df_inventario.to_csv("inventario.csv", index=False)
df_leido = pd.read_csv("inventario.csv")
print("¿Son iguales los DataFrames?", df_inventario.equals(df_leido))



#scikit-learn
datos = {
    "edad": [18, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    "ingreso": [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5],
    "compro": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
}

df_datos = pd.DataFrame(datos)
X = df_datos[['edad', 'ingreso']]
y = df_datos['compro']

# 10. Dividir datos (80% / 20%), entrenar y evaluar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
print("Precisión del modelo (test_size=0.2):", accuracy_score(y_test, y_pred))

# 11. Probar con clientes nuevos
clientes_nuevos = pd.DataFrame({
    "edad": [28, 52],
    "ingreso": [2.2, 4.8]
})
predicciones = modelo.predict(clientes_nuevos)
print("Predicciones para clientes nuevos:")
for i, pred in enumerate(predicciones):
    resultado = "Sí compra" if pred == 1 else "No compra"
    print(f"Cliente {i+1} (Edad: {clientes_nuevos.iloc[i]['edad']}, Ingreso: {clientes_nuevos.iloc[i]['ingreso']}M): {resultado}")

# 12. Experimentar con la división de datos (test_size 0.3 y 0.5)
print("Experimentando con la división de datos:")
for test_size in [0.3, 0.5]:
    X_train_exp, X_test_exp, y_train_exp, y_test_exp = train_test_split(X, y, test_size=test_size, random_state=42)
    modelo_exp = LogisticRegression()
    modelo_exp.fit(X_train_exp, y_train_exp)
    y_pred_exp = modelo_exp.predict(X_test_exp)
    print(f"Precisión con test_size={test_size}: {accuracy_score(y_test_exp, y_pred_exp)}")

##
#RETRO INTEGRADO

estudiantes = {
    "horas_estudio": [2, 4, 5, 6, 8, 10, 3, 7, 9, 1],
    "asistencia": [60, 70, 75, 80, 90, 95, 65, 85, 92, 50],
    "aprobo": [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
}

# Parte Pandas
df_estudiantes = pd.DataFrame(estudiantes)
print("Estadísticas (describe):")
print(df_estudiantes.describe())

df_estudiantes['promedio_semanal'] = df_estudiantes['horas_estudio'] / 7
print("DataFrame con promedio semanal:")
print(df_estudiantes)

aprobados_bajas_horas = df_estudiantes[(df_estudiantes['aprobo'] == 1) & (df_estudiantes['horas_estudio'] < 6)]
print("Estudiantes que aprobaron con menos de 6 horas de estudio:")
print(aprobados_bajas_horas)

# Parte NumPy
asistencia_np = np.array(estudiantes['asistencia'])
print("Análisis de Asistencia (NumPy):")
print("Promedio de asistencia:", asistencia_np.mean())
print("Desviación estándar de asistencia:", asistencia_np.std())

# Parte Scikit-learn
X_reto = df_estudiantes[['horas_estudio', 'asistencia']]
y_reto = df_estudiantes['aprobo']

X_tr, X_te, y_tr, y_te = train_test_split(X_reto, y_reto, test_size=0.2, random_state=42)
modelo_reto = LogisticRegression()
modelo_reto.fit(X_tr, y_tr)

y_pr = modelo_reto.predict(X_te)
print("Precisión del modelo en el reto:", accuracy_score(y_te, y_pr))

aprendiz_nuevo = pd.DataFrame({
    "horas_estudio": [5],
    "asistencia": [78]
})
prediccion_aprendiz = modelo_reto.predict(aprendiz_nuevo)
resultado_final = "Aprueba" if prediccion_aprendiz[0] == 1 else "No aprueba"
print(f"Predicción para aprendiz (5 horas, 78% asistencia): {resultado_final}")