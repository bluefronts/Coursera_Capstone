#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!conda install -c conda-forge geopy --yes
import requests
import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup as bs
from geopy.geocoders import Nominatim


# In[76]:


# we try to get Chinatown location first


# with open('newyork_data.json') as json_data:
#     newyork_data = json.load(json_data)

# In[5]:


neighborhoods_data = newyork_data['features']
#take a look at structure in feature
newyork_data['features'][1]


# In[6]:


# define the dataframe columns
column_names = ['Borough', 'Neighborhood', 'Latitude', 'Longitude'] 

# instantiate the dataframe
neighborhoods = pd.DataFrame(columns=column_names)


# In[7]:


#get all info into dataframe
for x in neighborhoods_data:
    borough = x['properties']['borough'] 
    neighborhood_name = x['properties']['name']
        
    neighborhood_latlon = x['geometry']['coordinates']
    neighborhood_lat = neighborhood_latlon[1]
    neighborhood_lon = neighborhood_latlon[0]
    
    neighborhoods = neighborhoods.append({'Borough': borough,
                                          'Neighborhood': neighborhood_name,
                                          'Latitude': neighborhood_lat,
                                          'Longitude': neighborhood_lon}, ignore_index=True)


# In[8]:


neighborhoods.head(20)


# In[9]:


neighborhoods.loc[neighborhoods['Neighborhood']=='Chinatown']


# In[10]:


#get chinatown latitude and longtitude
latitude=neighborhoods.iloc[100,-2]
longitude=neighborhoods.iloc[100,-1]
print('Chinatown in New York is at ({},{})'.format(latitude,longitude))


# In[11]:


#next, use explore function in Foursquare API to find 100 Chinese Restaurant


# In[12]:


#Although we can use parameter 'categoryId' to filter all Chinese Restaurant, but we increase difficulty by manually filtering in another endpoint 'VenueDetails'
CLIENT_ID='0BPBI1NPMF11CVC2IP2AOOGYLSCFZIZCHTN4UKHQJCCFVHFN'
CLIENT_SECRET='5S1BMTKQ50OSBHWTO1EAHRBTOYBXPGZLIR1G1SZUFIBU103F'
VERSION='20200701'
radius=5000
LIMIT=200
categoryId='4d4b7105d754a06374d81259'
url = 'https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v={}&radius={}&limit={}&categoryId={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, radius, LIMIT,categoryId)
url


# In[13]:


results = requests.get(url).json()


# In[14]:


df_init=[]


# In[15]:


columnname=['NAME','ID','ADDRESS']


# In[16]:


df_init=pd.DataFrame(columns=columnname)
df_init


# In[17]:


#use for loop to add all results into dataframe, note that due to limit by API, we can only retrive 100 spots at one time
for item in results['response']['groups'][0]['items']:
    NAME=item['venue']['name']
    ID=item['venue']['id']
    try:
        ADDRESS=item['venue']['location']['address']
    except:
        ADDRESS='N/A'
    df_init=df_init.append({'NAME':NAME,'ID':ID,'ADDRESS':ADDRESS},ignore_index=True)
df_init


# In[17]:


#now we use id in each row and Premium endpoint of Foursquare API ' https://api.foursquare.com/v2/venues/VENUE_ID' to search for categories,price tier,likes count,rating,
#ratingSignals,likes count,popular timeframe,latitude,longitude
#1. we use a function to find out Chinese Restaurant and Non-Chinese Restaurant 
#2. we use first for loop to filter the most liked tip
#3. we use second for loop to combine all popular timeframe into one,cos timeframes can be more than one


# In[18]:


#1. we use a function to find out Chinese Restaurant and Non-Chinese Restaurant,cos one venue can have more than one categories, so we use for loop to filter all categories
def if_cnr(venue_input):
    
        list1=[]
        try:
            for item in venue_input['response']['venue']['categories']:
                x=('4bf58dd8d48988d145941735' in item['id'])
                list1.append(x)
            if True in list1:
                return 'Chinese Restaurant'
            else:
                return 'Non-Chinese Restaurant'
        except:
            return 'N/A'


