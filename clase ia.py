import numpy as np
from sklearn.linear_model import LinearRegression

x_metros_cuadrados = np.array([[50], [60], [70], [80], [90]])


y_precio = np.array([150000, 180000, 210000, 240000, 270000])

modelo_prediccion = LinearRegression()
modelo_prediccion.fit(x_metros_cuadrados, y_precio) 

nueva_casa = np.array([[100]])
precio_predicho = modelo_prediccion.predict(nueva_casa)

# Ahora precio_predicho[0] será directamente el número flotante
print(f"Para una casa de 100 m², el precio estimado es: {precio_predicho[0]:.2f} millones de pesos")