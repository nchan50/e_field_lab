# libraries
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
 
 
# Get the data 
data = pd.read_csv('e_field.csv')
 
# Transform it to a long format
df=data.unstack().reset_index()
df.columns=["X","Y","Z"]
 
# Rescale the spreadsheet rows and columns to centimeters
df['X']=pd.Categorical(df['X'])

df['X']=df['X'].cat.codes*2 +1

df['Y']=pd.Categorical(df['Y'])

df['Y']=df['Y'].cat.codes*2 +1


data = df.values.tolist()

fields = [[0 for y in range(7)] for x in range(10)]
for x in range(len(fields)):
    for y in range(len(fields[x])):
        Ex = -1 * (data[9 * (x+2) + y + 1][2] - data[9 * x + y + 1][2])
        Ey = -1 * (data[9 * (x+1) + y + 2][2] - data[9 * (x+1) + y][2])
        plt.quiver(x * 2 + 1, y * 2 + 1, Ex, Ey, scale=23)
        
plt.xlabel('X coordinate (cm)')
plt.ylabel('Y coordinate (cm)')
plt.title('Electric Field Vectors')

plt.grid()
plt.show()
