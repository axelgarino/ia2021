import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data_url= 'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
covid_df = pd.read_csv(data_url)

df = pd.DataFrame(covid_df)
filter1 = df[df['osm_admin_level_4'].str.contains("Córdoba", case=False)]
#filter1 = df[df['osm_admin_level_4'] == "Córdoba"

x_dia_inicio = filter1['dia_inicio'].values

y_contagios = filter1['nue_casosconf_diff'].values

y_fallecidos = filter1['nue_fallecidos_diff'].values

plt.plot(x_dia_inicio,y_contagios, label='n contagios')
plt.plot(x_dia_inicio,y_fallecidos, label='n decesos')
plt.legend(loc='best', numpoints=1) 
plt.title("Curva de contagios en Argentina")
plt.xlabel("Cordoba")
plt.show()