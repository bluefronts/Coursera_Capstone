#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install lxml


# In[2]:


pip install beautifulsoup4


# In[3]:


url='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'


# In[4]:


import requests


# In[5]:


html=requests.get(url).text


# In[6]:


from bs4 import BeautifulSoup as bs


# In[7]:


soup = bs(html,'lxml')


# In[8]:


import pandas as pd
rawdata=[]
columnname=['PostCode','Borough', 'Neighborhood']
df=pd.DataFrame(columns=columnname)
df


# In[9]:


for x in soup.table.find_all('tr')[1:]:
    postcode=x.find('td').get_text().strip()
    borough=x.find('td').find_next().get_text().strip()
    neighboohood=x.find('td').find_next().find_next().get_text().strip()
    df=df.append({'PostCode':postcode,'Borough':borough,'Neighborhood':neighboohood},ignore_index=True)


# In[10]:


df


# In[11]:


#Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned.
df=df[df.Borough != 'Not assigned']
df


# In[12]:


#More than one neighborhood can exist in one postal code area. For example, in the table on the Wikipedia page, 
#you will notice that M5A is listed twice and has two neighborhoods: Harbourfront and Regent Park. 
#These two rows will be combined into one row with the neighborhoods separated with a comma as shown in row 11 in the above table.


# In[13]:


#def combine(df):
    #return','.join(df.values)

#df=df.groupby(['PostCode'])['Neighborhood'].apply(combine)
#df


# In[14]:


#If a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough.
for row in range(len(df)):
    if df.iloc[row,-1]=='Parkwoods':
        df.iloc[row,-1]=df.iloc[row,-2]


# In[15]:


df.shape


# In[16]:


pip install geocoder


# In[17]:


df2=pd.read_csv('Geospatial_Coordinates.csv')


# In[19]:


df2


# In[20]:


df2.rename(columns={'Postal Code':'PostCode'},inplace=True)
df2


# In[22]:


df_merged=df.merge(df2,on='PostCode')
df_merged


# In[ ]:




