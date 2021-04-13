import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# colocar el archivo descargado en una carpeta data en donde se encuentra el notebook, 
# renombrarlo a encuesta_sueldos.csv y ejecutar
df_sueldos = pd.read_csv('C:\Users\Chelo\Desktop\UTN 2021\Inteligencia Artificial\encuesta_sueldos.csv', header=10)

df_sueldos[:2]