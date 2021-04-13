import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data_url2= 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
covid_mundial = pd.read_csv(data_url2)
print(covid_mundial.head())

filtro1 = covid_mundial['Country/Region']
#print(filtro1)

filtro_argentina = covid_mundial[filtro1 == 'Brazil']
#print(filtro_argentina)

filtro_españa = covid_mundial[filtro1 == 'US']

x_dias = np.linspace(1,444,444)
print(len(x_dias))

y_argentina = filtro_argentina.iloc[0:1,6:].values
#print(y_argentina)
y_argentina = y_argentina[0]
print(len(y_argentina))

y_españa = filtro_españa.iloc[0:1,6:].values
y_españa = y_españa[0]
print(len(y_españa))

plt.plot(x_dias,y_argentina, label='n contagios Argentina')
plt.plot(x_dias,y_españa, label='n contagios España')
plt.legend(loc='best', numpoints=1) 
plt.title("Curva de contagios en Argentina y España")
plt.xlabel("441 dias")
plt.show()