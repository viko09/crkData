import corsikaio
import pandas as pd

# Importing the data obtained from the simulations
f = corsikaio.CorsikaParticleFile('gamma/gamma0_J10DAT000010')
# This is the number of showers
print('Showers: ', f.run_header['run_number'])

print("---------------------------------------------------------------")

print('version:')
print(f.version)

print("---------------------------------------------------------------")

# Now import the complete file
data = corsikaio.CorsikaFile('gamma/gamma0_J10DAT000010')
# Give us the class of our file
print('EventClass: ', data.EventClass)
# Esto nos muestra el numero de lluvias
print('Run Number, Run Header: ', data.run_header['run_number'])

print("---------------------------------------------------------------")

# Now we import our data as a DataFrame by pandas
obj1 = pd.DataFrame(data)
print('Data Frame: ', obj1.head(), '\n')
print('Values: ', obj1.values)

print("---------------------------------------------------------------")

# Importamos los datos a pandas como un dataframe
obj2 = pd.DataFrame(f)
print(obj2.head(), '\n')
print(obj1.values)

print("---------------------------------------------------------------")

# Nos da un arreglo (x, y) x es el número de filas y y el de columnas
shape = obj1.shape
# In this case, we obtain an array of (10000 , 4)
print(shape)

print("---------------------------------------------------------------")

# Nos da un arreglo (x, y) x es el número de filas y y el de columnas
shape = obj2.shape
# En este caso obtenemos una tupla (10000 , 4)
print(shape)

print("---------------------------------------------------------------")

# Dividiremos nuestros datos en un x (entrada) y un y (salida). Cortamos secciones
features = obj1.iloc[:, obj1.columns == 'longitudinal']
print(features)

# El orden va [fila, columna] [inicio:fin, inicio:fin] empieza t contar desde cero [incluido, excluido]

print("---------------------------------------------------------------")

# Buscamos definir la variable dependiente
label = obj1.iloc[:, obj1.columns == 'particles']  # Variable dependiente
print(label)

print("---------------------------------------------------------------")

# Concatenar columnas: Obtenemos un x y y que será utilizados para la obtención del
# modelo de regresión lineal

dataset = pd.concat([features, label], axis=1)
print(dataset)

print("---------------------------------------------------------------")

# Obtenemos un arreglo de los datos juntos
# print(np.array(obj1))

print("---------------------------------------------------------------")

# Imprimimos los nombres de las columnas de nuestros datos
print(obj1.columns)

print("---------------------------------------------------------------")
