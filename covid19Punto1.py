import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data_url= 'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
covid_df = pd.read_csv(data_url)
x_dia_inicio = covid_df['dia_cuarentena_dnu260'].values

y = covid_df['tot_casosconf'].values

y_contagios = covid_df['tot_casosconf'].values
y_fallecidos = covid_df['tot_fallecidos'].values

plt.plot(x_dia_inicio,y_contagios, label='n contagios')
plt.plot(x_dia_inicio,y_fallecidos, label='n decesos')
plt.legend(loc='best', numpoints=1) 
plt.title("Curva de contagios en Argentina")
plt.xlabel("Días desde el primer dia de cuarentena")
plt.show()