import pandas as pd	#Imports calculation properties
import numpy as np	#Imports calculation with arrays properties
import matplotlib.pyplot as plt #Imports graph plotting properties
import seaborn as sns  #Imports graph plotting properties
path= "Enter Path to CSV file"

plt.rcParams['figure.figsize'] = [8,5]
plt.rcParams['font.size'] =14
plt.rcParams['font.weight']= 'bold'
plt.style.use('seaborn-whitegrid')

df= pd.read_csv(path)
print("Number of dataset: ",df.shape)
print('')
df.head()