# In[20]:


#Use one venue id to take a look at its structure
url_venue='https://api.foursquare.com/v2/venues/{}?&client_id={}&client_secret={}&v={}'.format('585164b77220e62219c9aeb6',CLIENT_ID, CLIENT_SECRET,VERSION)
print(url_venue)
venue_detail=requests.get(url_venue).json()
venue_detail['response']['venue']


# In[ ]:


#testing tips API
url_tips='https://api.foursquare.com/v2/venues/{}/tips?&sort=popular&client_id={}&client_secret={}&v={}'.format('4fd38a04e4b065401a9aaf88',CLIENT_ID, CLIENT_SECRET,VERSION)
print(url_tips)
tips_detail=requests.get(url_tips).json()
tips_detail['response']['tips']['items'][0]['agreeCount']


# #2. we use first for loop to filter the most liked tip
# #3. we use second for loop to combine all popular timeframe into one,cos timeframes can be more than one
# #4. Due to venues details are not the same, for example, some have tips some don't, so we use try/except to catach some details in case errors occur
# 
# df=df_init
# df['Category']=''
# df['Price_Tier']=''
# df['Likes_Count']=''
# df['Rating']=''
# df['Rating_Signals']=''
# df['Tips']=''
# df['Agree_Count']=''
# df['Polular_Timeframe_Today']=''
# df['Latitude']=''
# df['Longitude']=''
# 
# for index,row in df_init.iterrows():
#     id_venue=row['ID']
#     url_venue='https://api.foursquare.com/v2/venues/{}?&client_id={}&client_secret={}&v={}'.format(id_venue,CLIENT_ID, CLIENT_SECRET,VERSION)
#     url_tips='https://api.foursquare.com/v2/venues/{}/tips?&sort=popular&client_id={}&client_secret={}&v={}'.format(id_venue,CLIENT_ID, CLIENT_SECRET,VERSION)
#     venue_detail=requests.get(url_venue).json()
#     tips_detail=requests.get(url_tips).json()
#     #deal with categories function
#     Category=if_cnr(venue_detail)
#     #deal with other parameters
#     try:
#         Price_Tier=venue_detail['response']['venue']['price']['tier']
#     except:
#         Price_Tier='N/A'
#     try:
#         Likes_Count=venue_detail['response']['venue']['likes']['count']
#     except:
#         Likes_Count='N/A'
#     try:
#         Rating=venue_detail['response']['venue']['rating']
#     except:
#         Rating='N/A'
#     try:
#         Rating_Signals=venue_detail['response']['venue']['ratingSignals']
#     except:
#         Rating_Signals='N/A'
#     #use API parameter 'sort=popular' to retrive most liked tips
#     Tips=''
#     Agree_Count=0
#     try:
#         Tips=tips_detail['response']['tips']['items'][0]['text']
#         Agree_Count=tips_detail['response']['tips']['items'][0]['agreeCount']
#     except:
#         Agree_Count='N/A'
#         Tips=='N/A'
# 
#     #deal with today's popular timeframes,combine all timeframe into one
#     Polular_Timeframe_Today=''
#     try:
#         for y in venue_detail['response']['venue']['popular']['timeframes'][0]['open']:
#             Polular_Timeframe_Today+=y['renderedTime']
#     except:
#         Polular_Timeframe_Today='N/A'
#     
#     try:
#         Latitude=venue_detail['response']['venue']['location']['lat']
#         Longitude=venue_detail['response']['venue']['location']['lng']
#     except:
#         Latitude='N/A'
#         Longitude='N/A'
#     #all retrived data into columns
#     row['Category']=Category
#     row['Price_Tier']=Price_Tier
#     row['Likes_Count']=Likes_Count
#     row['Rating']=Rating
#     row['Rating_Signals']=Rating_Signals
#     row['Tips']=Tips
#     row['Agree_Count']=Agree_Count
#     row['Polular_Timeframe_Today']=Polular_Timeframe_Today
#     row['Latitude']=Latitude
#     row['Longitude']=Longitude
# 

