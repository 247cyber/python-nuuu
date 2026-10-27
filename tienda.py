import pandas as pd   
from sklearn.tree import DecisionTreeClassifier

df = pd.read_excel("ia.xlsx")
# Definir X (características) y y (objetivo)
x = df[['valor']]  
y = df['compra']    

modelo = DecisionTreeClassifier(random_state=42)

modelo.fit(x,y)
# Predicción para un nuevo ingreso
prediccion = modelo.predict(pd.DataFrame({"valor": [80000]}))

if prediccion[0] == 1:
    print("el cine se puede comprar")
else:
    print("el cliente no podria pagar")