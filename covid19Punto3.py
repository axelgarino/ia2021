import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data_url= 'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
covid_df = pd.read_csv(data_url)

filtro1 = covid_df['tot_casosconf'] > 200
#print(filtro1)

filtro_covid = covid_df[filtro1]
#print(filtro_covid)

x_dia_inicio = filtro_covid['dia_inicio'].values

y_total_casos = filtro_covid['nue_casosconf_diff'].values
#print(y_total_casos)

plt.plot(x_dia_inicio,y_total_casos , label='n° de casos por dia')
plt.legend(loc='best', numpoints=1) 
plt.title("Total casos confirmados en Argentina")
plt.xlabel("Días desde el contagio n°200")
plt.show()