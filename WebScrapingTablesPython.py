#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area').text


# In[2]:


#conda install lxml
#conda install html5lib
from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())


# In[3]:


My_table = soup.find('table',{'class':'wikitable sortable'})
My_table


# In[4]:


links = My_table.findAll('a')
links


# In[26]:


countriesByAreaList = []

for tr in My_table.find_all('tr')[1:]:
    countriesByAreaList.append({
        'Rank': tr.find_all('td')[0].text.replace("\n", ""),
        'Area': tr.find_all('td')[2].text.replace("\n", ""),
        'Notes': tr.find_all('td')[3].text.replace("\n", "")
    })

countriesByAreaList


# In[ ]:


Countries = []
for link in links:
    Countries.append(link.get('title'))
    
print(Countries)


# In[31]:


import pandas as pd
dfCountriesByArea = pd.DataFrame(countriesByAreaList, columns =['Rank', 'Area', 'Notes']) 

dfCountriesByArea


# In[ ]:


import pandas as pd
df = pd.DataFrame()
df['Country'] = Countries

df


# In[32]:


dfCountriesByArea.to_csv(r'/tmp/countriesByArea.csv', sep='|', index = None, header=True)


# In[ ]:


df.to_csv(r'/tmp/countries.csv', sep='|', index = None, header=True)


# In[ ]:


df.to_csv(r'/tmp/countries.csv', sep='|', header=True)

