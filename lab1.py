import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

# set period
date_from = '2018-01-01'
date_to = '2018-01-30'

# method which takes data from json.
def fetch_currency(currency,beg,end):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + currency + "/" + date_from + "/" + date_to + "/"
    currency_req = requests.get(url)
    currency_data = currency_req.json()
    return currency_data['rates']

# Use fetch_currency for load data
result1 = fetch_currency('USD',date_from,date_to)
result2 = fetch_currency('EUR',date_from,date_to)

# take first 10 elements and convert to dict
rate_dataframe1 = pd.DataFrame.from_dict(result1).head(10)
rate_dataframe2 = pd.DataFrame.from_dict(result2).head(10)

#set keys
plot_data1 = rate_dataframe1.set_index(['effectiveDate'])['mid']
plot_data2 = rate_dataframe2.set_index(['effectiveDate'])['mid']

# compute correlation.
correlation = np.corrcoef (plot_data1, plot_data2)[0][1]

# print data 
plt.plot(plot_data1, 'g--', plot_data2,'b--')
plt.ylim(ymin=0)
plt.title('Korelacja {} do {} = {}'.format(currency1, currency2, correlation))
plt.ylabel('Wartość w PLN')
plt.xlabel('Data')
plt.legend([currency1, currency2], loc='lower right')
plt.show()
