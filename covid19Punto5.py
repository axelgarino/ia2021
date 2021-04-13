import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data_url= 'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
covid_df = pd.read_csv(data_url)

filtro_provincias = covid_df['osm_admin_level_4']

filtro_cordoba = covid_df[filtro_provincias=='Córdoba']
#print(filtro_cordoba)

x_dia_inicio = filtro_cordoba['dia_inicio'].values

y_filtro_cordoba = filtro_cordoba['nue_casosconf_diff'].values

plt.plot(x_dia_inicio,y_filtro_cordoba , label='n casos por dia')
plt.legend(loc='best', numpoints=1) 
plt.title("Cantidad casos por dia en Cordoba")
plt.xlabel("Días desde el primer contagio")
plt.show()