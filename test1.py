import corsikaio
import pandas as pd

# Importing the data obtained from the simulations
data = corsikaio.CorsikaParticleFile('gamma/gamma0_J10DAT000010')

print("---------------------------------------------------------------")

# Now we import our data as a DataFrame by pandas
obj1 = pd.DataFrame(data)

print("---------------------------------------------------------------")

# Gives an array (x, y) x is the number of rows and y number of cols
shape = obj1.shape
# In this case, we obtain an array of (10000 , 4)
print(shape)

print("---------------------------------------------------------------")

#  We are going to divide our dataset in x (input) and y (output). Split sections
features = obj1.iloc[:, :]
print(features)

# El orden va [fila, columna] [inicio:fin, inicio:fin] empieza t contar desde cero [incluido, excluido]

print("---------------------------------------------------------------")

F = obj1.columns
print(F)