# In[74]:


# show dataframe
df.head()


# In[35]:


# take out rating=N/A items
df1=df[df['Rating']!='N/A']
df1


# In[36]:


#sort by rating for next analysis
df2=df1.sort_values(by='Rating', ascending=False)
df2


# In[37]:


#we only trace top 20 rating places
df3=df2[0:21]
df3


# In[38]:


#install and import folium function
#! conda install -c conda-forge folium
import folium 
import webbrowser
from folium.plugins import MarkerCluster


# In[66]:


# create map of New York using latitude and longitude values
# https://python-visualization.github.io/folium/quickstart.html
map_chinatown = folium.Map(location=[latitude, longitude], zoom_start=14)
map_chinatown


# In[67]:


# add markers to map
for name, lat, lng, rating, address,price_tier, Polular_Timeframe_Today in zip(df3['NAME'],df3['Latitude'], df3['Longitude'], df3['Rating'], df3['ADDRESS'],df3['Price_Tier'],df3['Polular_Timeframe_Today']):
    label = 'Rating:{}, Address:{}, Price_Tier:{},\n Avoid Time:{}'.format(rating,address,price_tier,Polular_Timeframe_Today )
    tooltip= '{}'.format(name)
    if price_tier==1 or price_tier==2:
        folium.Marker([lat, lng],popup=label,icon=folium.Icon(color='blue',icon='info-sign'),tooltip=tooltip).add_to(map_chinatown)
    elif price_tier==3 or price_tier==4:
        folium.Marker([lat, lng],popup=label,icon=folium.Icon(color='red',icon='info-sign'),tooltip=tooltip).add_to(map_chinatown)
    else:
        folium.Marker([lat, lng],popup=label,icon=folium.Icon(color='black',icon='info-sign'),tooltip=tooltip).add_to(map_chinatown)
        
map_chinatown


# In[72]:


# add clusters into map
map_chinatown = folium.Map(location=[latitude, longitude], zoom_start=14)


# In[73]:


marker_cluster = folium.plugins.MarkerCluster().add_to(map_chinatown) 
for index, row in df3.iterrows():
    locationlist = row[['Latitude','Longitude']].values.tolist()
    tooltip= '{}'.format(name)
    if row['Price_Tier']==1 or row['Price_Tier']==2:
        folium.Marker(location=locationlist, popup='Address:{}, Rating:{}, Price Tier:{},/n Avoid Time:{}'.format(row['ADDRESS'],row['Rating'],row['Price_Tier'],row['Polular_Timeframe_Today']), icon=folium.Icon(color='green', icon='ok-sign'),tooltip=tooltip).add_to(marker_cluster)
    elif row['Price_Tier']==3 or row['Price_Tier']==4:
        folium.Marker(location=locationlist, popup='Address:{}, Rating:{}, Price Tier:{},/n Avoid Time:{}'.format(row['ADDRESS'],row['Rating'],row['Price_Tier'],row['Polular_Timeframe_Today']), icon=folium.Icon(color='red', icon='ok-sign'),tooltip=tooltip).add_to(marker_cluster)
    else:
        folium.Marker(location=locationlist, popup='Address:{}, Rating:{}, Price Tier:{},/n Avoid Time:{}'.format(row['ADDRESS'],row['Rating'],row['Price_Tier'],row['Polular_Timeframe_Today']), icon=folium.Icon(color='black', icon='ok-sign'),tooltip=tooltip).add_to(marker_cluster)
map_chinatown
    


# In[ ]:


# Finally,we have:
# 1. A intuitive map with top 20 rating restaurants around Chinatown in NY
# 2. If there are more than two restaurants nearby one location, there will be clucters button to click
# 3. We can mouseover to those locations to see their names
# 4. We can choose different price tiers by looking at their colors, green means cheap, red means a bit expensive, black means we dont have price info of these locations
# 5. By clicking those locations we can see details of address,rating,price tier and popular time frame to avoid queuing

