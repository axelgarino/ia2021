import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data_url= 'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
covid_df = pd.read_csv(data_url)

x_dia_inicio = covid_df['dia_inicio'].values
y_nuevos_casos = covid_df['nue_casosconf_diff'].values

plt.plot(x_dia_inicio,y_nuevos_casos , label='n casos por dia')
plt.legend(loc='best', numpoints=1) 
plt.title("Cantidad casos confirmados por dia en Argentina")
plt.xlabel("Días desde el primer dia de cuarentena")
plt.show()