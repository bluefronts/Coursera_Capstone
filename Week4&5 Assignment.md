```python
#!conda install -c conda-forge geopy --yes
import requests
import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup as bs
from geopy.geocoders import Nominatim
```


```python
# we try to get Chinatown location first
```

with open('newyork_data.json') as json_data:
    newyork_data = json.load(json_data)


```python
neighborhoods_data = newyork_data['features']
#take a look at structure in feature
newyork_data['features'][1]
```




    {'type': 'Feature',
     'id': 'nyu_2451_34572.2',
     'geometry': {'type': 'Point',
      'coordinates': [-73.82993910812398, 40.87429419303012]},
     'geometry_name': 'geom',
     'properties': {'name': 'Co-op City',
      'stacked': 2,
      'annoline1': 'Co-op',
      'annoline2': 'City',
      'annoline3': None,
      'annoangle': 0.0,
      'borough': 'Bronx',
      'bbox': [-73.82993910812398,
       40.87429419303012,
       -73.82993910812398,
       40.87429419303012]}}




```python
# define the dataframe columns
column_names = ['Borough', 'Neighborhood', 'Latitude', 'Longitude'] 

# instantiate the dataframe
neighborhoods = pd.DataFrame(columns=column_names)
```


```python
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
```


```python
neighborhoods.head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bronx</td>
      <td>Wakefield</td>
      <td>40.894705</td>
      <td>-73.847201</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bronx</td>
      <td>Co-op City</td>
      <td>40.874294</td>
      <td>-73.829939</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bronx</td>
      <td>Eastchester</td>
      <td>40.887556</td>
      <td>-73.827806</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bronx</td>
      <td>Fieldston</td>
      <td>40.895437</td>
      <td>-73.905643</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bronx</td>
      <td>Riverdale</td>
      <td>40.890834</td>
      <td>-73.912585</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bronx</td>
      <td>Kingsbridge</td>
      <td>40.881687</td>
      <td>-73.902818</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Manhattan</td>
      <td>Marble Hill</td>
      <td>40.876551</td>
      <td>-73.910660</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bronx</td>
      <td>Woodlawn</td>
      <td>40.898273</td>
      <td>-73.867315</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bronx</td>
      <td>Norwood</td>
      <td>40.877224</td>
      <td>-73.879391</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bronx</td>
      <td>Williamsbridge</td>
      <td>40.881039</td>
      <td>-73.857446</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Bronx</td>
      <td>Baychester</td>
      <td>40.866858</td>
      <td>-73.835798</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Bronx</td>
      <td>Pelham Parkway</td>
      <td>40.857413</td>
      <td>-73.854756</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Bronx</td>
      <td>City Island</td>
      <td>40.847247</td>
      <td>-73.786488</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Bronx</td>
      <td>Bedford Park</td>
      <td>40.870185</td>
      <td>-73.885512</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Bronx</td>
      <td>University Heights</td>
      <td>40.855727</td>
      <td>-73.910416</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Bronx</td>
      <td>Morris Heights</td>
      <td>40.847898</td>
      <td>-73.919672</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Bronx</td>
      <td>Fordham</td>
      <td>40.860997</td>
      <td>-73.896427</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Bronx</td>
      <td>East Tremont</td>
      <td>40.842696</td>
      <td>-73.887356</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Bronx</td>
      <td>West Farms</td>
      <td>40.839475</td>
      <td>-73.877745</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Bronx</td>
      <td>High  Bridge</td>
      <td>40.836623</td>
      <td>-73.926102</td>
    </tr>
  </tbody>
</table>
</div>




```python
neighborhoods.loc[neighborhoods['Neighborhood']=='Chinatown']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>100</th>
      <td>Manhattan</td>
      <td>Chinatown</td>
      <td>40.715618</td>
      <td>-73.994279</td>
    </tr>
  </tbody>
</table>
</div>




```python
#get chinatown latitude and longtitude
latitude=neighborhoods.iloc[100,-2]
longitude=neighborhoods.iloc[100,-1]
print('Chinatown in New York is at ({},{})'.format(latitude,longitude))
```

    Chinatown in New York is at (40.71561842231432,-73.99427936255978)
    


```python
#next, use explore function in Foursquare API to find 100 Chinese Restaurant
```


```python
#Although we can use parameter 'categoryId' to filter all Chinese Restaurant, but we increase difficulty by manually filtering in another endpoint 'VenueDetails'
CLIENT_ID='0BPBI1NPMF11CVC2IP2AOOGYLSCFZIZCHTN4UKHQJCCFVHFN'
CLIENT_SECRET='5S1BMTKQ50OSBHWTO1EAHRBTOYBXPGZLIR1G1SZUFIBU103F'
VERSION='20200701'
radius=5000
LIMIT=200
categoryId='4d4b7105d754a06374d81259'
url = 'https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v={}&radius={}&limit={}&categoryId={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, radius, LIMIT,categoryId)
url
```




    'https://api.foursquare.com/v2/venues/explore?client_id=0BPBI1NPMF11CVC2IP2AOOGYLSCFZIZCHTN4UKHQJCCFVHFN&client_secret=5S1BMTKQ50OSBHWTO1EAHRBTOYBXPGZLIR1G1SZUFIBU103F&ll=40.71561842231432,-73.99427936255978&v=20200701&radius=5000&limit=200&categoryId=4d4b7105d754a06374d81259'




```python
results = requests.get(url).json()
```


```python
df_init=[]
```


```python
columnname=['NAME','ID','ADDRESS']
```


```python
df_init=pd.DataFrame(columns=columnname)
df_init
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NAME</th>
      <th>ID</th>
      <th>ADDRESS</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NAME</th>
      <th>ID</th>
      <th>ADDRESS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cheeky Sandwiches</td>
      <td>4b1896caf964a52069d423e3</td>
      <td>35 Orchard St</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kiki's</td>
      <td>5521c2ff498ebe2368634187</td>
      <td>130 Division St</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Scarr's Pizza</td>
      <td>56c3c626cd106998d2b196d0</td>
      <td>22 Orchard St</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Wayla</td>
      <td>5cc4e9d0c876c8002c3010cb</td>
      <td>100 Forsyth St</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Forgtmenot</td>
      <td>4fd38a04e4b065401a9aaf88</td>
      <td>138 Division St</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Jeffrey's Grocery</td>
      <td>4ca21faa8afca09388192116</td>
      <td>172 Waverly Pl</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Buvette</td>
      <td>4d0bf7e3f29c236ac675bfe7</td>
      <td>42 Grove St</td>
    </tr>
    <tr>
      <th>97</th>
      <td>L’Accolade</td>
      <td>5d181bac17d3b9002329f126</td>
      <td>302 Bleecker St</td>
    </tr>
    <tr>
      <th>98</th>
      <td>CAVA</td>
      <td>57bcd600498e81d153625a1a</td>
      <td>143 4th Ave</td>
    </tr>
    <tr>
      <th>99</th>
      <td>4 Charles Prime Rib</td>
      <td>585164b77220e62219c9aeb6</td>
      <td>4 Charles St</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 3 columns</p>
</div>




```python
#now we use id in each row and Premium endpoint of Foursquare API ' https://api.foursquare.com/v2/venues/VENUE_ID' to search for categories,price tier,likes count,rating,
#ratingSignals,likes count,popular timeframe,latitude,longitude
#1. we use a function to find out Chinese Restaurant and Non-Chinese Restaurant 
#2. we use first for loop to filter the most liked tip
#3. we use second for loop to combine all popular timeframe into one,cos timeframes can be more than one
```


```python
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
```


```python
#Use one venue id to take a look at its structure
url_venue='https://api.foursquare.com/v2/venues/{}?&client_id={}&client_secret={}&v={}'.format('585164b77220e62219c9aeb6',CLIENT_ID, CLIENT_SECRET,VERSION)
print(url_venue)
venue_detail=requests.get(url_venue).json()
venue_detail['response']['venue']
```

    https://api.foursquare.com/v2/venues/585164b77220e62219c9aeb6?&client_id=0BPBI1NPMF11CVC2IP2AOOGYLSCFZIZCHTN4UKHQJCCFVHFN&client_secret=5S1BMTKQ50OSBHWTO1EAHRBTOYBXPGZLIR1G1SZUFIBU103F&v=20200701
    




    {'id': '585164b77220e62219c9aeb6',
     'name': '4 Charles Prime Rib',
     'contact': {'phone': '2125615992',
      'formattedPhone': '(212) 561-5992',
      'facebook': '885277744922395',
      'facebookUsername': '4charlesprimerib',
      'facebookName': '4 Charles Prime Rib'},
     'location': {'address': '4 Charles St',
      'crossStreet': 'Greenwich Ave',
      'lat': 40.735219495923204,
      'lng': -74.0006488188871,
      'labeledLatLngs': [{'label': 'display',
        'lat': 40.735219495923204,
        'lng': -74.0006488188871},
       {'label': 'entrance', 'lat': 40.735185, 'lng': -74.000661}],
      'postalCode': '10014',
      'cc': 'US',
      'city': 'New York',
      'state': 'NY',
      'country': 'United States',
      'formattedAddress': ['4 Charles St (Greenwich Ave)',
       'New York, NY 10014',
       'United States']},
     'canonicalUrl': 'https://foursquare.com/v/4-charles-prime-rib/585164b77220e62219c9aeb6',
     'categories': [{'id': '4bf58dd8d48988d1cc941735',
       'name': 'Steakhouse',
       'pluralName': 'Steakhouses',
       'shortName': 'Steakhouse',
       'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/steakhouse_',
        'suffix': '.png'},
       'primary': True}],
     'verified': False,
     'stats': {'tipCount': 57},
     'url': 'http://www.nycprimerib.com',
     'likes': {'count': 217,
      'groups': [{'type': 'others', 'count': 217, 'items': []}],
      'summary': '217 Likes'},
     'dislike': False,
     'ok': False,
     'rating': 9.3,
     'ratingColor': '00B551',
     'ratingSignals': 270,
     'allowMenuUrlEdit': True,
     'beenHere': {'count': 0,
      'unconfirmedCount': 0,
      'marked': False,
      'lastCheckinExpiredAt': 0},
     'specials': {'count': 0, 'items': []},
     'photos': {'count': 145,
      'groups': [{'type': 'venue',
        'name': 'Venue photos',
        'count': 145,
        'items': [{'id': '5e4ea442bb3fc70008d67b1c',
          'createdAt': 1582212162,
          'source': {'name': 'Swarm for Android',
           'url': 'https://www.swarmapp.com'},
          'prefix': 'https://fastly.4sqi.net/img/general/',
          'suffix': '/797590_WoGLpybFi42d4PgxKm8i1A8Ces7oKtLJS7C6ZnFaLlo.jpg',
          'width': 1440,
          'height': 1080,
          'user': {'id': '797590',
           'firstName': 'Gilbert',
           'lastName': 'M',
           'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
            'suffix': '/RWJVJ4GMQHWKIIAQ.jpg'}},
          'visibility': 'public'},
         {'id': '5e4b439ee193bd0008cb9348',
          'createdAt': 1581990814,
          'source': {'name': 'Foursquare for iOS',
           'url': 'https://foursquare.com/download/#/iphone'},
          'prefix': 'https://fastly.4sqi.net/img/general/',
          'suffix': '/399433442_tJdtaBpDY0E5dpXeOyFIPS64TJgmLaxEOg8ODLzXJAk.jpg',
          'width': 1440,
          'height': 1920,
          'user': {'id': '399433442',
           'firstName': 'Lori',
           'lastName': 'S',
           'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
            'suffix': '/399433442_nJS1rITZ_EYHEbR2LAfWsW3U4oW7l8ydJJ6EXQDXQDkkhPQZn_Ac-ydNx43NUeGiQM3FTX5Fn.jpg'}},
          'visibility': 'public'}]}]},
     'reasons': {'count': 1,
      'items': [{'summary': 'Lots of people like this place',
        'type': 'general',
        'reasonName': 'rawLikesReason'}]},
     'hereNow': {'count': 0, 'summary': 'Nobody here', 'groups': []},
     'createdAt': 1481729207,
     'tips': {'count': 57,
      'groups': [{'type': 'others',
        'name': 'All tips',
        'count': 57,
        'items': [{'id': '5d5b210b1a31830007c10db2',
          'createdAt': 1566253323,
          'text': 'Must get the French dip!',
          'type': 'user',
          'canonicalUrl': 'https://foursquare.com/item/5d5b210b1a31830007c10db2',
          'lang': 'en',
          'likes': {'count': 0, 'groups': []},
          'logView': True,
          'agreeCount': 0,
          'disagreeCount': 0,
          'todo': {'count': 0},
          'user': {'id': '134726799',
           'firstName': 'Julie',
           'lastName': 'W',
           'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
            'suffix': '/134726799-NRPPMBS0IBEXS0JV.jpg'}},
          'authorInteractionType': 'liked'},
         {'id': '5cbddce128374e002cfd92ef',
          'createdAt': 1555946721,
          'text': 'Worth waiting until 11pm for a reservation. Get the burger. Don’t overlook the apps and sides either.',
          'type': 'user',
          'canonicalUrl': 'https://foursquare.com/item/5cbddce128374e002cfd92ef',
          'photo': {'id': '5cbddce4e679bc002cf3aa54',
           'createdAt': 1555946724,
           'source': {'name': 'Foursquare for iOS',
            'url': 'https://foursquare.com/download/#/iphone'},
           'prefix': 'https://fastly.4sqi.net/img/general/',
           'suffix': '/451571718_m6rmyFbGuVrGWsEDLthkrvcVzcVMCEja6JzpIFPkrJo.jpg',
           'width': 1440,
           'height': 1920,
           'visibility': 'public'},
          'photourl': 'https://fastly.4sqi.net/img/general/original/451571718_m6rmyFbGuVrGWsEDLthkrvcVzcVMCEja6JzpIFPkrJo.jpg',
          'lang': 'en',
          'likes': {'count': 0, 'groups': []},
          'logView': True,
          'agreeCount': 0,
          'disagreeCount': 0,
          'todo': {'count': 0},
          'user': {'id': '451571718',
           'firstName': 'Kristen',
           'lastName': 'M',
           'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
            'suffix': '/451571718_MnLLN2lU_2nxhh_9upAXEol-LzefoiZ3uM0E1St93zuEzeI2_dSUeJxws4cIaijq_Ar65Qi6g.jpg'}},
          'authorInteractionType': 'liked'}]}]},
     'shortUrl': 'http://4sq.com/2gL4avj',
     'timeZone': 'America/New_York',
     'listed': {'count': 1072,
      'groups': [{'type': 'others',
        'name': 'Lists from other people',
        'count': 1072,
        'items': [{'id': '4f06192a0e0199f87c8392e4',
          'name': 'Quick, I need a date spot.',
          'description': 'My favorite date spots in various neighborhoods at various price points. Some trendy, some hidden, all relatively calm and civilized.',
          'type': 'others',
          'user': {'id': '23355',
           'firstName': 'Dan',
           'lastName': 'K',
           'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
            'suffix': '/23355-ULKIVMCI21C0M32V.jpg'}},
          'editable': False,
          'public': True,
          'collaborative': False,
          'url': '/user/23355/list/quick-i-need-a-date-spot',
          'canonicalUrl': 'https://foursquare.com/user/23355/list/quick-i-need-a-date-spot',
          'createdAt': 1325799722,
          'updatedAt': 1583879230,
          'photo': {'id': '4eadcfc9490170218c74db8a',
           'createdAt': 1320013769,
           'prefix': 'https://fastly.4sqi.net/img/general/',
           'suffix': '/Y1KLPFVKNEKQLS5GW4MW42JKAG3DZY32HXKPVAJKDH2ED4AM.jpg',
           'width': 612,
           'height': 612,
           'user': {'id': '799572',
            'firstName': 'Ben',
            'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
             'suffix': '/MQIUT4UIXC1LXX0M.jpg'}},
           'visibility': 'public'},
          'followers': {'count': 842},
          'listItems': {'count': 204,
           'items': [{'id': 'v585164b77220e62219c9aeb6',
             'createdAt': 1538699722}]}},
         {'id': '4f066f8ee5fa76365a2b7e45',
          'name': 'Favorite NYC restaurants',
          'description': 'My favorites range from formal French service to rogue smokers in the dining room under buzzing florescent lights. It all boils down to the food.',
          'type': 'others',
          'user': {'id': '23355',
           'firstName': 'Dan',
           'lastName': 'K',
           'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
            'suffix': '/23355-ULKIVMCI21C0M32V.jpg'}},
          'editable': False,
          'public': True,
          'collaborative': False,
          'url': '/user/23355/list/favorite-nyc-restaurants',
          'canonicalUrl': 'https://foursquare.com/user/23355/list/favorite-nyc-restaurants',
          'createdAt': 1325821838,
          'updatedAt': 1583544816,
          'photo': {'id': '4dff811aa12d231074fa4ef3',
           'createdAt': 1308590362,
           'prefix': 'https://fastly.4sqi.net/img/general/',
           'suffix': '/VQILTMF2AJDZISBGICA4W3RAZSPQGFOAGTK2MEUMAVTDLOQL.jpg',
           'width': 537,
           'height': 720,
           'user': {'id': '79616',
            'firstName': 'Anna',
            'lastName': 'G',
            'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
             'suffix': '/79616-FUW2PDCIHF1ZZFHF.jpg'}},
           'visibility': 'public'},
          'followers': {'count': 65},
          'listItems': {'count': 180,
           'items': [{'id': 'v585164b77220e62219c9aeb6',
             'createdAt': 1538699719}]}},
         {'id': '5a148d4df00a706b12138319',
          'name': 'These Are the 5 Best Burgers in New York City.',
          'description': 'What makes the best burger in NYC? The patty. The bun. The pickles. The cheese. It all matters.',
          'type': 'others',
          'user': {'id': '322698',
           'firstName': 'Bon Appetit Magazine',
           'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
            'suffix': '/322698-VIDHV5IKLLYBJFNU.jpg'},
           'type': 'page'},
          'editable': False,
          'public': True,
          'collaborative': False,
          'url': '/p/bon-appetit-magazine/322698/list/these-are-the-5-best-burgers-in-new-york-city',
          'canonicalUrl': 'https://foursquare.com/p/bon-appetit-magazine/322698/list/these-are-the-5-best-burgers-in-new-york-city',
          'createdAt': 1511296333,
          'updatedAt': 1512507157,
          'photo': {'id': '554bb0cc498e3a4f7a48144e',
           'createdAt': 1431023820,
           'prefix': 'https://fastly.4sqi.net/img/general/',
           'suffix': '/2974519_zkxWpIRAQ5DWvOD5t0cGGesCHVNRLTklQ7lS0uj3rWY.jpg',
           'width': 640,
           'height': 640,
           'user': {'id': '2974519',
            'firstName': 'Nick',
            'lastName': 'S',
            'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
             'suffix': '/2974519_F7i6y1AZ_NgCRCEQPRUEgrk8iqkAgKa_RySOhsHEJxFbQfywnEdxH6aJO1l1TYJRDUhstBcHN'}},
           'visibility': 'public'},
          'logView': True,
          'followers': {'count': 41},
          'listItems': {'count': 5,
           'items': [{'id': 't5a27026f0a464d3b1e4ea508',
             'createdAt': 1512506169,
             'photo': {'id': '58f93f59b6eedb771950e71b',
              'createdAt': 1492729689,
              'prefix': 'https://fastly.4sqi.net/img/general/',
              'suffix': '/18424063__SFuyvVdqBbkxDD8GiOejne0XrMF_aSLci95OvnPb-s.jpg',
              'width': 1440,
              'height': 1920,
              'user': {'id': '18424063',
               'firstName': 'Corey',
               'lastName': 'S',
               'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
                'suffix': '/18424063-DOL35A4N1OZ5S0KQ.jpg'}},
              'visibility': 'public'}}]}},
         {'id': '4e565b8cb61cabc6beb389bd',
          'name': "The Next 10 Restaurants I'll Try",
          'description': '',
          'type': 'others',
          'user': {'id': '697943',
           'firstName': 'Noah',
           'lastName': 'W',
           'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
            'suffix': '/697943_jQx3rpaR_DmCtX0lbxNf3D3idRsUdoFl_feXc4MkLlYeHO5BkTZg0NY0SXHF9tYgq50UFxsnx.jpg'}},
          'editable': False,
          'public': True,
          'collaborative': False,
          'url': '/noah_weiss/list/the-next-10-restaurants-ill-try',
          'canonicalUrl': 'https://foursquare.com/noah_weiss/list/the-next-10-restaurants-ill-try',
          'createdAt': 1314282380,
          'updatedAt': 1583028933,
          'photo': {'id': '55784cc0498e3314aa2dc6e9',
           'createdAt': 1433947328,
           'prefix': 'https://fastly.4sqi.net/img/general/',
           'suffix': '/131079914_wTdkkQVzAlHQOj6skSUT3GLCBigzDFuo5_LZ7TqaZzk.jpg',
           'width': 1500,
           'height': 1000,
           'user': {'id': '131079914',
            'firstName': 'Fuku',
            'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',
             'suffix': '/131079914_RD4NrFK1_bQ96eHYBgMRIHnmT2ZAAWrSccFrYIsStwJy3vfHpjh3ICwi0UmZaTqVvgnnu6zZE.jpg'},
            'type': 'venuePage',
            'venue': {'id': '55784a26498e43f834a72d8a'}},
           'visibility': 'public'},
          'followers': {'count': 99},
          'listItems': {'count': 28,
           'items': [{'id': 'v585164b77220e62219c9aeb6',
             'createdAt': 1564265712}]}}]}]},
     'hours': {'status': 'Closed until 6:00 PM',
      'richStatus': {'entities': [], 'text': 'Closed until 6:00 PM'},
      'isOpen': False,
      'isLocalHoliday': True,
      'localHolidayName': 'Independence Day',
      'dayData': [],
      'timeframes': [{'days': 'Mon–Sun',
        'includesToday': True,
        'open': [{'renderedTime': '6:00 PM–Midnight'}],
        'segments': []}]},
     'popular': {'isOpen': False,
      'isLocalHoliday': True,
      'localHolidayName': 'Independence Day',
      'timeframes': [{'days': 'Today',
        'includesToday': True,
        'open': [{'renderedTime': '5:00 PM–Midnight'}],
        'segments': []},
       {'days': 'Sun',
        'open': [{'renderedTime': '5:00 PM–Midnight'}],
        'segments': []},
       {'days': 'Mon–Thu',
        'open': [{'renderedTime': '5:00 PM–Midnight'}],
        'segments': []},
       {'days': 'Fri',
        'open': [{'renderedTime': '5:00 PM–1:00 AM'}],
        'segments': []}]},
     'seasonalHours': [],
     'defaultHours': {'status': 'Closed until 6:00 PM',
      'richStatus': {'entities': [], 'text': 'Closed until 6:00 PM'},
      'isOpen': False,
      'isLocalHoliday': True,
      'localHolidayName': 'Independence Day',
      'dayData': [],
      'timeframes': [{'days': 'Mon–Sun',
        'includesToday': True,
        'open': [{'renderedTime': '6:00 PM–Midnight'}],
        'segments': []}]},
     'pageUpdates': {'count': 0, 'items': []},
     'inbox': {'count': 0, 'items': []},
     'attributes': {'groups': [{'type': 'reservations',
        'name': 'Reservations',
        'summary': 'Reservations',
        'count': 3,
        'items': [{'displayName': 'Reservations', 'displayValue': 'Yes'}]},
       {'type': 'payments',
        'name': 'Credit Cards',
        'summary': 'Credit Cards',
        'count': 7,
        'items': [{'displayName': 'Credit Cards', 'displayValue': 'Yes'}]},
       {'type': 'outdoorSeating',
        'name': 'Outdoor Seating',
        'count': 1,
        'items': [{'displayName': 'Outdoor Seating', 'displayValue': 'No'}]},
       {'type': 'serves',
        'name': 'Menus',
        'summary': 'Dinner',
        'count': 8,
        'items': [{'displayName': 'Dinner', 'displayValue': 'Dinner'}]}]},
     'bestPhoto': {'id': '5e4ea442bb3fc70008d67b1c',
      'createdAt': 1582212162,
      'source': {'name': 'Swarm for Android', 'url': 'https://www.swarmapp.com'},
      'prefix': 'https://fastly.4sqi.net/img/general/',
      'suffix': '/797590_WoGLpybFi42d4PgxKm8i1A8Ces7oKtLJS7C6ZnFaLlo.jpg',
      'width': 1440,
      'height': 1080,
      'visibility': 'public'},
     'colors': {'highlightColor': {'photoId': '5e4ea442bb3fc70008d67b1c',
       'value': -9420736},
      'highlightTextColor': {'photoId': '5e4ea442bb3fc70008d67b1c', 'value': -1},
      'algoVersion': 3}}




```python
#testing tips API
url_tips='https://api.foursquare.com/v2/venues/{}/tips?&sort=popular&client_id={}&client_secret={}&v={}'.format('4fd38a04e4b065401a9aaf88',CLIENT_ID, CLIENT_SECRET,VERSION)
print(url_tips)
tips_detail=requests.get(url_tips).json()
tips_detail['response']['tips']['items'][0]['agreeCount']
```

#2. we use first for loop to filter the most liked tip
#3. we use second for loop to combine all popular timeframe into one,cos timeframes can be more than one
#4. Due to venues details are not the same, for example, some have tips some don't, so we use try/except to catach some details in case errors occur

df=df_init
df['Category']=''
df['Price_Tier']=''
df['Likes_Count']=''
df['Rating']=''
df['Rating_Signals']=''
df['Tips']=''
df['Agree_Count']=''
df['Polular_Timeframe_Today']=''
df['Latitude']=''
df['Longitude']=''

for index,row in df_init.iterrows():
    id_venue=row['ID']
    url_venue='https://api.foursquare.com/v2/venues/{}?&client_id={}&client_secret={}&v={}'.format(id_venue,CLIENT_ID, CLIENT_SECRET,VERSION)
    url_tips='https://api.foursquare.com/v2/venues/{}/tips?&sort=popular&client_id={}&client_secret={}&v={}'.format(id_venue,CLIENT_ID, CLIENT_SECRET,VERSION)
    venue_detail=requests.get(url_venue).json()
    tips_detail=requests.get(url_tips).json()
    #deal with categories function
    Category=if_cnr(venue_detail)
    #deal with other parameters
    try:
        Price_Tier=venue_detail['response']['venue']['price']['tier']
    except:
        Price_Tier='N/A'
    try:
        Likes_Count=venue_detail['response']['venue']['likes']['count']
    except:
        Likes_Count='N/A'
    try:
        Rating=venue_detail['response']['venue']['rating']
    except:
        Rating='N/A'
    try:
        Rating_Signals=venue_detail['response']['venue']['ratingSignals']
    except:
        Rating_Signals='N/A'
    #use API parameter 'sort=popular' to retrive most liked tips
    Tips=''
    Agree_Count=0
    try:
        Tips=tips_detail['response']['tips']['items'][0]['text']
        Agree_Count=tips_detail['response']['tips']['items'][0]['agreeCount']
    except:
        Agree_Count='N/A'
        Tips=='N/A'

    #deal with today's popular timeframes,combine all timeframe into one
    Polular_Timeframe_Today=''
    try:
        for y in venue_detail['response']['venue']['popular']['timeframes'][0]['open']:
            Polular_Timeframe_Today+=y['renderedTime']
    except:
        Polular_Timeframe_Today='N/A'
    
    try:
        Latitude=venue_detail['response']['venue']['location']['lat']
        Longitude=venue_detail['response']['venue']['location']['lng']
    except:
        Latitude='N/A'
        Longitude='N/A'
    #all retrived data into columns
    row['Category']=Category
    row['Price_Tier']=Price_Tier
    row['Likes_Count']=Likes_Count
    row['Rating']=Rating
    row['Rating_Signals']=Rating_Signals
    row['Tips']=Tips
    row['Agree_Count']=Agree_Count
    row['Polular_Timeframe_Today']=Polular_Timeframe_Today
    row['Latitude']=Latitude
    row['Longitude']=Longitude



```python
# show dataframe
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NAME</th>
      <th>ID</th>
      <th>ADDRESS</th>
      <th>Category</th>
      <th>Price_Tier</th>
      <th>Likes_Count</th>
      <th>Rating</th>
      <th>Rating_Signals</th>
      <th>Tips</th>
      <th>Agree_Count</th>
      <th>Polular_Timeframe_Today</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cheeky Sandwiches</td>
      <td>4b1896caf964a52069d423e3</td>
      <td>35 Orchard St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>545</td>
      <td>9.2</td>
      <td>739</td>
      <td>The chicken sandwich is a must try. The beigne...</td>
      <td>5</td>
      <td>10:00 AM–10:00 PM</td>
      <td>40.7158</td>
      <td>-73.9918</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kiki's</td>
      <td>5521c2ff498ebe2368634187</td>
      <td>130 Division St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>830</td>
      <td>9.1</td>
      <td>1066</td>
      <td>Unbelievable. Hands down the best Greek food o...</td>
      <td>18</td>
      <td>Noon–Midnight</td>
      <td>40.7145</td>
      <td>-73.992</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Scarr's Pizza</td>
      <td>56c3c626cd106998d2b196d0</td>
      <td>22 Orchard St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>229</td>
      <td>9.1</td>
      <td>294</td>
      <td>This place has an old school diner vibe with d...</td>
      <td>12</td>
      <td>Noon–Midnight</td>
      <td>40.7153</td>
      <td>-73.9916</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Wayla</td>
      <td>5cc4e9d0c876c8002c3010cb</td>
      <td>100 Forsyth St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>127</td>
      <td>9.3</td>
      <td>147</td>
      <td>Get the branzino if you like flavors like tama...</td>
      <td>8</td>
      <td>11:00 AM–3:00 PM5:00 PM–11:00 PM</td>
      <td>40.7183</td>
      <td>-73.9926</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Forgtmenot</td>
      <td>4fd38a04e4b065401a9aaf88</td>
      <td>138 Division St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>517</td>
      <td>9</td>
      <td>646</td>
      <td>After careful review of the LES, this might be...</td>
      <td>6</td>
      <td>Noon–1:00 AM</td>
      <td>40.7145</td>
      <td>-73.9915</td>
    </tr>
  </tbody>
</table>
</div>




```python
# take out rating=N/A items
df1=df[df['Rating']!='N/A']
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NAME</th>
      <th>ID</th>
      <th>ADDRESS</th>
      <th>Category</th>
      <th>Price_Tier</th>
      <th>Likes_Count</th>
      <th>Rating</th>
      <th>Rating_Signals</th>
      <th>Tips</th>
      <th>Agree_Count</th>
      <th>Polular_Timeframe_Today</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cheeky Sandwiches</td>
      <td>4b1896caf964a52069d423e3</td>
      <td>35 Orchard St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>545</td>
      <td>9.2</td>
      <td>739</td>
      <td>The chicken sandwich is a must try. The beigne...</td>
      <td>5</td>
      <td>10:00 AM–10:00 PM</td>
      <td>40.7158</td>
      <td>-73.9918</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kiki's</td>
      <td>5521c2ff498ebe2368634187</td>
      <td>130 Division St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>830</td>
      <td>9.1</td>
      <td>1066</td>
      <td>Unbelievable. Hands down the best Greek food o...</td>
      <td>18</td>
      <td>Noon–Midnight</td>
      <td>40.7145</td>
      <td>-73.992</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Scarr's Pizza</td>
      <td>56c3c626cd106998d2b196d0</td>
      <td>22 Orchard St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>229</td>
      <td>9.1</td>
      <td>294</td>
      <td>This place has an old school diner vibe with d...</td>
      <td>12</td>
      <td>Noon–Midnight</td>
      <td>40.7153</td>
      <td>-73.9916</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Wayla</td>
      <td>5cc4e9d0c876c8002c3010cb</td>
      <td>100 Forsyth St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>127</td>
      <td>9.3</td>
      <td>147</td>
      <td>Get the branzino if you like flavors like tama...</td>
      <td>8</td>
      <td>11:00 AM–3:00 PM5:00 PM–11:00 PM</td>
      <td>40.7183</td>
      <td>-73.9926</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Forgtmenot</td>
      <td>4fd38a04e4b065401a9aaf88</td>
      <td>138 Division St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>517</td>
      <td>9</td>
      <td>646</td>
      <td>After careful review of the LES, this might be...</td>
      <td>6</td>
      <td>Noon–1:00 AM</td>
      <td>40.7145</td>
      <td>-73.9915</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Jeffrey's Grocery</td>
      <td>4ca21faa8afca09388192116</td>
      <td>172 Waverly Pl</td>
      <td>Non-Chinese Restaurant</td>
      <td>3</td>
      <td>685</td>
      <td>9.2</td>
      <td>907</td>
      <td>I love here!!! Their Bloody May is the best in...</td>
      <td>5</td>
      <td>10:00 AM–1:00 AM</td>
      <td>40.7339</td>
      <td>-74.0013</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Buvette</td>
      <td>4d0bf7e3f29c236ac675bfe7</td>
      <td>42 Grove St</td>
      <td>Non-Chinese Restaurant</td>
      <td>3</td>
      <td>1849</td>
      <td>9.1</td>
      <td>2373</td>
      <td>Amazing place and delicious food, just a bit p...</td>
      <td>16</td>
      <td>9:00 AM–11:00 PM</td>
      <td>40.7328</td>
      <td>-74.0043</td>
    </tr>
    <tr>
      <th>97</th>
      <td>L’Accolade</td>
      <td>5d181bac17d3b9002329f126</td>
      <td>302 Bleecker St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>23</td>
      <td>9</td>
      <td>45</td>
      <td>Potatoes are sooo good. Plus $10 rotating wine...</td>
      <td>1</td>
      <td>4:00 PM–Midnight</td>
      <td>40.7325</td>
      <td>-74.0038</td>
    </tr>
    <tr>
      <th>98</th>
      <td>CAVA</td>
      <td>57bcd600498e81d153625a1a</td>
      <td>143 4th Ave</td>
      <td>Non-Chinese Restaurant</td>
      <td>1</td>
      <td>330</td>
      <td>9</td>
      <td>416</td>
      <td>The salad bowls are a superior tasting, health...</td>
      <td>13</td>
      <td>Noon–4:00 PM7:00 PM–8:00 PM</td>
      <td>40.7338</td>
      <td>-73.9896</td>
    </tr>
    <tr>
      <th>99</th>
      <td>4 Charles Prime Rib</td>
      <td>585164b77220e62219c9aeb6</td>
      <td>4 Charles St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>217</td>
      <td>9.3</td>
      <td>270</td>
      <td>Get the ribeye and Tempranillo. Split the burg...</td>
      <td>8</td>
      <td>5:00 PM–Midnight</td>
      <td>40.7352</td>
      <td>-74.0006</td>
    </tr>
  </tbody>
</table>
<p>99 rows × 13 columns</p>
</div>




```python
#sort by rating for next analysis
df2=df1.sort_values(by='Rating', ascending=False)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NAME</th>
      <th>ID</th>
      <th>ADDRESS</th>
      <th>Category</th>
      <th>Price_Tier</th>
      <th>Likes_Count</th>
      <th>Rating</th>
      <th>Rating_Signals</th>
      <th>Tips</th>
      <th>Agree_Count</th>
      <th>Polular_Timeframe_Today</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70</th>
      <td>Brooklyn Bagel &amp; Coffee Company</td>
      <td>5b8e66ac234724002c927c4b</td>
      <td>63 E 8th St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>78</td>
      <td>9.4</td>
      <td>91</td>
      <td>Freshly made, great choice and delicious! So g...</td>
      <td>4</td>
      <td>7:00 AM–3:00 PM</td>
      <td>40.7309</td>
      <td>-73.9933</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Faicco's Italian Specialties</td>
      <td>4a74a36af964a520fede1fe3</td>
      <td>260 Bleecker St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>332</td>
      <td>9.4</td>
      <td>445</td>
      <td>Order the Italian special ($12) features: pros...</td>
      <td>8</td>
      <td>10:00 AM–6:00 PM</td>
      <td>40.7311</td>
      <td>-74.003</td>
    </tr>
    <tr>
      <th>99</th>
      <td>4 Charles Prime Rib</td>
      <td>585164b77220e62219c9aeb6</td>
      <td>4 Charles St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>217</td>
      <td>9.3</td>
      <td>270</td>
      <td>Get the ribeye and Tempranillo. Split the burg...</td>
      <td>8</td>
      <td>5:00 PM–Midnight</td>
      <td>40.7352</td>
      <td>-74.0006</td>
    </tr>
    <tr>
      <th>38</th>
      <td>SUGARFISH by sushi nozawa</td>
      <td>5c6c6715f709c1002cd49290</td>
      <td>202 Spring St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>83</td>
      <td>9.3</td>
      <td>94</td>
      <td>Opens 2/21!</td>
      <td>3</td>
      <td>Noon–11:00 PM</td>
      <td>40.7253</td>
      <td>-74.0035</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Sunny &amp; Annie Gourmet Deli</td>
      <td>4b41102bf964a52055c025e3</td>
      <td>94 Avenue B</td>
      <td>Non-Chinese Restaurant</td>
      <td>1</td>
      <td>429</td>
      <td>9.3</td>
      <td>571</td>
      <td>Life altering sandwiches. I had the 2014 with ...</td>
      <td>4</td>
      <td>N/A</td>
      <td>40.7246</td>
      <td>-73.9816</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saigon Vietnamese Sandwich Deli</td>
      <td>49e9549df964a520f2651fe3</td>
      <td>369 Broome St</td>
      <td>Non-Chinese Restaurant</td>
      <td>1</td>
      <td>440</td>
      <td>8.9</td>
      <td>631</td>
      <td>The best banh mi sandwich in NYC! If you are a...</td>
      <td>3</td>
      <td>11:00 AM–6:00 PM</td>
      <td>40.7201</td>
      <td>-73.9957</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Banter</td>
      <td>589c7ca37b43b441e3ac3ef8</td>
      <td>169 Sullivan St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>274</td>
      <td>8.9</td>
      <td>351</td>
      <td>Adorable new Australian café on Sullivan St! P...</td>
      <td>10</td>
      <td>9:00 AM–5:00 PM7:00 PM–9:00 PM</td>
      <td>40.728</td>
      <td>-74.0012</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Loring Place</td>
      <td>58324f3f9dc8d00516f64b6d</td>
      <td>21 W 8th St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>404</td>
      <td>8.9</td>
      <td>503</td>
      <td>Everything is fantastic! Exactly what you'd ex...</td>
      <td>14</td>
      <td>11:00 AM–3:00 PM5:00 PM–11:00 PM</td>
      <td>40.7329</td>
      <td>-73.9976</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Sweet Chick</td>
      <td>537b5a29498ec121cf9fa1f4</td>
      <td>178 Ludlow St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>678</td>
      <td>8.9</td>
      <td>893</td>
      <td>Want something sweet for brunch? Get the Chick...</td>
      <td>12</td>
      <td>10:00 AM–11:00 PM</td>
      <td>40.7218</td>
      <td>-73.9875</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Ise Restaurant</td>
      <td>56f5d9d7498e00fbd06e7421</td>
      <td>63 Cooper Sq</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>143</td>
      <td>8.9</td>
      <td>189</td>
      <td>absolutely loved. soft shell crab, nameko soba...</td>
      <td>3</td>
      <td>Noon–3:00 PM6:00 PM–11:00 PM</td>
      <td>40.7291</td>
      <td>-73.99</td>
    </tr>
  </tbody>
</table>
<p>99 rows × 13 columns</p>
</div>




```python
#we only trace top 20 rating places
df3=df2[0:21]
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NAME</th>
      <th>ID</th>
      <th>ADDRESS</th>
      <th>Category</th>
      <th>Price_Tier</th>
      <th>Likes_Count</th>
      <th>Rating</th>
      <th>Rating_Signals</th>
      <th>Tips</th>
      <th>Agree_Count</th>
      <th>Polular_Timeframe_Today</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70</th>
      <td>Brooklyn Bagel &amp; Coffee Company</td>
      <td>5b8e66ac234724002c927c4b</td>
      <td>63 E 8th St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>78</td>
      <td>9.4</td>
      <td>91</td>
      <td>Freshly made, great choice and delicious! So g...</td>
      <td>4</td>
      <td>7:00 AM–3:00 PM</td>
      <td>40.7309</td>
      <td>-73.9933</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Faicco's Italian Specialties</td>
      <td>4a74a36af964a520fede1fe3</td>
      <td>260 Bleecker St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>332</td>
      <td>9.4</td>
      <td>445</td>
      <td>Order the Italian special ($12) features: pros...</td>
      <td>8</td>
      <td>10:00 AM–6:00 PM</td>
      <td>40.7311</td>
      <td>-74.003</td>
    </tr>
    <tr>
      <th>99</th>
      <td>4 Charles Prime Rib</td>
      <td>585164b77220e62219c9aeb6</td>
      <td>4 Charles St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>217</td>
      <td>9.3</td>
      <td>270</td>
      <td>Get the ribeye and Tempranillo. Split the burg...</td>
      <td>8</td>
      <td>5:00 PM–Midnight</td>
      <td>40.7352</td>
      <td>-74.0006</td>
    </tr>
    <tr>
      <th>38</th>
      <td>SUGARFISH by sushi nozawa</td>
      <td>5c6c6715f709c1002cd49290</td>
      <td>202 Spring St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>83</td>
      <td>9.3</td>
      <td>94</td>
      <td>Opens 2/21!</td>
      <td>3</td>
      <td>Noon–11:00 PM</td>
      <td>40.7253</td>
      <td>-74.0035</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Sunny &amp; Annie Gourmet Deli</td>
      <td>4b41102bf964a52055c025e3</td>
      <td>94 Avenue B</td>
      <td>Non-Chinese Restaurant</td>
      <td>1</td>
      <td>429</td>
      <td>9.3</td>
      <td>571</td>
      <td>Life altering sandwiches. I had the 2014 with ...</td>
      <td>4</td>
      <td>N/A</td>
      <td>40.7246</td>
      <td>-73.9816</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Crown Shy</td>
      <td>5c883f65f4b525002c0bf2ca</td>
      <td>70 Pine St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>154</td>
      <td>9.3</td>
      <td>187</td>
      <td>You have to drink the Sinclaire and my favorit...</td>
      <td>10</td>
      <td>Noon–1:00 PM5:00 PM–11:00 PM</td>
      <td>40.7062</td>
      <td>-74.0075</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Le Coucou</td>
      <td>57583641498e90001a32e13e</td>
      <td>138 Lafayette St</td>
      <td>Non-Chinese Restaurant</td>
      <td>3</td>
      <td>394</td>
      <td>9.3</td>
      <td>498</td>
      <td>At Le Coucou, the menu includes seaweed butter...</td>
      <td>4</td>
      <td>10:00 AM–3:00 PM5:00 PM–11:00 PM</td>
      <td>40.7191</td>
      <td>-74.0002</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Los Tacos No. 1</td>
      <td>5d5f24ec09484500079aee00</td>
      <td>136 Church St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>78</td>
      <td>9.3</td>
      <td>95</td>
      <td>The new taco joint in town (or in TriBeCa area...</td>
      <td>9</td>
      <td>11:00 AM–9:00 PM</td>
      <td>40.7143</td>
      <td>-74.0088</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Wayla</td>
      <td>5cc4e9d0c876c8002c3010cb</td>
      <td>100 Forsyth St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>127</td>
      <td>9.3</td>
      <td>147</td>
      <td>Get the branzino if you like flavors like tama...</td>
      <td>8</td>
      <td>11:00 AM–3:00 PM5:00 PM–11:00 PM</td>
      <td>40.7183</td>
      <td>-73.9926</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Shake Shack</td>
      <td>59d36de20fe7a024363de0b8</td>
      <td>20 3rd Ave</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>163</td>
      <td>9.2</td>
      <td>191</td>
      <td>The best Shake Shack in the city. All orders a...</td>
      <td>21</td>
      <td>Noon–Midnight</td>
      <td>40.73</td>
      <td>-73.9897</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Hudson Eats</td>
      <td>5362a2ae498e3b18c22334be</td>
      <td>225 Liberty St</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>903</td>
      <td>9.2</td>
      <td>1089</td>
      <td>A completely insane food oasis in Battery Park...</td>
      <td>10</td>
      <td>11:00 AM–9:00 PM</td>
      <td>40.7127</td>
      <td>-74.0159</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Chobani</td>
      <td>50002274e4b0deb8db4eea3b</td>
      <td>152 Prince St</td>
      <td>Non-Chinese Restaurant</td>
      <td>1</td>
      <td>1029</td>
      <td>9.2</td>
      <td>1289</td>
      <td>This place is fantastic. Great spot to grab a ...</td>
      <td>7</td>
      <td>10:00 AM–8:00 PM</td>
      <td>40.7258</td>
      <td>-74.001</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Jeffrey's Grocery</td>
      <td>4ca21faa8afca09388192116</td>
      <td>172 Waverly Pl</td>
      <td>Non-Chinese Restaurant</td>
      <td>3</td>
      <td>685</td>
      <td>9.2</td>
      <td>907</td>
      <td>I love here!!! Their Bloody May is the best in...</td>
      <td>5</td>
      <td>10:00 AM–1:00 AM</td>
      <td>40.7339</td>
      <td>-74.0013</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Upstate Craft Beer and Oyster Bar</td>
      <td>4e41f0822271a90466a0e967</td>
      <td>95 1st Ave</td>
      <td>Non-Chinese Restaurant</td>
      <td>3</td>
      <td>627</td>
      <td>9.2</td>
      <td>835</td>
      <td></td>
      <td>N/A</td>
      <td>5:00 PM–11:00 PM</td>
      <td>40.7263</td>
      <td>-73.9865</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Butler Bakeshop</td>
      <td>5b7c4cb3c58ed7002c1fd9bd</td>
      <td>40 Water St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>78</td>
      <td>9.2</td>
      <td>104</td>
      <td>The egg sandwich with avocado and Ryan’s signa...</td>
      <td>6</td>
      <td>8:00 AM–6:00 PM</td>
      <td>40.7033</td>
      <td>-73.9925</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Blue Ribbon Sushi</td>
      <td>45ac12d6f964a5205d411fe3</td>
      <td>119 Sullivan St</td>
      <td>Non-Chinese Restaurant</td>
      <td>3</td>
      <td>816</td>
      <td>9.2</td>
      <td>1087</td>
      <td>Wow. The sushi is good value, the service is a...</td>
      <td>6</td>
      <td>2:00 PM–Midnight</td>
      <td>40.7262</td>
      <td>-74.0026</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Joseph Leonard</td>
      <td>4a78c865f964a52068e61fe3</td>
      <td>170 Waverly Pl</td>
      <td>Non-Chinese Restaurant</td>
      <td>3</td>
      <td>1157</td>
      <td>9.2</td>
      <td>1501</td>
      <td>This is the best brunch in the city. Breakfast...</td>
      <td>15</td>
      <td>10:00 AM–4:00 PM6:00 PM–1:00 AM</td>
      <td>40.7337</td>
      <td>-74.0018</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Raku</td>
      <td>5aea422a033693002bf0c1cb</td>
      <td>48 Macdougal St</td>
      <td>Non-Chinese Restaurant</td>
      <td>N/A</td>
      <td>166</td>
      <td>9.2</td>
      <td>190</td>
      <td>Get the Niku. No one knows about this place ye...</td>
      <td>7</td>
      <td>Noon–10:00 PM</td>
      <td>40.7274</td>
      <td>-74.0027</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Cafe Mogador</td>
      <td>41044980f964a520750b1fe3</td>
      <td>101 Saint Marks Pl</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>1399</td>
      <td>9.2</td>
      <td>1823</td>
      <td>The food is delicious. I especially liked the ...</td>
      <td>11</td>
      <td>10:00 AM–4:00 PM6:00 PM–11:00 PM</td>
      <td>40.7273</td>
      <td>-73.9845</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Kura</td>
      <td>510c85e7e4b0056826b88297</td>
      <td>130 Saint Marks Pl</td>
      <td>Non-Chinese Restaurant</td>
      <td>4</td>
      <td>212</td>
      <td>9.2</td>
      <td>263</td>
      <td>Amazing. Did the 20 piece omakase for 150, it ...</td>
      <td>2</td>
      <td>5:00 PM–11:00 PM</td>
      <td>40.7268</td>
      <td>-73.9834</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Bobwhite Counter</td>
      <td>4f00dea9f9abd5b3917d422c</td>
      <td>94 Avenue C</td>
      <td>Non-Chinese Restaurant</td>
      <td>2</td>
      <td>778</td>
      <td>9.2</td>
      <td>1053</td>
      <td>The buffalo chicken sandwich should run for pr...</td>
      <td>10</td>
      <td>Noon–11:00 PM</td>
      <td>40.7237</td>
      <td>-73.9791</td>
    </tr>
  </tbody>
</table>
</div>




```python
#install and import folium function
#! conda install -c conda-forge folium
import folium 
import webbrowser
from folium.plugins import MarkerCluster
```


```python
# create map of New York using latitude and longitude values
# https://python-visualization.github.io/folium/quickstart.html
map_chinatown = folium.Map(location=[latitude, longitude], zoom_start=14)
map_chinatown
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvZ2gvcHl0aG9uLXZpc3VhbGl6YXRpb24vZm9saXVtL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5taW4uY3NzIi8+CiAgICA8c3R5bGU+aHRtbCwgYm9keSB7d2lkdGg6IDEwMCU7aGVpZ2h0OiAxMDAlO21hcmdpbjogMDtwYWRkaW5nOiAwO308L3N0eWxlPgogICAgPHN0eWxlPiNtYXAge3Bvc2l0aW9uOmFic29sdXRlO3RvcDowO2JvdHRvbTowO3JpZ2h0OjA7bGVmdDowO308L3N0eWxlPgogICAgCiAgICAgICAgICAgIDxtZXRhIG5hbWU9InZpZXdwb3J0IiBjb250ZW50PSJ3aWR0aD1kZXZpY2Utd2lkdGgsCiAgICAgICAgICAgICAgICBpbml0aWFsLXNjYWxlPTEuMCwgbWF4aW11bS1zY2FsZT0xLjAsIHVzZXItc2NhbGFibGU9bm8iIC8+CiAgICAgICAgICAgIDxzdHlsZT4KICAgICAgICAgICAgICAgICNtYXBfZDczM2U4MmNjMWU4NGE4Yzg2ZDMxMWUyNmZhZTk5YzAgewogICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgICAgICB3aWR0aDogMTAwLjAlOwogICAgICAgICAgICAgICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgICAgICAgICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCA9IEwubWFwKAogICAgICAgICAgICAgICAgIm1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCIsCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgY2VudGVyOiBbNDAuNzE1NjE4NDIyMzE0MzIsIC03My45OTQyNzkzNjI1NTk3OF0sCiAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NywKICAgICAgICAgICAgICAgICAgICB6b29tOiAxNCwKICAgICAgICAgICAgICAgICAgICB6b29tQ29udHJvbDogdHJ1ZSwKICAgICAgICAgICAgICAgICAgICBwcmVmZXJDYW52YXM6IGZhbHNlLAogICAgICAgICAgICAgICAgfQogICAgICAgICAgICApOwoKICAgICAgICAgICAgCgogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzMxYWRlY2IxZmQyMzQwMWU4MThiN2ZmZjVhMzIwZTcwID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAiaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmciLAogICAgICAgICAgICAgICAgeyJhdHRyaWJ1dGlvbiI6ICJEYXRhIGJ5IFx1MDAyNmNvcHk7IFx1MDAzY2EgaHJlZj1cImh0dHA6Ly9vcGVuc3RyZWV0bWFwLm9yZ1wiXHUwMDNlT3BlblN0cmVldE1hcFx1MDAzYy9hXHUwMDNlLCB1bmRlciBcdTAwM2NhIGhyZWY9XCJodHRwOi8vd3d3Lm9wZW5zdHJlZXRtYXAub3JnL2NvcHlyaWdodFwiXHUwMDNlT0RiTFx1MDAzYy9hXHUwMDNlLiIsICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwgIm1heE5hdGl2ZVpvb20iOiAxOCwgIm1heFpvb20iOiAxOCwgIm1pblpvb20iOiAwLCAibm9XcmFwIjogZmFsc2UsICJvcGFjaXR5IjogMSwgInN1YmRvbWFpbnMiOiAiYWJjIiwgInRtcyI6IGZhbHNlfQogICAgICAgICAgICApLmFkZFRvKG1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCk7CiAgICAgICAgCjwvc2NyaXB0Pg== onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
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

```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvZ2gvcHl0aG9uLXZpc3VhbGl6YXRpb24vZm9saXVtL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5taW4uY3NzIi8+CiAgICA8c3R5bGU+aHRtbCwgYm9keSB7d2lkdGg6IDEwMCU7aGVpZ2h0OiAxMDAlO21hcmdpbjogMDtwYWRkaW5nOiAwO308L3N0eWxlPgogICAgPHN0eWxlPiNtYXAge3Bvc2l0aW9uOmFic29sdXRlO3RvcDowO2JvdHRvbTowO3JpZ2h0OjA7bGVmdDowO308L3N0eWxlPgogICAgCiAgICAgICAgICAgIDxtZXRhIG5hbWU9InZpZXdwb3J0IiBjb250ZW50PSJ3aWR0aD1kZXZpY2Utd2lkdGgsCiAgICAgICAgICAgICAgICBpbml0aWFsLXNjYWxlPTEuMCwgbWF4aW11bS1zY2FsZT0xLjAsIHVzZXItc2NhbGFibGU9bm8iIC8+CiAgICAgICAgICAgIDxzdHlsZT4KICAgICAgICAgICAgICAgICNtYXBfZDczM2U4MmNjMWU4NGE4Yzg2ZDMxMWUyNmZhZTk5YzAgewogICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgICAgICB3aWR0aDogMTAwLjAlOwogICAgICAgICAgICAgICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgICAgICAgICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCA9IEwubWFwKAogICAgICAgICAgICAgICAgIm1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCIsCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgY2VudGVyOiBbNDAuNzE1NjE4NDIyMzE0MzIsIC03My45OTQyNzkzNjI1NTk3OF0sCiAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NywKICAgICAgICAgICAgICAgICAgICB6b29tOiAxNCwKICAgICAgICAgICAgICAgICAgICB6b29tQ29udHJvbDogdHJ1ZSwKICAgICAgICAgICAgICAgICAgICBwcmVmZXJDYW52YXM6IGZhbHNlLAogICAgICAgICAgICAgICAgfQogICAgICAgICAgICApOwoKICAgICAgICAgICAgCgogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzMxYWRlY2IxZmQyMzQwMWU4MThiN2ZmZjVhMzIwZTcwID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAiaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmciLAogICAgICAgICAgICAgICAgeyJhdHRyaWJ1dGlvbiI6ICJEYXRhIGJ5IFx1MDAyNmNvcHk7IFx1MDAzY2EgaHJlZj1cImh0dHA6Ly9vcGVuc3RyZWV0bWFwLm9yZ1wiXHUwMDNlT3BlblN0cmVldE1hcFx1MDAzYy9hXHUwMDNlLCB1bmRlciBcdTAwM2NhIGhyZWY9XCJodHRwOi8vd3d3Lm9wZW5zdHJlZXRtYXAub3JnL2NvcHlyaWdodFwiXHUwMDNlT0RiTFx1MDAzYy9hXHUwMDNlLiIsICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwgIm1heE5hdGl2ZVpvb20iOiAxOCwgIm1heFpvb20iOiAxOCwgIm1pblpvb20iOiAwLCAibm9XcmFwIjogZmFsc2UsICJvcGFjaXR5IjogMSwgInN1YmRvbWFpbnMiOiAiYWJjIiwgInRtcyI6IGZhbHNlfQogICAgICAgICAgICApLmFkZFRvKG1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl8zZWZmNDkxMDQwNTU0ZmM5OWRlMzRjYzM0ZjExMzliOSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczMDkxMjU3NTYxOTEzNiwgLTczLjk5MzI1OTE0MzcxMDVdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDczM2U4MmNjMWU4NGE4Yzg2ZDMxMWUyNmZhZTk5YzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzU2NjUyMTMwZDdkNzQxMGU4NzFlODEzMTBmMTkyOGFiID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJpbmZvLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImJsYWNrIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfM2VmZjQ5MTA0MDU1NGZjOTlkZTM0Y2MzNGYxMTM5Yjkuc2V0SWNvbihpY29uXzU2NjUyMTMwZDdkNzQxMGU4NzFlODEzMTBmMTkyOGFiKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9mOTM1YTNjNzQ4NzA0YTdlYThiMGI1YjE2NzJjMGQ0YiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfM2VmNGYyNzFhNmVlNDNjNzg1YmZkZTUxYzA3ZWI4ZTcgPSAkKGA8ZGl2IGlkPSJodG1sXzNlZjRmMjcxYTZlZTQzYzc4NWJmZGU1MWMwN2ViOGU3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXRpbmc6OS40LCBBZGRyZXNzOjYzIEUgOHRoIFN0LCBQcmljZV9UaWVyOk4vQSwgIEF2b2lkIFRpbWU6NzowMCBBTeKAkzM6MDAgUE08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZjkzNWEzYzc0ODcwNGE3ZWE4YjBiNWIxNjcyYzBkNGIuc2V0Q29udGVudChodG1sXzNlZjRmMjcxYTZlZTQzYzc4NWJmZGU1MWMwN2ViOGU3KTsKICAgICAgICAKCiAgICAgICAgbWFya2VyXzNlZmY0OTEwNDA1NTRmYzk5ZGUzNGNjMzRmMTEzOWI5LmJpbmRQb3B1cChwb3B1cF9mOTM1YTNjNzQ4NzA0YTdlYThiMGI1YjE2NzJjMGQ0YikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyXzNlZmY0OTEwNDA1NTRmYzk5ZGUzNGNjMzRmMTEzOWI5LmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIEJyb29rbHluIEJhZ2VsICYgQ29mZmVlIENvbXBhbnkKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfOTY2OTdhNTdjOWY4NGVjYzg3NjQyYjg4NjUzNTk3MzkgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzExMTY2MTA4NzU5OCwgLTc0LjAwMzA0MjU3ODY5NzJdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDczM2U4MmNjMWU4NGE4Yzg2ZDMxMWUyNmZhZTk5YzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzE5ZTc3NDczM2M1ZTQ5NWQ5MWM2ZDk4ZDY1MDY5OWFiID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJpbmZvLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImJsdWUiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl85NjY5N2E1N2M5Zjg0ZWNjODc2NDJiODg2NTM1OTczOS5zZXRJY29uKGljb25fMTllNzc0NzMzYzVlNDk1ZDkxYzZkOThkNjUwNjk5YWIpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2NiOTNiNmFhNWQ1NjRkMjhiNmY2OWI3YTNiOTU5MjliID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF84MzFkZDZmNjUzY2Y0NDlkYTIwMmUyNDM1NTUxYWIwZSA9ICQoYDxkaXYgaWQ9Imh0bWxfODMxZGQ2ZjY1M2NmNDQ5ZGEyMDJlMjQzNTU1MWFiMGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJhdGluZzo5LjQsIEFkZHJlc3M6MjYwIEJsZWVja2VyIFN0LCBQcmljZV9UaWVyOjIsICBBdm9pZCBUaW1lOjEwOjAwIEFN4oCTNjowMCBQTTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9jYjkzYjZhYTVkNTY0ZDI4YjZmNjliN2EzYjk1OTI5Yi5zZXRDb250ZW50KGh0bWxfODMxZGQ2ZjY1M2NmNDQ5ZGEyMDJlMjQzNTU1MWFiMGUpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfOTY2OTdhNTdjOWY4NGVjYzg3NjQyYjg4NjUzNTk3MzkuYmluZFBvcHVwKHBvcHVwX2NiOTNiNmFhNWQ1NjRkMjhiNmY2OWI3YTNiOTU5MjliKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfOTY2OTdhNTdjOWY4NGVjYzg3NjQyYjg4NjUzNTk3MzkuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgRmFpY2NvJ3MgSXRhbGlhbiBTcGVjaWFsdGllcwogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl8xZTA1NTkxOGJmMmE0ZDBhYjE2NDE0YjZkMWVlMjljOSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczNTIxOTQ5NTkyMzIwNCwgLTc0LjAwMDY0ODgxODg4NzFdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDczM2U4MmNjMWU4NGE4Yzg2ZDMxMWUyNmZhZTk5YzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzZmMGFjNTIzOTFiYzRkNThhNDc0ZWZiY2RjODU5OWY0ID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJpbmZvLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImJsYWNrIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfMWUwNTU5MThiZjJhNGQwYWIxNjQxNGI2ZDFlZTI5Yzkuc2V0SWNvbihpY29uXzZmMGFjNTIzOTFiYzRkNThhNDc0ZWZiY2RjODU5OWY0KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8xNWI2ZDViNDZiY2M0NTQ0YWUzODllNGRiNDQzNDk0YyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZmFlYjhjODMyZWMxNDJhYjhlZjUxMzg3ODg1MDMwNDUgPSAkKGA8ZGl2IGlkPSJodG1sX2ZhZWI4YzgzMmVjMTQyYWI4ZWY1MTM4Nzg4NTAzMDQ1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXRpbmc6OS4zLCBBZGRyZXNzOjQgQ2hhcmxlcyBTdCwgUHJpY2VfVGllcjpOL0EsICBBdm9pZCBUaW1lOjU6MDAgUE3igJNNaWRuaWdodDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8xNWI2ZDViNDZiY2M0NTQ0YWUzODllNGRiNDQzNDk0Yy5zZXRDb250ZW50KGh0bWxfZmFlYjhjODMyZWMxNDJhYjhlZjUxMzg3ODg1MDMwNDUpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfMWUwNTU5MThiZjJhNGQwYWIxNjQxNGI2ZDFlZTI5YzkuYmluZFBvcHVwKHBvcHVwXzE1YjZkNWI0NmJjYzQ1NDRhZTM4OWU0ZGI0NDM0OTRjKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfMWUwNTU5MThiZjJhNGQwYWIxNjQxNGI2ZDFlZTI5YzkuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgNCBDaGFybGVzIFByaW1lIFJpYgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl9lN2ZhMTZiMmM5ZWU0NmY5YTJjYjgxZmJkOTc0NGVkZSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyNTI5OTc5NjA5MTM1NiwgLTc0LjAwMzUwNzMzOTc0Nzk3XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl83MTNmMTFmMzI5ZTA0OTEzYmQ4ZGUzNjU2NWFlMjBjMCA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibGFjayIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2U3ZmExNmIyYzllZTQ2ZjlhMmNiODFmYmQ5NzQ0ZWRlLnNldEljb24oaWNvbl83MTNmMTFmMzI5ZTA0OTEzYmQ4ZGUzNjU2NWFlMjBjMCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZDBlZjdjYzRjYzE4NDQ4ODg0MDU4MzI1MTE1NzFlNzQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2M0ZTM1OTgwODY5YjQ5MWFiODU4YTU2NmI0Zjk1MGFlID0gJChgPGRpdiBpZD0iaHRtbF9jNGUzNTk4MDg2OWI0OTFhYjg1OGE1NjZiNGY5NTBhZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmF0aW5nOjkuMywgQWRkcmVzczoyMDIgU3ByaW5nIFN0LCBQcmljZV9UaWVyOk4vQSwgIEF2b2lkIFRpbWU6Tm9vbuKAkzExOjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2QwZWY3Y2M0Y2MxODQ0ODg4NDA1ODMyNTExNTcxZTc0LnNldENvbnRlbnQoaHRtbF9jNGUzNTk4MDg2OWI0OTFhYjg1OGE1NjZiNGY5NTBhZSk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9lN2ZhMTZiMmM5ZWU0NmY5YTJjYjgxZmJkOTc0NGVkZS5iaW5kUG9wdXAocG9wdXBfZDBlZjdjYzRjYzE4NDQ4ODg0MDU4MzI1MTE1NzFlNzQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9lN2ZhMTZiMmM5ZWU0NmY5YTJjYjgxZmJkOTc0NGVkZS5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBTVUdBUkZJU0ggYnkgc3VzaGkgbm96YXdhCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzcxMzc3NWJlNGMzMDQxNTFhOGI0MDc2MGEyODgyZTg4ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI0NTkwMDIyNDQ3OSwgLTczLjk4MTYwMDI2OTYwODU1XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl9kMjg5MzVkNzY0YjA0Y2E3YjAzNjYyMWI3ZjNiYmE3NiA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibHVlIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfNzEzNzc1YmU0YzMwNDE1MWE4YjQwNzYwYTI4ODJlODguc2V0SWNvbihpY29uX2QyODkzNWQ3NjRiMDRjYTdiMDM2NjIxYjdmM2JiYTc2KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF80N2MxYmZkNmM1OTQ0ODg5YTg2ZjgzZGEwMGU2MTMwZSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMDkxZDk2Njc4NGY3NDJlNThiZmY1MmNjMmQ5YzM5ZGUgPSAkKGA8ZGl2IGlkPSJodG1sXzA5MWQ5NjY3ODRmNzQyZTU4YmZmNTJjYzJkOWMzOWRlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXRpbmc6OS4zLCBBZGRyZXNzOjk0IEF2ZW51ZSBCLCBQcmljZV9UaWVyOjEsICBBdm9pZCBUaW1lOk4vQTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF80N2MxYmZkNmM1OTQ0ODg5YTg2ZjgzZGEwMGU2MTMwZS5zZXRDb250ZW50KGh0bWxfMDkxZDk2Njc4NGY3NDJlNThiZmY1MmNjMmQ5YzM5ZGUpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfNzEzNzc1YmU0YzMwNDE1MWE4YjQwNzYwYTI4ODJlODguYmluZFBvcHVwKHBvcHVwXzQ3YzFiZmQ2YzU5NDQ4ODlhODZmODNkYTAwZTYxMzBlKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfNzEzNzc1YmU0YzMwNDE1MWE4YjQwNzYwYTI4ODJlODguYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgU3VubnkgJiBBbm5pZSBHb3VybWV0IERlbGkKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfNWM3YWE4Yjk1NTdlNGM3NGFhYjE2MWQyYzMwMDBkMzEgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDYxODY5MzA1MzA4NiwgLTc0LjAwNzQ5MDExNjAzNzkxXSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl83ZjYxZWQ5YWU3Yjc0NzQ3YmMxYjM0MmZjYzc0ZTk1NSA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibGFjayIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyXzVjN2FhOGI5NTU3ZTRjNzRhYWIxNjFkMmMzMDAwZDMxLnNldEljb24oaWNvbl83ZjYxZWQ5YWU3Yjc0NzQ3YmMxYjM0MmZjYzc0ZTk1NSk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMzE0MDRmODI2Nzg3NGY4ZmIyY2FiNzdlM2ZmNTlhYmQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzViZWQ1ZTgwOWY0NjQwM2ZiMTE2OWQ4OGNhYmE1MjY1ID0gJChgPGRpdiBpZD0iaHRtbF81YmVkNWU4MDlmNDY0MDNmYjExNjlkODhjYWJhNTI2NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmF0aW5nOjkuMywgQWRkcmVzczo3MCBQaW5lIFN0LCBQcmljZV9UaWVyOk4vQSwgIEF2b2lkIFRpbWU6Tm9vbuKAkzE6MDAgUE01OjAwIFBN4oCTMTE6MDAgUE08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMzE0MDRmODI2Nzg3NGY4ZmIyY2FiNzdlM2ZmNTlhYmQuc2V0Q29udGVudChodG1sXzViZWQ1ZTgwOWY0NjQwM2ZiMTE2OWQ4OGNhYmE1MjY1KTsKICAgICAgICAKCiAgICAgICAgbWFya2VyXzVjN2FhOGI5NTU3ZTRjNzRhYWIxNjFkMmMzMDAwZDMxLmJpbmRQb3B1cChwb3B1cF8zMTQwNGY4MjY3ODc0ZjhmYjJjYWI3N2UzZmY1OWFiZCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyXzVjN2FhOGI5NTU3ZTRjNzRhYWIxNjFkMmMzMDAwZDMxLmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIENyb3duIFNoeQogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl84MzNlZTJlMTA0Nzk0NjQ1YTU2ZTE2NjU1NDg4OTlhYyA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxOTExMzcwMzk4MjEzLCAtNzQuMDAwMjAxNzQzNTUxMjZdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDczM2U4MmNjMWU4NGE4Yzg2ZDMxMWUyNmZhZTk5YzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzkxNmYzOTgwMzM3ZjRlNTViMGNmODAzOTA3MzRiMTczID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJpbmZvLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogInJlZCIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyXzgzM2VlMmUxMDQ3OTQ2NDVhNTZlMTY2NTU0ODg5OWFjLnNldEljb24oaWNvbl85MTZmMzk4MDMzN2Y0ZTU1YjBjZjgwMzkwNzM0YjE3Myk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMjAwNWQwZjhlMzY1NDk4MGE3YTVmMmM3Njc2ODlkN2MgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzkyMjc0ZGM1NzFlYzQ4ZmFhZTdlNWQ1YmQwMGYxNjEwID0gJChgPGRpdiBpZD0iaHRtbF85MjI3NGRjNTcxZWM0OGZhYWU3ZTVkNWJkMDBmMTYxMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmF0aW5nOjkuMywgQWRkcmVzczoxMzggTGFmYXlldHRlIFN0LCBQcmljZV9UaWVyOjMsICBBdm9pZCBUaW1lOjEwOjAwIEFN4oCTMzowMCBQTTU6MDAgUE3igJMxMTowMCBQTTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8yMDA1ZDBmOGUzNjU0OTgwYTdhNWYyYzc2NzY4OWQ3Yy5zZXRDb250ZW50KGh0bWxfOTIyNzRkYzU3MWVjNDhmYWFlN2U1ZDViZDAwZjE2MTApOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfODMzZWUyZTEwNDc5NDY0NWE1NmUxNjY1NTQ4ODk5YWMuYmluZFBvcHVwKHBvcHVwXzIwMDVkMGY4ZTM2NTQ5ODBhN2E1ZjJjNzY3Njg5ZDdjKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfODMzZWUyZTEwNDc5NDY0NWE1NmUxNjY1NTQ4ODk5YWMuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgTGUgQ291Y291CiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzM0M2VmN2Y0MDRiZTRlYjU4ZTNmNGM5MmFiZTM0YTc4ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzE0MjY3LCAtNzQuMDA4NzU2XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl85MjMzZmY1MzhhMjk0YzgzYWZjZmEwMWQ3MTcyNDBmYyA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibGFjayIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyXzM0M2VmN2Y0MDRiZTRlYjU4ZTNmNGM5MmFiZTM0YTc4LnNldEljb24oaWNvbl85MjMzZmY1MzhhMjk0YzgzYWZjZmEwMWQ3MTcyNDBmYyk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNzZkZGQyOGViNjIxNGUzODlmYjI4NDA1YjBiNTRhNjkgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzA2YWJhODAyNThkYzRkY2E4MjBhZTE3YTRmNzBjNGM0ID0gJChgPGRpdiBpZD0iaHRtbF8wNmFiYTgwMjU4ZGM0ZGNhODIwYWUxN2E0ZjcwYzRjNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmF0aW5nOjkuMywgQWRkcmVzczoxMzYgQ2h1cmNoIFN0LCBQcmljZV9UaWVyOk4vQSwgIEF2b2lkIFRpbWU6MTE6MDAgQU3igJM5OjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzc2ZGRkMjhlYjYyMTRlMzg5ZmIyODQwNWIwYjU0YTY5LnNldENvbnRlbnQoaHRtbF8wNmFiYTgwMjU4ZGM0ZGNhODIwYWUxN2E0ZjcwYzRjNCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl8zNDNlZjdmNDA0YmU0ZWI1OGUzZjRjOTJhYmUzNGE3OC5iaW5kUG9wdXAocG9wdXBfNzZkZGQyOGViNjIxNGUzODlmYjI4NDA1YjBiNTRhNjkpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl8zNDNlZjdmNDA0YmU0ZWI1OGUzZjRjOTJhYmUzNGE3OC5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBMb3MgVGFjb3MgTm8uIDEKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfYzNiOTBlYTgzYjJmNGZhOWIzMGE4OTNkMmFmNGQ2ZTMgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTgyOTA4NDM3NTcxLCAtNzMuOTkyNTgzOTc1MTk1ODhdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDczM2U4MmNjMWU4NGE4Yzg2ZDMxMWUyNmZhZTk5YzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzYwYTE2MThmMGJhZjQyZjBhMWJjM2ZlNzc4YWU5YjU4ID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJpbmZvLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImJsYWNrIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfYzNiOTBlYTgzYjJmNGZhOWIzMGE4OTNkMmFmNGQ2ZTMuc2V0SWNvbihpY29uXzYwYTE2MThmMGJhZjQyZjBhMWJjM2ZlNzc4YWU5YjU4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9kZDMxMmM0NDI0N2U0Njc4YTEyY2RhMjg0MzE2MTQzNyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYzZhM2NlZDhjNmM5NGRjYjg2ZjI4MDU0NjRiYmJjMjUgPSAkKGA8ZGl2IGlkPSJodG1sX2M2YTNjZWQ4YzZjOTRkY2I4NmYyODA1NDY0YmJiYzI1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXRpbmc6OS4zLCBBZGRyZXNzOjEwMCBGb3JzeXRoIFN0LCBQcmljZV9UaWVyOk4vQSwgIEF2b2lkIFRpbWU6MTE6MDAgQU3igJMzOjAwIFBNNTowMCBQTeKAkzExOjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2RkMzEyYzQ0MjQ3ZTQ2NzhhMTJjZGEyODQzMTYxNDM3LnNldENvbnRlbnQoaHRtbF9jNmEzY2VkOGM2Yzk0ZGNiODZmMjgwNTQ2NGJiYmMyNSk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9jM2I5MGVhODNiMmY0ZmE5YjMwYTg5M2QyYWY0ZDZlMy5iaW5kUG9wdXAocG9wdXBfZGQzMTJjNDQyNDdlNDY3OGExMmNkYTI4NDMxNjE0MzcpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9jM2I5MGVhODNiMmY0ZmE5YjMwYTg5M2QyYWY0ZDZlMy5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBXYXlsYQogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl9hNzc2N2JkZDlkOTM0ODU1OGQ0MTJjNWU1MDcxMGU0MCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyOTk5ODQ1MzIzMzgyLCAtNzMuOTg5Njk1Njg5Mzg0Ml0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fNDcwNTYzOTU1MDk0NGEwMGJiNjRiY2YyYjcyNDkwZDAgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImluZm8tc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmxhY2siLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl9hNzc2N2JkZDlkOTM0ODU1OGQ0MTJjNWU1MDcxMGU0MC5zZXRJY29uKGljb25fNDcwNTYzOTU1MDk0NGEwMGJiNjRiY2YyYjcyNDkwZDApOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzA4OGI4ZmEzMjFiNDQxY2FhNTIyOTQ5Y2QzNmYzYmUzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF85MjU1NjY5MDgwMzM0ZDIyODlmZDY5NjU4Y2FhYzk0OSA9ICQoYDxkaXYgaWQ9Imh0bWxfOTI1NTY2OTA4MDMzNGQyMjg5ZmQ2OTY1OGNhYWM5NDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJhdGluZzo5LjIsIEFkZHJlc3M6MjAgM3JkIEF2ZSwgUHJpY2VfVGllcjpOL0EsICBBdm9pZCBUaW1lOk5vb27igJNNaWRuaWdodDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8wODhiOGZhMzIxYjQ0MWNhYTUyMjk0OWNkMzZmM2JlMy5zZXRDb250ZW50KGh0bWxfOTI1NTY2OTA4MDMzNGQyMjg5ZmQ2OTY1OGNhYWM5NDkpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfYTc3NjdiZGQ5ZDkzNDg1NThkNDEyYzVlNTA3MTBlNDAuYmluZFBvcHVwKHBvcHVwXzA4OGI4ZmEzMjFiNDQxY2FhNTIyOTQ5Y2QzNmYzYmUzKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfYTc3NjdiZGQ5ZDkzNDg1NThkNDEyYzVlNTA3MTBlNDAuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgU2hha2UgU2hhY2sKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfYTJkYmFhY2E3YjlhNDYwZjgxMTQzZjdkMWZjZDcyZmUgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTI2NjU5NzE0ODE0MzUsIC03NC4wMTU5MDEwODg3MTQ2XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl9jMTA4ZWZlYzUzM2U0MjJhODg2OWU0MDcxMDM0NTc5YiA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibHVlIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfYTJkYmFhY2E3YjlhNDYwZjgxMTQzZjdkMWZjZDcyZmUuc2V0SWNvbihpY29uX2MxMDhlZmVjNTMzZTQyMmE4ODY5ZTQwNzEwMzQ1NzliKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF80NmFjNjY1YzcwYmM0YjY0YTBiMzFmYjg0NmVmMGNhNSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZWI5Y2I5MWQ4YzQ4NGExOTgwYjhmM2NlZWEwMDQxYTAgPSAkKGA8ZGl2IGlkPSJodG1sX2ViOWNiOTFkOGM0ODRhMTk4MGI4ZjNjZWVhMDA0MWEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXRpbmc6OS4yLCBBZGRyZXNzOjIyNSBMaWJlcnR5IFN0LCBQcmljZV9UaWVyOjIsICBBdm9pZCBUaW1lOjExOjAwIEFN4oCTOTowMCBQTTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF80NmFjNjY1YzcwYmM0YjY0YTBiMzFmYjg0NmVmMGNhNS5zZXRDb250ZW50KGh0bWxfZWI5Y2I5MWQ4YzQ4NGExOTgwYjhmM2NlZWEwMDQxYTApOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfYTJkYmFhY2E3YjlhNDYwZjgxMTQzZjdkMWZjZDcyZmUuYmluZFBvcHVwKHBvcHVwXzQ2YWM2NjVjNzBiYzRiNjRhMGIzMWZiODQ2ZWYwY2E1KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfYTJkYmFhY2E3YjlhNDYwZjgxMTQzZjdkMWZjZDcyZmUuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgSHVkc29uIEVhdHMKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfNTc4OGE2ODIwYTliNDE2YmJjNDg0NGUwZTYwNjYwODUgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjU4MTg2NzI5MjM1NSwgLTc0LjAwMDk4NDk1MDI0NTM1XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl84ODI1MTg3YjM0NDY0YjY4YWNiODM0OTUwNTZlMDU5MyA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibHVlIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfNTc4OGE2ODIwYTliNDE2YmJjNDg0NGUwZTYwNjYwODUuc2V0SWNvbihpY29uXzg4MjUxODdiMzQ0NjRiNjhhY2I4MzQ5NTA1NmUwNTkzKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8wN2Q2NWRjYTkwOGM0NWFmYTJjYWYxZjg1NThlOTQ2OCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZWExOThlZTcwNmNmNDU1MDg5MGFjNjQyN2FjZmEwZmQgPSAkKGA8ZGl2IGlkPSJodG1sX2VhMTk4ZWU3MDZjZjQ1NTA4OTBhYzY0MjdhY2ZhMGZkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXRpbmc6OS4yLCBBZGRyZXNzOjE1MiBQcmluY2UgU3QsIFByaWNlX1RpZXI6MSwgIEF2b2lkIFRpbWU6MTA6MDAgQU3igJM4OjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzA3ZDY1ZGNhOTA4YzQ1YWZhMmNhZjFmODU1OGU5NDY4LnNldENvbnRlbnQoaHRtbF9lYTE5OGVlNzA2Y2Y0NTUwODkwYWM2NDI3YWNmYTBmZCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl81Nzg4YTY4MjBhOWI0MTZiYmM0ODQ0ZTBlNjA2NjA4NS5iaW5kUG9wdXAocG9wdXBfMDdkNjVkY2E5MDhjNDVhZmEyY2FmMWY4NTU4ZTk0NjgpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl81Nzg4YTY4MjBhOWI0MTZiYmM0ODQ0ZTBlNjA2NjA4NS5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBDaG9iYW5pCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyX2M2MzRhOTUyZTA5ODQxOGViZmE5MTQxMzFmNmZlMTU5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzMzOTE5LCAtNzQuMDAxMzQ2XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl9iYzcwMTc0OTQ5Y2I0NDUxOWI2NzI3YjEwY2M3NGQ4YyA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJyZWQiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl9jNjM0YTk1MmUwOTg0MThlYmZhOTE0MTMxZjZmZTE1OS5zZXRJY29uKGljb25fYmM3MDE3NDk0OWNiNDQ1MTliNjcyN2IxMGNjNzRkOGMpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzMyMDUzNWU5OWRiYjQxNDk5MzhhZTkzNDNkODIwZjM1ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF84OTc4MGUzNTA5MjE0MmU0YTk1MTVmMTUzNzNhMjlkNyA9ICQoYDxkaXYgaWQ9Imh0bWxfODk3ODBlMzUwOTIxNDJlNGE5NTE1ZjE1MzczYTI5ZDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJhdGluZzo5LjIsIEFkZHJlc3M6MTcyIFdhdmVybHkgUGwsIFByaWNlX1RpZXI6MywgIEF2b2lkIFRpbWU6MTA6MDAgQU3igJMxOjAwIEFNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzMyMDUzNWU5OWRiYjQxNDk5MzhhZTkzNDNkODIwZjM1LnNldENvbnRlbnQoaHRtbF84OTc4MGUzNTA5MjE0MmU0YTk1MTVmMTUzNzNhMjlkNyk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9jNjM0YTk1MmUwOTg0MThlYmZhOTE0MTMxZjZmZTE1OS5iaW5kUG9wdXAocG9wdXBfMzIwNTM1ZTk5ZGJiNDE0OTkzOGFlOTM0M2Q4MjBmMzUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9jNjM0YTk1MmUwOTg0MThlYmZhOTE0MTMxZjZmZTE1OS5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBKZWZmcmV5J3MgR3JvY2VyeQogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl9iOTkxNGE4Yzc3M2Q0YmMwOWVhYzdmMjQ2MzdjMzJjOSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyNjMzMSwgLTczLjk4NjQ1M10sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fMjg4YTRkM2E5YjYxNDljNDk4YzFkNzRiYzMyMTlkNzYgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImluZm8tc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAicmVkIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfYjk5MTRhOGM3NzNkNGJjMDllYWM3ZjI0NjM3YzMyYzkuc2V0SWNvbihpY29uXzI4OGE0ZDNhOWI2MTQ5YzQ5OGMxZDc0YmMzMjE5ZDc2KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF85YTVhMTA4MjViZDc0MThmODFjNjJlMzZlNzVjODUwOSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfN2VkNTIwNDVhZmVhNGQ5MTg4NzUzOTZkNzk4NmI4ZGQgPSAkKGA8ZGl2IGlkPSJodG1sXzdlZDUyMDQ1YWZlYTRkOTE4ODc1Mzk2ZDc5ODZiOGRkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXRpbmc6OS4yLCBBZGRyZXNzOjk1IDFzdCBBdmUsIFByaWNlX1RpZXI6MywgIEF2b2lkIFRpbWU6NTowMCBQTeKAkzExOjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzlhNWExMDgyNWJkNzQxOGY4MWM2MmUzNmU3NWM4NTA5LnNldENvbnRlbnQoaHRtbF83ZWQ1MjA0NWFmZWE0ZDkxODg3NTM5NmQ3OTg2YjhkZCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9iOTkxNGE4Yzc3M2Q0YmMwOWVhYzdmMjQ2MzdjMzJjOS5iaW5kUG9wdXAocG9wdXBfOWE1YTEwODI1YmQ3NDE4ZjgxYzYyZTM2ZTc1Yzg1MDkpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9iOTkxNGE4Yzc3M2Q0YmMwOWVhYzdmMjQ2MzdjMzJjOS5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBVcHN0YXRlIENyYWZ0IEJlZXIgYW5kIE95c3RlciBCYXIKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfZWJlNzQyMDZhMmVlNGIxMGI1N2FlYzRhYjFiODdjNzAgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDMyOTQ3MTI4MjkzOSwgLTczLjk5MjUyNjAzNDU0MzA4XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl83NGI2M2Y0YzU2MzU0ZTM0OGI0NThiYzVhOWRkZmMyMyA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibGFjayIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2ViZTc0MjA2YTJlZTRiMTBiNTdhZWM0YWIxYjg3YzcwLnNldEljb24oaWNvbl83NGI2M2Y0YzU2MzU0ZTM0OGI0NThiYzVhOWRkZmMyMyk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMzBlOTg4OGJkMTljNDcwOTk2NzlkMjkwODZmZTM5YTMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzg1NzExNjhlODU4MTQ2NDc5OTQyYzQyOTJmNjA4YWEyID0gJChgPGRpdiBpZD0iaHRtbF84NTcxMTY4ZTg1ODE0NjQ3OTk0MmM0MjkyZjYwOGFhMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmF0aW5nOjkuMiwgQWRkcmVzczo0MCBXYXRlciBTdCwgUHJpY2VfVGllcjpOL0EsICBBdm9pZCBUaW1lOjg6MDAgQU3igJM2OjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzMwZTk4ODhiZDE5YzQ3MDk5Njc5ZDI5MDg2ZmUzOWEzLnNldENvbnRlbnQoaHRtbF84NTcxMTY4ZTg1ODE0NjQ3OTk0MmM0MjkyZjYwOGFhMik7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9lYmU3NDIwNmEyZWU0YjEwYjU3YWVjNGFiMWI4N2M3MC5iaW5kUG9wdXAocG9wdXBfMzBlOTg4OGJkMTljNDcwOTk2NzlkMjkwODZmZTM5YTMpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9lYmU3NDIwNmEyZWU0YjEwYjU3YWVjNGFiMWI4N2M3MC5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBCdXRsZXIgQmFrZXNob3AKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfYmI5NjMxZWYyZWNiNDQ4NjkyZTIyOTk3MTFjOTcyODAgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjYxNjY2Nzg4OTAxNiwgLTc0LjAwMjYwNzEyMjAyMThdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDczM2U4MmNjMWU4NGE4Yzg2ZDMxMWUyNmZhZTk5YzApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzY1NWE5ODJhODI3NjQzZDE4Y2I3ZDVhMmY4YjFhYmQwID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJpbmZvLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogInJlZCIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2JiOTYzMWVmMmVjYjQ0ODY5MmUyMjk5NzExYzk3MjgwLnNldEljb24oaWNvbl82NTVhOTgyYTgyNzY0M2QxOGNiN2Q1YTJmOGIxYWJkMCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMTJlYTg0ODMwOTM5NDg0ZjkzYmNkZmZjOWE0ZTIwNDkgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzFhZmZjYmQ1MDA3NjQ1OWNhM2I3NTgzYWNiNGQ0ODZlID0gJChgPGRpdiBpZD0iaHRtbF8xYWZmY2JkNTAwNzY0NTljYTNiNzU4M2FjYjRkNDg2ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmF0aW5nOjkuMiwgQWRkcmVzczoxMTkgU3VsbGl2YW4gU3QsIFByaWNlX1RpZXI6MywgIEF2b2lkIFRpbWU6MjowMCBQTeKAk01pZG5pZ2h0PC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzEyZWE4NDgzMDkzOTQ4NGY5M2JjZGZmYzlhNGUyMDQ5LnNldENvbnRlbnQoaHRtbF8xYWZmY2JkNTAwNzY0NTljYTNiNzU4M2FjYjRkNDg2ZSk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9iYjk2MzFlZjJlY2I0NDg2OTJlMjI5OTcxMWM5NzI4MC5iaW5kUG9wdXAocG9wdXBfMTJlYTg0ODMwOTM5NDg0ZjkzYmNkZmZjOWE0ZTIwNDkpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9iYjk2MzFlZjJlY2I0NDg2OTJlMjI5OTcxMWM5NzI4MC5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBCbHVlIFJpYmJvbiBTdXNoaQogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl84MjMwMGNlNTdmZjA0MDE5OWVjNjJkMDRjY2I5ZjAxYSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczMzY4MTQzNjIwMjE1NCwgLTc0LjAwMTc2NzI2ODY4MTEyXSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl8wZjRjM2VkZWUyMzI0NjQxOTQ4YmI5MWUxZTgxYzliMyA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJyZWQiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl84MjMwMGNlNTdmZjA0MDE5OWVjNjJkMDRjY2I5ZjAxYS5zZXRJY29uKGljb25fMGY0YzNlZGVlMjMyNDY0MTk0OGJiOTFlMWU4MWM5YjMpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzQ4NmNkMDNiYTkzZDQ0NTA5YTNkZDAyMGNhODg1ZjcyID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8yMTdlYmEwZmIwY2E0NjI0YjAwODVhMjZkMTk0NzM4MCA9ICQoYDxkaXYgaWQ9Imh0bWxfMjE3ZWJhMGZiMGNhNDYyNGIwMDg1YTI2ZDE5NDczODAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJhdGluZzo5LjIsIEFkZHJlc3M6MTcwIFdhdmVybHkgUGwsIFByaWNlX1RpZXI6MywgIEF2b2lkIFRpbWU6MTA6MDAgQU3igJM0OjAwIFBNNjowMCBQTeKAkzE6MDAgQU08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNDg2Y2QwM2JhOTNkNDQ1MDlhM2RkMDIwY2E4ODVmNzIuc2V0Q29udGVudChodG1sXzIxN2ViYTBmYjBjYTQ2MjRiMDA4NWEyNmQxOTQ3MzgwKTsKICAgICAgICAKCiAgICAgICAgbWFya2VyXzgyMzAwY2U1N2ZmMDQwMTk5ZWM2MmQwNGNjYjlmMDFhLmJpbmRQb3B1cChwb3B1cF80ODZjZDAzYmE5M2Q0NDUwOWEzZGQwMjBjYTg4NWY3MikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyXzgyMzAwY2U1N2ZmMDQwMTk5ZWM2MmQwNGNjYjlmMDFhLmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIEpvc2VwaCBMZW9uYXJkCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyX2NlZWJiNDM0YjgxMDRjODQ4Zjk5MTMyMGI5ZGVlNmRkID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI3NDA0MTkzMzYzNzI1LCAtNzQuMDAyNjk2MzcyMjQ4NV0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fMDc0YmM1ZmJiMGU4NGYxMmE3OTA4ZDllYzU0YzVmYWYgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImluZm8tc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmxhY2siLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl9jZWViYjQzNGI4MTA0Yzg0OGY5OTEzMjBiOWRlZTZkZC5zZXRJY29uKGljb25fMDc0YmM1ZmJiMGU4NGYxMmE3OTA4ZDllYzU0YzVmYWYpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzJjNGZlNjk4MzgxYTQ3MDRhYjkxZWIwOWQ0MWY0OTQ3ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9kZTA2OGQ2ZmVjNDU0ZTNkYjc4NWQzMThmYzMzYjgwNiA9ICQoYDxkaXYgaWQ9Imh0bWxfZGUwNjhkNmZlYzQ1NGUzZGI3ODVkMzE4ZmMzM2I4MDYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJhdGluZzo5LjIsIEFkZHJlc3M6NDggTWFjZG91Z2FsIFN0LCBQcmljZV9UaWVyOk4vQSwgIEF2b2lkIFRpbWU6Tm9vbuKAkzEwOjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzJjNGZlNjk4MzgxYTQ3MDRhYjkxZWIwOWQ0MWY0OTQ3LnNldENvbnRlbnQoaHRtbF9kZTA2OGQ2ZmVjNDU0ZTNkYjc4NWQzMThmYzMzYjgwNik7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9jZWViYjQzNGI4MTA0Yzg0OGY5OTEzMjBiOWRlZTZkZC5iaW5kUG9wdXAocG9wdXBfMmM0ZmU2OTgzODFhNDcwNGFiOTFlYjA5ZDQxZjQ5NDcpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9jZWViYjQzNGI4MTA0Yzg0OGY5OTEzMjBiOWRlZTZkZC5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBSYWt1CiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzQwZDZmZWNlYTFlNjRiOTZhMTVjMmVmMzU0NDgxMmUyID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI3Mjc3MzUzNTg0NTgsIC03My45ODQ1MDUyOTgwMDE4OF0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fNzdmNmVhMWNmOGU4NDEyMDg0ZTdiMDU3ODg0ZGZiZDAgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImluZm8tc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmx1ZSIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyXzQwZDZmZWNlYTFlNjRiOTZhMTVjMmVmMzU0NDgxMmUyLnNldEljb24oaWNvbl83N2Y2ZWExY2Y4ZTg0MTIwODRlN2IwNTc4ODRkZmJkMCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfOGI5NTU1MmFjZjlmNDY1NThlYmIzMDA2MjQ1NDA2YmYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2U4NTI2NzFmNDI0MDRmOGM5M2MyOGFkNTYzZWU4ZTg0ID0gJChgPGRpdiBpZD0iaHRtbF9lODUyNjcxZjQyNDA0ZjhjOTNjMjhhZDU2M2VlOGU4NCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmF0aW5nOjkuMiwgQWRkcmVzczoxMDEgU2FpbnQgTWFya3MgUGwsIFByaWNlX1RpZXI6MiwgIEF2b2lkIFRpbWU6MTA6MDAgQU3igJM0OjAwIFBNNjowMCBQTeKAkzExOjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzhiOTU1NTJhY2Y5ZjQ2NTU4ZWJiMzAwNjI0NTQwNmJmLnNldENvbnRlbnQoaHRtbF9lODUyNjcxZjQyNDA0ZjhjOTNjMjhhZDU2M2VlOGU4NCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl80MGQ2ZmVjZWExZTY0Yjk2YTE1YzJlZjM1NDQ4MTJlMi5iaW5kUG9wdXAocG9wdXBfOGI5NTU1MmFjZjlmNDY1NThlYmIzMDA2MjQ1NDA2YmYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl80MGQ2ZmVjZWExZTY0Yjk2YTE1YzJlZjM1NDQ4MTJlMi5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBDYWZlIE1vZ2Fkb3IKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfYzc1YmQ5ZTRjMmY0NDRlZDlmMmI4ODllZGMxMjczOTggPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjY4MDI2NDQ2OTkzNzYsIC03My45ODM0NDQwNzUyMzY0NV0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF9kNzMzZTgyY2MxZTg0YThjODZkMzExZTI2ZmFlOTljMCk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fM2JiMWI1MzBmMTY0NGRlZTkyODAwZDdiZTlmNzUwYTUgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogImluZm8tc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAicmVkIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfYzc1YmQ5ZTRjMmY0NDRlZDlmMmI4ODllZGMxMjczOTguc2V0SWNvbihpY29uXzNiYjFiNTMwZjE2NDRkZWU5MjgwMGQ3YmU5Zjc1MGE1KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF83MjYyM2Q3NTY0NWU0MjMwYWQ2OGFkMjQ4ODA0Mjc3ZiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYjYwM2U5Yzk4NjJhNDgxYjg1YjlmMDRlYjBiNjNjYWMgPSAkKGA8ZGl2IGlkPSJodG1sX2I2MDNlOWM5ODYyYTQ4MWI4NWI5ZjA0ZWIwYjYzY2FjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXRpbmc6OS4yLCBBZGRyZXNzOjEzMCBTYWludCBNYXJrcyBQbCwgUHJpY2VfVGllcjo0LCAgQXZvaWQgVGltZTo1OjAwIFBN4oCTMTE6MDAgUE08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNzI2MjNkNzU2NDVlNDIzMGFkNjhhZDI0ODgwNDI3N2Yuc2V0Q29udGVudChodG1sX2I2MDNlOWM5ODYyYTQ4MWI4NWI5ZjA0ZWIwYjYzY2FjKTsKICAgICAgICAKCiAgICAgICAgbWFya2VyX2M3NWJkOWU0YzJmNDQ0ZWQ5ZjJiODg5ZWRjMTI3Mzk4LmJpbmRQb3B1cChwb3B1cF83MjYyM2Q3NTY0NWU0MjMwYWQ2OGFkMjQ4ODA0Mjc3ZikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyX2M3NWJkOWU0YzJmNDQ0ZWQ5ZjJiODg5ZWRjMTI3Mzk4LmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIEt1cmEKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfOWU0ZmJiMzExMDZlNDAyNDhiOTE3ZWY4YjE0NTMzZDkgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjM3MTU0MDEyNDQxMSwgLTczLjk3OTEyMDk4MjI4MDY5XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2Q3MzNlODJjYzFlODRhOGM4NmQzMTFlMjZmYWU5OWMwKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl9jYzBhNzUwNzQ3Mjc0Y2U3YmUxMjg1MjdkMGYxOTVhNyA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAiaW5mby1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibHVlIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfOWU0ZmJiMzExMDZlNDAyNDhiOTE3ZWY4YjE0NTMzZDkuc2V0SWNvbihpY29uX2NjMGE3NTA3NDcyNzRjZTdiZTEyODUyN2QwZjE5NWE3KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF83MmZmYThmOTBmM2E0ZWNiOGQyZmNkYTBmY2ZhNGE0YiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYjI1ZjhiZGFmMTEwNGVlZTkyYTZmNzM2NDhlMzM3NTIgPSAkKGA8ZGl2IGlkPSJodG1sX2IyNWY4YmRhZjExMDRlZWU5MmE2ZjczNjQ4ZTMzNzUyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXRpbmc6OS4yLCBBZGRyZXNzOjk0IEF2ZW51ZSBDLCBQcmljZV9UaWVyOjIsICBBdm9pZCBUaW1lOk5vb27igJMxMTowMCBQTTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF83MmZmYThmOTBmM2E0ZWNiOGQyZmNkYTBmY2ZhNGE0Yi5zZXRDb250ZW50KGh0bWxfYjI1ZjhiZGFmMTEwNGVlZTkyYTZmNzM2NDhlMzM3NTIpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfOWU0ZmJiMzExMDZlNDAyNDhiOTE3ZWY4YjE0NTMzZDkuYmluZFBvcHVwKHBvcHVwXzcyZmZhOGY5MGYzYTRlY2I4ZDJmY2RhMGZjZmE0YTRiKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfOWU0ZmJiMzExMDZlNDAyNDhiOTE3ZWY4YjE0NTMzZDkuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgQm9id2hpdGUgQ291bnRlcgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCjwvc2NyaXB0Pg== onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
# add clusters into map
map_chinatown = folium.Map(location=[latitude, longitude], zoom_start=14)
```


```python
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
    
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvZ2gvcHl0aG9uLXZpc3VhbGl6YXRpb24vZm9saXVtL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5taW4uY3NzIi8+CiAgICA8c3R5bGU+aHRtbCwgYm9keSB7d2lkdGg6IDEwMCU7aGVpZ2h0OiAxMDAlO21hcmdpbjogMDtwYWRkaW5nOiAwO308L3N0eWxlPgogICAgPHN0eWxlPiNtYXAge3Bvc2l0aW9uOmFic29sdXRlO3RvcDowO2JvdHRvbTowO3JpZ2h0OjA7bGVmdDowO308L3N0eWxlPgogICAgCiAgICAgICAgICAgIDxtZXRhIG5hbWU9InZpZXdwb3J0IiBjb250ZW50PSJ3aWR0aD1kZXZpY2Utd2lkdGgsCiAgICAgICAgICAgICAgICBpbml0aWFsLXNjYWxlPTEuMCwgbWF4aW11bS1zY2FsZT0xLjAsIHVzZXItc2NhbGFibGU9bm8iIC8+CiAgICAgICAgICAgIDxzdHlsZT4KICAgICAgICAgICAgICAgICNtYXBfZTkyMzNkYjIyYTMzNDgwMGIxNmRkNzFkZGM3NWJmYmIgewogICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgICAgICB3aWR0aDogMTAwLjAlOwogICAgICAgICAgICAgICAgICAgIGhlaWdodDogMTAwLjAlOwogICAgICAgICAgICAgICAgICAgIGxlZnQ6IDAuMCU7CiAgICAgICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL2xlYWZsZXQubWFya2VyY2x1c3Rlci8xLjEuMC9sZWFmbGV0Lm1hcmtlcmNsdXN0ZXIuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9sZWFmbGV0Lm1hcmtlcmNsdXN0ZXIvMS4xLjAvTWFya2VyQ2x1c3Rlci5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvbGVhZmxldC5tYXJrZXJjbHVzdGVyLzEuMS4wL01hcmtlckNsdXN0ZXIuRGVmYXVsdC5jc3MiLz4KPC9oZWFkPgo8Ym9keT4gICAgCiAgICAKICAgICAgICAgICAgPGRpdiBjbGFzcz0iZm9saXVtLW1hcCIgaWQ9Im1hcF9lOTIzM2RiMjJhMzM0ODAwYjE2ZGQ3MWRkYzc1YmZiYiIgPjwvZGl2PgogICAgICAgIAo8L2JvZHk+CjxzY3JpcHQ+ICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXBfZTkyMzNkYjIyYTMzNDgwMGIxNmRkNzFkZGM3NWJmYmIgPSBMLm1hcCgKICAgICAgICAgICAgICAgICJtYXBfZTkyMzNkYjIyYTMzNDgwMGIxNmRkNzFkZGM3NWJmYmIiLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGNlbnRlcjogWzQwLjcxNTYxODQyMjMxNDMyLCAtNzMuOTk0Mjc5MzYyNTU5NzhdLAogICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcsCiAgICAgICAgICAgICAgICAgICAgem9vbTogMTQsCiAgICAgICAgICAgICAgICAgICAgem9vbUNvbnRyb2w6IHRydWUsCiAgICAgICAgICAgICAgICAgICAgcHJlZmVyQ2FudmFzOiBmYWxzZSwKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgKTsKCiAgICAgICAgICAgIAoKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl9hZjM5ODMyZWI4MmQ0MzdkYTAxYmFiYjQ5M2E0OGFhMCA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgImh0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nIiwKICAgICAgICAgICAgICAgIHsiYXR0cmlidXRpb24iOiAiRGF0YSBieSBcdTAwMjZjb3B5OyBcdTAwM2NhIGhyZWY9XCJodHRwOi8vb3BlbnN0cmVldG1hcC5vcmdcIlx1MDAzZU9wZW5TdHJlZXRNYXBcdTAwM2MvYVx1MDAzZSwgdW5kZXIgXHUwMDNjYSBocmVmPVwiaHR0cDovL3d3dy5vcGVuc3RyZWV0bWFwLm9yZy9jb3B5cmlnaHRcIlx1MDAzZU9EYkxcdTAwM2MvYVx1MDAzZS4iLCAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsICJtYXhOYXRpdmVab29tIjogMTgsICJtYXhab29tIjogMTgsICJtaW5ab29tIjogMCwgIm5vV3JhcCI6IGZhbHNlLCAib3BhY2l0eSI6IDEsICJzdWJkb21haW5zIjogImFiYyIsICJ0bXMiOiBmYWxzZX0KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZTkyMzNkYjIyYTMzNDgwMGIxNmRkNzFkZGM3NWJmYmIpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfY2x1c3Rlcl83YjI0YjgzN2I2NDA0OGFlOWQ5ZjEyMzFkYmJhMDQ3YyA9IEwubWFya2VyQ2x1c3Rlckdyb3VwKAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFwX2U5MjMzZGIyMmEzMzQ4MDBiMTZkZDcxZGRjNzViZmJiLmFkZExheWVyKG1hcmtlcl9jbHVzdGVyXzdiMjRiODM3YjY0MDQ4YWU5ZDlmMTIzMWRiYmEwNDdjKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzkwNjA5YzFjZWZiODQ2NjZiZmUwZmY4NTkxNWEyOTM1ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzMwOTEyNTc1NjE5MTM2LCAtNzMuOTkzMjU5MTQzNzEwNV0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcmtlcl9jbHVzdGVyXzdiMjRiODM3YjY0MDQ4YWU5ZDlmMTIzMWRiYmEwNDdjKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl9jNzI5NGU0ZjZjYWU0ZDI5OTNmZWZkZTVlZmZiNzAwYyA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAib2stc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmxhY2siLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl85MDYwOWMxY2VmYjg0NjY2YmZlMGZmODU5MTVhMjkzNS5zZXRJY29uKGljb25fYzcyOTRlNGY2Y2FlNGQyOTkzZmVmZGU1ZWZmYjcwMGMpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2Q4ZmE1MjJjYzRhMjQzNGNiODljZjZiNzVmMjIyMjVmID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8zMjE3NjBkYjA0MmI0ZDkwYjE3YmE4ODlkYTU1ZTJlOCA9ICQoYDxkaXYgaWQ9Imh0bWxfMzIxNzYwZGIwNDJiNGQ5MGIxN2JhODg5ZGE1NWUyZTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZHJlc3M6NjMgRSA4dGggU3QsIFJhdGluZzo5LjQsIFByaWNlIFRpZXI6Ti9BLC9uIEF2b2lkIFRpbWU6NzowMCBBTeKAkzM6MDAgUE08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZDhmYTUyMmNjNGEyNDM0Y2I4OWNmNmI3NWYyMjIyNWYuc2V0Q29udGVudChodG1sXzMyMTc2MGRiMDQyYjRkOTBiMTdiYTg4OWRhNTVlMmU4KTsKICAgICAgICAKCiAgICAgICAgbWFya2VyXzkwNjA5YzFjZWZiODQ2NjZiZmUwZmY4NTkxNWEyOTM1LmJpbmRQb3B1cChwb3B1cF9kOGZhNTIyY2M0YTI0MzRjYjg5Y2Y2Yjc1ZjIyMjI1ZikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyXzkwNjA5YzFjZWZiODQ2NjZiZmUwZmY4NTkxNWEyOTM1LmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIEJvYndoaXRlIENvdW50ZXIKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfYzU0OGUxOGI2MmI5NGUwNzllZTFlMWIwNzk4ZDAzYWEgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzExMTY2MTA4NzU5OCwgLTc0LjAwMzA0MjU3ODY5NzJdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXJrZXJfY2x1c3Rlcl83YjI0YjgzN2I2NDA0OGFlOWQ5ZjEyMzFkYmJhMDQ3Yyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fZmNhOTM5YTI5NTFlNDNmMjg5NmRhNjgyZmMyNTE4MTEgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogIm9rLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImdyZWVuIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfYzU0OGUxOGI2MmI5NGUwNzllZTFlMWIwNzk4ZDAzYWEuc2V0SWNvbihpY29uX2ZjYTkzOWEyOTUxZTQzZjI4OTZkYTY4MmZjMjUxODExKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hYWRkMzU1ZmQ2MWU0MzQyYThmMDM3ZmZlNTEyN2ZjNyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZjk4Yzg4ODRmNDIyNGRlNGE1MzBkZmZmNDg1NjdlMzQgPSAkKGA8ZGl2IGlkPSJodG1sX2Y5OGM4ODg0ZjQyMjRkZTRhNTMwZGZmZjQ4NTY3ZTM0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BZGRyZXNzOjI2MCBCbGVlY2tlciBTdCwgUmF0aW5nOjkuNCwgUHJpY2UgVGllcjoyLC9uIEF2b2lkIFRpbWU6MTA6MDAgQU3igJM2OjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2FhZGQzNTVmZDYxZTQzNDJhOGYwMzdmZmU1MTI3ZmM3LnNldENvbnRlbnQoaHRtbF9mOThjODg4NGY0MjI0ZGU0YTUzMGRmZmY0ODU2N2UzNCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9jNTQ4ZTE4YjYyYjk0ZTA3OWVlMWUxYjA3OThkMDNhYS5iaW5kUG9wdXAocG9wdXBfYWFkZDM1NWZkNjFlNDM0MmE4ZjAzN2ZmZTUxMjdmYzcpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9jNTQ4ZTE4YjYyYjk0ZTA3OWVlMWUxYjA3OThkMDNhYS5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBCb2J3aGl0ZSBDb3VudGVyCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyX2RiOWU5OTlhY2RmYTQ3OTQ4YmUxM2Q5NmQ4ZDc1MGRhID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzM1MjE5NDk1OTIzMjA0LCAtNzQuMDAwNjQ4ODE4ODg3MV0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcmtlcl9jbHVzdGVyXzdiMjRiODM3YjY0MDQ4YWU5ZDlmMTIzMWRiYmEwNDdjKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl85NDBkZWIxZjk3ZTg0YWJlYmRiZmRlMDU5MjkxYmNjNiA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAib2stc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmxhY2siLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl9kYjllOTk5YWNkZmE0Nzk0OGJlMTNkOTZkOGQ3NTBkYS5zZXRJY29uKGljb25fOTQwZGViMWY5N2U4NGFiZWJkYmZkZTA1OTI5MWJjYzYpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2ViOWFkNDI2MTNmNDQyNmE4YTMyNDliYjRhMDY1MTZiID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xM2M0ZjFiYzJiZjk0MmQ4OTdmZjNkYmZlNDZhZGY5ZSA9ICQoYDxkaXYgaWQ9Imh0bWxfMTNjNGYxYmMyYmY5NDJkODk3ZmYzZGJmZTQ2YWRmOWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZHJlc3M6NCBDaGFybGVzIFN0LCBSYXRpbmc6OS4zLCBQcmljZSBUaWVyOk4vQSwvbiBBdm9pZCBUaW1lOjU6MDAgUE3igJNNaWRuaWdodDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9lYjlhZDQyNjEzZjQ0MjZhOGEzMjQ5YmI0YTA2NTE2Yi5zZXRDb250ZW50KGh0bWxfMTNjNGYxYmMyYmY5NDJkODk3ZmYzZGJmZTQ2YWRmOWUpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfZGI5ZTk5OWFjZGZhNDc5NDhiZTEzZDk2ZDhkNzUwZGEuYmluZFBvcHVwKHBvcHVwX2ViOWFkNDI2MTNmNDQyNmE4YTMyNDliYjRhMDY1MTZiKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfZGI5ZTk5OWFjZGZhNDc5NDhiZTEzZDk2ZDhkNzUwZGEuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgQm9id2hpdGUgQ291bnRlcgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl9mNWY5ZTZlYzc1ZGY0NDcwOTMwZTI3NWI0YjdlN2E2YiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyNTI5OTc5NjA5MTM1NiwgLTc0LjAwMzUwNzMzOTc0Nzk3XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFya2VyX2NsdXN0ZXJfN2IyNGI4MzdiNjQwNDhhZTlkOWYxMjMxZGJiYTA0N2MpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzlkMmQwZDZiN2NlNzQ3ODFiODI2YWJjMDE2NWIzN2E1ID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJvay1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibGFjayIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2Y1ZjllNmVjNzVkZjQ0NzA5MzBlMjc1YjRiN2U3YTZiLnNldEljb24oaWNvbl85ZDJkMGQ2YjdjZTc0NzgxYjgyNmFiYzAxNjViMzdhNSk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMzhkNTg3MTkzM2VmNDllMmI4Njc0NmNkY2Q1YWNiMWYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzFmYmNmZDNmNDBiYjQwZmZhYjg1MjdlMDg0NjZlMDEwID0gJChgPGRpdiBpZD0iaHRtbF8xZmJjZmQzZjQwYmI0MGZmYWI4NTI3ZTA4NDY2ZTAxMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRkcmVzczoyMDIgU3ByaW5nIFN0LCBSYXRpbmc6OS4zLCBQcmljZSBUaWVyOk4vQSwvbiBBdm9pZCBUaW1lOk5vb27igJMxMTowMCBQTTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8zOGQ1ODcxOTMzZWY0OWUyYjg2NzQ2Y2RjZDVhY2IxZi5zZXRDb250ZW50KGh0bWxfMWZiY2ZkM2Y0MGJiNDBmZmFiODUyN2UwODQ2NmUwMTApOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfZjVmOWU2ZWM3NWRmNDQ3MDkzMGUyNzViNGI3ZTdhNmIuYmluZFBvcHVwKHBvcHVwXzM4ZDU4NzE5MzNlZjQ5ZTJiODY3NDZjZGNkNWFjYjFmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfZjVmOWU2ZWM3NWRmNDQ3MDkzMGUyNzViNGI3ZTdhNmIuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgQm9id2hpdGUgQ291bnRlcgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl84NmJhMmE4OTMyODE0ZTIyOGJlOGJlNjE3OTVlMWExMCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyNDU5MDAyMjQ0NzksIC03My45ODE2MDAyNjk2MDg1NV0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcmtlcl9jbHVzdGVyXzdiMjRiODM3YjY0MDQ4YWU5ZDlmMTIzMWRiYmEwNDdjKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl8xMjFkZTMwZWU4ZGI0YmEwODUxOTYxNGEzYjgzNDcyYiA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAib2stc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiZ3JlZW4iLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl84NmJhMmE4OTMyODE0ZTIyOGJlOGJlNjE3OTVlMWExMC5zZXRJY29uKGljb25fMTIxZGUzMGVlOGRiNGJhMDg1MTk2MTRhM2I4MzQ3MmIpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzVjNGJjNGVlMjJiYTQxZGRiY2UxNTE5YzljYTkyZTVhID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9hZTFhNTlhNGFjNzI0MjhiYmY1ZmM5YWY2NDE0NzU5YyA9ICQoYDxkaXYgaWQ9Imh0bWxfYWUxYTU5YTRhYzcyNDI4YmJmNWZjOWFmNjQxNDc1OWMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZHJlc3M6OTQgQXZlbnVlIEIsIFJhdGluZzo5LjMsIFByaWNlIFRpZXI6MSwvbiBBdm9pZCBUaW1lOk4vQTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF81YzRiYzRlZTIyYmE0MWRkYmNlMTUxOWM5Y2E5MmU1YS5zZXRDb250ZW50KGh0bWxfYWUxYTU5YTRhYzcyNDI4YmJmNWZjOWFmNjQxNDc1OWMpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfODZiYTJhODkzMjgxNGUyMjhiZThiZTYxNzk1ZTFhMTAuYmluZFBvcHVwKHBvcHVwXzVjNGJjNGVlMjJiYTQxZGRiY2UxNTE5YzljYTkyZTVhKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfODZiYTJhODkzMjgxNGUyMjhiZThiZTYxNzk1ZTFhMTAuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgQm9id2hpdGUgQ291bnRlcgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl8xNmE0NTI0OGIyMTg0YjI5YWE3MTYxODMxNzg0OTA3ZSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcwNjE4NjkzMDUzMDg2LCAtNzQuMDA3NDkwMTE2MDM3OTFdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXJrZXJfY2x1c3Rlcl83YjI0YjgzN2I2NDA0OGFlOWQ5ZjEyMzFkYmJhMDQ3Yyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fYWRhZjViNmViNjAzNGQ3M2FhMGQ3NmZhNGJlODNhM2EgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogIm9rLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImJsYWNrIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfMTZhNDUyNDhiMjE4NGIyOWFhNzE2MTgzMTc4NDkwN2Uuc2V0SWNvbihpY29uX2FkYWY1YjZlYjYwMzRkNzNhYTBkNzZmYTRiZTgzYTNhKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9kNDE5YWJjZWMxYTQ0YjllYWNlNGY5MTI1Y2IzMzk1OCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNDQzOTM2MmU2MDQ0NDI1ZThjMDZlY2MzMTE5OTZhODggPSAkKGA8ZGl2IGlkPSJodG1sXzQ0MzkzNjJlNjA0NDQyNWU4YzA2ZWNjMzExOTk2YTg4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BZGRyZXNzOjcwIFBpbmUgU3QsIFJhdGluZzo5LjMsIFByaWNlIFRpZXI6Ti9BLC9uIEF2b2lkIFRpbWU6Tm9vbuKAkzE6MDAgUE01OjAwIFBN4oCTMTE6MDAgUE08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZDQxOWFiY2VjMWE0NGI5ZWFjZTRmOTEyNWNiMzM5NTguc2V0Q29udGVudChodG1sXzQ0MzkzNjJlNjA0NDQyNWU4YzA2ZWNjMzExOTk2YTg4KTsKICAgICAgICAKCiAgICAgICAgbWFya2VyXzE2YTQ1MjQ4YjIxODRiMjlhYTcxNjE4MzE3ODQ5MDdlLmJpbmRQb3B1cChwb3B1cF9kNDE5YWJjZWMxYTQ0YjllYWNlNGY5MTI1Y2IzMzk1OCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyXzE2YTQ1MjQ4YjIxODRiMjlhYTcxNjE4MzE3ODQ5MDdlLmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIEJvYndoaXRlIENvdW50ZXIKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfOTY3ZGExYWFiYTcyNGQzM2JlYzMwZmZhYTk4MDA5N2UgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTkxMTM3MDM5ODIxMywgLTc0LjAwMDIwMTc0MzU1MTI2XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFya2VyX2NsdXN0ZXJfN2IyNGI4MzdiNjQwNDhhZTlkOWYxMjMxZGJiYTA0N2MpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uX2Q2YThkZGRlNWU2ZjRiM2NiNDYwODM0ZGM5MGJjOGIzID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJvay1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJyZWQiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl85NjdkYTFhYWJhNzI0ZDMzYmVjMzBmZmFhOTgwMDk3ZS5zZXRJY29uKGljb25fZDZhOGRkZGU1ZTZmNGIzY2I0NjA4MzRkYzkwYmM4YjMpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzcwOGFhMzYyYmExYjRiMmFhOWYzOWU2OWNkOTQxM2Q1ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF82YjhkMWE2ZjkxYjc0YjM1ODgwODYxYWEwNGJjMzIzYyA9ICQoYDxkaXYgaWQ9Imh0bWxfNmI4ZDFhNmY5MWI3NGIzNTg4MDg2MWFhMDRiYzMyM2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZHJlc3M6MTM4IExhZmF5ZXR0ZSBTdCwgUmF0aW5nOjkuMywgUHJpY2UgVGllcjozLC9uIEF2b2lkIFRpbWU6MTA6MDAgQU3igJMzOjAwIFBNNTowMCBQTeKAkzExOjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzcwOGFhMzYyYmExYjRiMmFhOWYzOWU2OWNkOTQxM2Q1LnNldENvbnRlbnQoaHRtbF82YjhkMWE2ZjkxYjc0YjM1ODgwODYxYWEwNGJjMzIzYyk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl85NjdkYTFhYWJhNzI0ZDMzYmVjMzBmZmFhOTgwMDk3ZS5iaW5kUG9wdXAocG9wdXBfNzA4YWEzNjJiYTFiNGIyYWE5ZjM5ZTY5Y2Q5NDEzZDUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl85NjdkYTFhYWJhNzI0ZDMzYmVjMzBmZmFhOTgwMDk3ZS5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBCb2J3aGl0ZSBDb3VudGVyCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzZlN2U0NDRmYjAxZDQzOWJhZmEwZTNjYWFiMTI3OTBhID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzE0MjY3LCAtNzQuMDA4NzU2XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFya2VyX2NsdXN0ZXJfN2IyNGI4MzdiNjQwNDhhZTlkOWYxMjMxZGJiYTA0N2MpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uX2QxZGM1NjQ4ZjUzNDQ5YWFhMGNhN2EwOTE2Mzg3OTAzID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJvay1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibGFjayIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyXzZlN2U0NDRmYjAxZDQzOWJhZmEwZTNjYWFiMTI3OTBhLnNldEljb24oaWNvbl9kMWRjNTY0OGY1MzQ0OWFhYTBjYTdhMDkxNjM4NzkwMyk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMDY2ZDk5YjM0NWJlNGE5OWE3Nzk0NmU0MDI2OGU0MmYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2MyMzcyMTU2MzA1NTQ1ZjFiYTRmMDRkMjA2MzI1MDMwID0gJChgPGRpdiBpZD0iaHRtbF9jMjM3MjE1NjMwNTU0NWYxYmE0ZjA0ZDIwNjMyNTAzMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRkcmVzczoxMzYgQ2h1cmNoIFN0LCBSYXRpbmc6OS4zLCBQcmljZSBUaWVyOk4vQSwvbiBBdm9pZCBUaW1lOjExOjAwIEFN4oCTOTowMCBQTTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8wNjZkOTliMzQ1YmU0YTk5YTc3OTQ2ZTQwMjY4ZTQyZi5zZXRDb250ZW50KGh0bWxfYzIzNzIxNTYzMDU1NDVmMWJhNGYwNGQyMDYzMjUwMzApOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfNmU3ZTQ0NGZiMDFkNDM5YmFmYTBlM2NhYWIxMjc5MGEuYmluZFBvcHVwKHBvcHVwXzA2NmQ5OWIzNDViZTRhOTlhNzc5NDZlNDAyNjhlNDJmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfNmU3ZTQ0NGZiMDFkNDM5YmFmYTBlM2NhYWIxMjc5MGEuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgQm9id2hpdGUgQ291bnRlcgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl9mZWUzZmFiZTA0NDE0NDBjYTA1ZGQyMDAwYzU2Y2Q2NSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxODI5MDg0Mzc1NzEsIC03My45OTI1ODM5NzUxOTU4OF0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcmtlcl9jbHVzdGVyXzdiMjRiODM3YjY0MDQ4YWU5ZDlmMTIzMWRiYmEwNDdjKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl85NjUwNDJiNDAxMGY0Nzk1YTZlODUyYTNiYmYxMDU0OSA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAib2stc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmxhY2siLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl9mZWUzZmFiZTA0NDE0NDBjYTA1ZGQyMDAwYzU2Y2Q2NS5zZXRJY29uKGljb25fOTY1MDQyYjQwMTBmNDc5NWE2ZTg1MmEzYmJmMTA1NDkpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzQwODQ5YzExOWM1NzQwNThiMGQyZWE2Y2YzZWU1NzhiID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xZDIwMTA4NWY3YzQ0MDQxYjNiOGQ3NTg1YzUwYWY3MSA9ICQoYDxkaXYgaWQ9Imh0bWxfMWQyMDEwODVmN2M0NDA0MWIzYjhkNzU4NWM1MGFmNzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZHJlc3M6MTAwIEZvcnN5dGggU3QsIFJhdGluZzo5LjMsIFByaWNlIFRpZXI6Ti9BLC9uIEF2b2lkIFRpbWU6MTE6MDAgQU3igJMzOjAwIFBNNTowMCBQTeKAkzExOjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzQwODQ5YzExOWM1NzQwNThiMGQyZWE2Y2YzZWU1NzhiLnNldENvbnRlbnQoaHRtbF8xZDIwMTA4NWY3YzQ0MDQxYjNiOGQ3NTg1YzUwYWY3MSk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9mZWUzZmFiZTA0NDE0NDBjYTA1ZGQyMDAwYzU2Y2Q2NS5iaW5kUG9wdXAocG9wdXBfNDA4NDljMTE5YzU3NDA1OGIwZDJlYTZjZjNlZTU3OGIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9mZWUzZmFiZTA0NDE0NDBjYTA1ZGQyMDAwYzU2Y2Q2NS5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBCb2J3aGl0ZSBDb3VudGVyCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyX2EyNDJjNjBlZDYxZTQyODQ4NWE1YmEwOTg2MzBjZGZiID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI5OTk4NDUzMjMzODIsIC03My45ODk2OTU2ODkzODQyXSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFya2VyX2NsdXN0ZXJfN2IyNGI4MzdiNjQwNDhhZTlkOWYxMjMxZGJiYTA0N2MpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uX2I4ZjJhNTBiNzZlMTQ2ZWFhOGU3ZGM5MWFkZDYwMDE2ID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJvay1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJibGFjayIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2EyNDJjNjBlZDYxZTQyODQ4NWE1YmEwOTg2MzBjZGZiLnNldEljb24oaWNvbl9iOGYyYTUwYjc2ZTE0NmVhYThlN2RjOTFhZGQ2MDAxNik7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMDc1MGZhYzlmYTFiNDYyZTk3NzczOTMyODkwMzc4ODAgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzYwZTk2NThkODM3NjQ0MGFiNzJiZmRkMzc4ZmFhNWZkID0gJChgPGRpdiBpZD0iaHRtbF82MGU5NjU4ZDgzNzY0NDBhYjcyYmZkZDM3OGZhYTVmZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRkcmVzczoyMCAzcmQgQXZlLCBSYXRpbmc6OS4yLCBQcmljZSBUaWVyOk4vQSwvbiBBdm9pZCBUaW1lOk5vb27igJNNaWRuaWdodDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8wNzUwZmFjOWZhMWI0NjJlOTc3NzM5MzI4OTAzNzg4MC5zZXRDb250ZW50KGh0bWxfNjBlOTY1OGQ4Mzc2NDQwYWI3MmJmZGQzNzhmYWE1ZmQpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfYTI0MmM2MGVkNjFlNDI4NDg1YTViYTA5ODYzMGNkZmIuYmluZFBvcHVwKHBvcHVwXzA3NTBmYWM5ZmExYjQ2MmU5Nzc3MzkzMjg5MDM3ODgwKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfYTI0MmM2MGVkNjFlNDI4NDg1YTViYTA5ODYzMGNkZmIuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgQm9id2hpdGUgQ291bnRlcgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl80NzUyZDQ5ODA2OTA0YzcyOTJkYTljZGRhOGE3Njk3ZCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxMjY2NTk3MTQ4MTQzNSwgLTc0LjAxNTkwMTA4ODcxNDZdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXJrZXJfY2x1c3Rlcl83YjI0YjgzN2I2NDA0OGFlOWQ5ZjEyMzFkYmJhMDQ3Yyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fZWEwYzI1MGZjNTY4NDc0NGI5ZDkyNTNjMThhOWU3MGIgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogIm9rLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImdyZWVuIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfNDc1MmQ0OTgwNjkwNGM3MjkyZGE5Y2RkYThhNzY5N2Quc2V0SWNvbihpY29uX2VhMGMyNTBmYzU2ODQ3NDRiOWQ5MjUzYzE4YTllNzBiKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hMWQ2ZjZiZTZjY2U0MzdmYjExNDA3ZjQ4OTMyZDc5YyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNTliMmNmNTg4NWNmNGIxYWI2OGI2YWJhZDQ4ZTk2OGUgPSAkKGA8ZGl2IGlkPSJodG1sXzU5YjJjZjU4ODVjZjRiMWFiNjhiNmFiYWQ0OGU5NjhlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BZGRyZXNzOjIyNSBMaWJlcnR5IFN0LCBSYXRpbmc6OS4yLCBQcmljZSBUaWVyOjIsL24gQXZvaWQgVGltZToxMTowMCBBTeKAkzk6MDAgUE08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTFkNmY2YmU2Y2NlNDM3ZmIxMTQwN2Y0ODkzMmQ3OWMuc2V0Q29udGVudChodG1sXzU5YjJjZjU4ODVjZjRiMWFiNjhiNmFiYWQ0OGU5NjhlKTsKICAgICAgICAKCiAgICAgICAgbWFya2VyXzQ3NTJkNDk4MDY5MDRjNzI5MmRhOWNkZGE4YTc2OTdkLmJpbmRQb3B1cChwb3B1cF9hMWQ2ZjZiZTZjY2U0MzdmYjExNDA3ZjQ4OTMyZDc5YykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyXzQ3NTJkNDk4MDY5MDRjNzI5MmRhOWNkZGE4YTc2OTdkLmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIEJvYndoaXRlIENvdW50ZXIKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfZGM3M2FjNWNhNzFlNGIzODlhMDJkNzEwYmFlODlkZjggPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjU4MTg2NzI5MjM1NSwgLTc0LjAwMDk4NDk1MDI0NTM1XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFya2VyX2NsdXN0ZXJfN2IyNGI4MzdiNjQwNDhhZTlkOWYxMjMxZGJiYTA0N2MpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uX2U1YjFjMTY4ZDk2ZDRjOTI5MTBjN2Q4OGQwNzQzYTA0ID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJvay1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJncmVlbiIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2RjNzNhYzVjYTcxZTRiMzg5YTAyZDcxMGJhZTg5ZGY4LnNldEljb24oaWNvbl9lNWIxYzE2OGQ5NmQ0YzkyOTEwYzdkODhkMDc0M2EwNCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMGQ1N2Y0MjUwMGZjNGZhZGIzMjljODgzYTk3YzE4N2EgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzRlY2FmMDU1MzIzMDRjNGJiYjhkYzYwYzhmOTQ4NTZkID0gJChgPGRpdiBpZD0iaHRtbF80ZWNhZjA1NTMyMzA0YzRiYmI4ZGM2MGM4Zjk0ODU2ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRkcmVzczoxNTIgUHJpbmNlIFN0LCBSYXRpbmc6OS4yLCBQcmljZSBUaWVyOjEsL24gQXZvaWQgVGltZToxMDowMCBBTeKAkzg6MDAgUE08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMGQ1N2Y0MjUwMGZjNGZhZGIzMjljODgzYTk3YzE4N2Euc2V0Q29udGVudChodG1sXzRlY2FmMDU1MzIzMDRjNGJiYjhkYzYwYzhmOTQ4NTZkKTsKICAgICAgICAKCiAgICAgICAgbWFya2VyX2RjNzNhYzVjYTcxZTRiMzg5YTAyZDcxMGJhZTg5ZGY4LmJpbmRQb3B1cChwb3B1cF8wZDU3ZjQyNTAwZmM0ZmFkYjMyOWM4ODNhOTdjMTg3YSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyX2RjNzNhYzVjYTcxZTRiMzg5YTAyZDcxMGJhZTg5ZGY4LmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIEJvYndoaXRlIENvdW50ZXIKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfMWU3ZjFhYmM5NzlkNDM0ZWE5NTUxMDNmNDA1ZjJkZDUgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzM5MTksIC03NC4wMDEzNDZdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXJrZXJfY2x1c3Rlcl83YjI0YjgzN2I2NDA0OGFlOWQ5ZjEyMzFkYmJhMDQ3Yyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fNWRmNzgyNzNjYjA5NGMyZTljN2QyMGZjNTVhODg5NzcgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogIm9rLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogInJlZCIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyXzFlN2YxYWJjOTc5ZDQzNGVhOTU1MTAzZjQwNWYyZGQ1LnNldEljb24oaWNvbl81ZGY3ODI3M2NiMDk0YzJlOWM3ZDIwZmM1NWE4ODk3Nyk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfOWI0ZjdmNWMzOTU3NGVmYzlmOTM5YjgwMzc1OGIyYTQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzAxNGZhMTMzMzM3YTQyMWU5NjA5MzdlMjUzZGQyN2IwID0gJChgPGRpdiBpZD0iaHRtbF8wMTRmYTEzMzMzN2E0MjFlOTYwOTM3ZTI1M2RkMjdiMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRkcmVzczoxNzIgV2F2ZXJseSBQbCwgUmF0aW5nOjkuMiwgUHJpY2UgVGllcjozLC9uIEF2b2lkIFRpbWU6MTA6MDAgQU3igJMxOjAwIEFNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzliNGY3ZjVjMzk1NzRlZmM5ZjkzOWI4MDM3NThiMmE0LnNldENvbnRlbnQoaHRtbF8wMTRmYTEzMzMzN2E0MjFlOTYwOTM3ZTI1M2RkMjdiMCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl8xZTdmMWFiYzk3OWQ0MzRlYTk1NTEwM2Y0MDVmMmRkNS5iaW5kUG9wdXAocG9wdXBfOWI0ZjdmNWMzOTU3NGVmYzlmOTM5YjgwMzc1OGIyYTQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl8xZTdmMWFiYzk3OWQ0MzRlYTk1NTEwM2Y0MDVmMmRkNS5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBCb2J3aGl0ZSBDb3VudGVyCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzkwZDRmNTkzNzYyNzRmOGJiNmEyNDUxYjI5OWNmZGEzID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI2MzMxLCAtNzMuOTg2NDUzXSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFya2VyX2NsdXN0ZXJfN2IyNGI4MzdiNjQwNDhhZTlkOWYxMjMxZGJiYTA0N2MpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uXzg2ODQyM2Y5Njg5OTRlOWViNGZlNDE5YWM1OTM1YTY1ID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJvay1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJyZWQiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl85MGQ0ZjU5Mzc2Mjc0ZjhiYjZhMjQ1MWIyOTljZmRhMy5zZXRJY29uKGljb25fODY4NDIzZjk2ODk5NGU5ZWI0ZmU0MTlhYzU5MzVhNjUpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzk2ODEwMTlkMzQ0MTQyMjJhOTM1M2E4YmVmNTQwMjBlID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF81YzI2NDU0M2ZiYjE0MDgwOTNlMzJhMzliZTI0ZjY5NSA9ICQoYDxkaXYgaWQ9Imh0bWxfNWMyNjQ1NDNmYmIxNDA4MDkzZTMyYTM5YmUyNGY2OTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZHJlc3M6OTUgMXN0IEF2ZSwgUmF0aW5nOjkuMiwgUHJpY2UgVGllcjozLC9uIEF2b2lkIFRpbWU6NTowMCBQTeKAkzExOjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzk2ODEwMTlkMzQ0MTQyMjJhOTM1M2E4YmVmNTQwMjBlLnNldENvbnRlbnQoaHRtbF81YzI2NDU0M2ZiYjE0MDgwOTNlMzJhMzliZTI0ZjY5NSk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl85MGQ0ZjU5Mzc2Mjc0ZjhiYjZhMjQ1MWIyOTljZmRhMy5iaW5kUG9wdXAocG9wdXBfOTY4MTAxOWQzNDQxNDIyMmE5MzUzYThiZWY1NDAyMGUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl85MGQ0ZjU5Mzc2Mjc0ZjhiYjZhMjQ1MWIyOTljZmRhMy5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBCb2J3aGl0ZSBDb3VudGVyCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyX2FiODJiNTdhNGRhMDRiM2E5YjY1OWQ0ZWEyZDA0YmI3ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzAzMjk0NzEyODI5MzksIC03My45OTI1MjYwMzQ1NDMwOF0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcmtlcl9jbHVzdGVyXzdiMjRiODM3YjY0MDQ4YWU5ZDlmMTIzMWRiYmEwNDdjKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl85OTk3YWUxODE1MjU0MjA2YTg5NDdlOWNiM2RiNzY3ZiA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAib2stc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmxhY2siLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl9hYjgyYjU3YTRkYTA0YjNhOWI2NTlkNGVhMmQwNGJiNy5zZXRJY29uKGljb25fOTk5N2FlMTgxNTI1NDIwNmE4OTQ3ZTljYjNkYjc2N2YpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2E0MTVmNmMyZDA4MzQ5MmE5MzQwOTZjZTYwZTY4YTFmID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9iZTZkM2UxMjg2YWM0NTAxODFhNWExOGY5ZDI0ODE2MyA9ICQoYDxkaXYgaWQ9Imh0bWxfYmU2ZDNlMTI4NmFjNDUwMTgxYTVhMThmOWQyNDgxNjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZHJlc3M6NDAgV2F0ZXIgU3QsIFJhdGluZzo5LjIsIFByaWNlIFRpZXI6Ti9BLC9uIEF2b2lkIFRpbWU6ODowMCBBTeKAkzY6MDAgUE08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTQxNWY2YzJkMDgzNDkyYTkzNDA5NmNlNjBlNjhhMWYuc2V0Q29udGVudChodG1sX2JlNmQzZTEyODZhYzQ1MDE4MWE1YTE4ZjlkMjQ4MTYzKTsKICAgICAgICAKCiAgICAgICAgbWFya2VyX2FiODJiNTdhNGRhMDRiM2E5YjY1OWQ0ZWEyZDA0YmI3LmJpbmRQb3B1cChwb3B1cF9hNDE1ZjZjMmQwODM0OTJhOTM0MDk2Y2U2MGU2OGExZikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyX2FiODJiNTdhNGRhMDRiM2E5YjY1OWQ0ZWEyZDA0YmI3LmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIEJvYndoaXRlIENvdW50ZXIKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfYjc0NDcxOGIyYWNiNGY1ZTk0MWZkNTllOTJiYTNiYjIgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjYxNjY2Nzg4OTAxNiwgLTc0LjAwMjYwNzEyMjAyMThdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXJrZXJfY2x1c3Rlcl83YjI0YjgzN2I2NDA0OGFlOWQ5ZjEyMzFkYmJhMDQ3Yyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fMmQxNzI1ODk2N2MwNGFkMGJjZTYyMjU5NWY3ZjNkN2YgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogIm9rLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogInJlZCIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2I3NDQ3MThiMmFjYjRmNWU5NDFmZDU5ZTkyYmEzYmIyLnNldEljb24oaWNvbl8yZDE3MjU4OTY3YzA0YWQwYmNlNjIyNTk1ZjdmM2Q3Zik7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMGE1YzY4YTM1NjA1NGFjYTlhZDVkZWU2NDFmNTJmMWYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzJmMzc3M2Y5OTU0MjQzNWQ4ZWFmOGUzN2M4MGMyMmEwID0gJChgPGRpdiBpZD0iaHRtbF8yZjM3NzNmOTk1NDI0MzVkOGVhZjhlMzdjODBjMjJhMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRkcmVzczoxMTkgU3VsbGl2YW4gU3QsIFJhdGluZzo5LjIsIFByaWNlIFRpZXI6MywvbiBBdm9pZCBUaW1lOjI6MDAgUE3igJNNaWRuaWdodDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8wYTVjNjhhMzU2MDU0YWNhOWFkNWRlZTY0MWY1MmYxZi5zZXRDb250ZW50KGh0bWxfMmYzNzczZjk5NTQyNDM1ZDhlYWY4ZTM3YzgwYzIyYTApOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfYjc0NDcxOGIyYWNiNGY1ZTk0MWZkNTllOTJiYTNiYjIuYmluZFBvcHVwKHBvcHVwXzBhNWM2OGEzNTYwNTRhY2E5YWQ1ZGVlNjQxZjUyZjFmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfYjc0NDcxOGIyYWNiNGY1ZTk0MWZkNTllOTJiYTNiYjIuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgQm9id2hpdGUgQ291bnRlcgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl8zZWFhZTVkM2IxMzI0OGM2YjFhMTY4OTUzZTM1ZjRhNSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczMzY4MTQzNjIwMjE1NCwgLTc0LjAwMTc2NzI2ODY4MTEyXSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFya2VyX2NsdXN0ZXJfN2IyNGI4MzdiNjQwNDhhZTlkOWYxMjMxZGJiYTA0N2MpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBpY29uX2IwYzU0OTFmOWRjYjRlYWE5MzliODk5ZDYxMmI0YzgyID0gTC5Bd2Vzb21lTWFya2Vycy5pY29uKAogICAgICAgICAgICAgICAgeyJleHRyYUNsYXNzZXMiOiAiZmEtcm90YXRlLTAiLCAiaWNvbiI6ICJvay1zaWduIiwgImljb25Db2xvciI6ICJ3aGl0ZSIsICJtYXJrZXJDb2xvciI6ICJyZWQiLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl8zZWFhZTVkM2IxMzI0OGM2YjFhMTY4OTUzZTM1ZjRhNS5zZXRJY29uKGljb25fYjBjNTQ5MWY5ZGNiNGVhYTkzOWI4OTlkNjEyYjRjODIpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2Y2NmRkNTBiNzgwMjRkODM5NjkyNDczOGRmMzNjNmQxID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF80YzIzZWU2MGJjM2U0NjhlYTJhYTc1Zjg2YzkwODRhMCA9ICQoYDxkaXYgaWQ9Imh0bWxfNGMyM2VlNjBiYzNlNDY4ZWEyYWE3NWY4NmM5MDg0YTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZHJlc3M6MTcwIFdhdmVybHkgUGwsIFJhdGluZzo5LjIsIFByaWNlIFRpZXI6MywvbiBBdm9pZCBUaW1lOjEwOjAwIEFN4oCTNDowMCBQTTY6MDAgUE3igJMxOjAwIEFNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2Y2NmRkNTBiNzgwMjRkODM5NjkyNDczOGRmMzNjNmQxLnNldENvbnRlbnQoaHRtbF80YzIzZWU2MGJjM2U0NjhlYTJhYTc1Zjg2YzkwODRhMCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl8zZWFhZTVkM2IxMzI0OGM2YjFhMTY4OTUzZTM1ZjRhNS5iaW5kUG9wdXAocG9wdXBfZjY2ZGQ1MGI3ODAyNGQ4Mzk2OTI0NzM4ZGYzM2M2ZDEpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl8zZWFhZTVkM2IxMzI0OGM2YjFhMTY4OTUzZTM1ZjRhNS5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBCb2J3aGl0ZSBDb3VudGVyCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzMwZDk1MTQwMGE5YjQ0OGJiMzc5YzExNmUyYzlhYWY0ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI3NDA0MTkzMzYzNzI1LCAtNzQuMDAyNjk2MzcyMjQ4NV0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcmtlcl9jbHVzdGVyXzdiMjRiODM3YjY0MDQ4YWU5ZDlmMTIzMWRiYmEwNDdjKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgaWNvbl85NTU4NzU5OGYzMjQ0ZmY0OGZlOTM2NjFkNDc1ZWM4YyA9IEwuQXdlc29tZU1hcmtlcnMuaWNvbigKICAgICAgICAgICAgICAgIHsiZXh0cmFDbGFzc2VzIjogImZhLXJvdGF0ZS0wIiwgImljb24iOiAib2stc2lnbiIsICJpY29uQ29sb3IiOiAid2hpdGUiLCAibWFya2VyQ29sb3IiOiAiYmxhY2siLCAicHJlZml4IjogImdseXBoaWNvbiJ9CiAgICAgICAgICAgICk7CiAgICAgICAgICAgIG1hcmtlcl8zMGQ5NTE0MDBhOWI0NDhiYjM3OWMxMTZlMmM5YWFmNC5zZXRJY29uKGljb25fOTU1ODc1OThmMzI0NGZmNDhmZTkzNjYxZDQ3NWVjOGMpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzk4YmRkNTEzYzQ3MTQ0ZTZiMGIwMjQ4YzkzMzQzZTY5ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9hM2E3OTRjYzQ1OTc0Y2IyYTViMThiNmE4Mzg2OGRiNCA9ICQoYDxkaXYgaWQ9Imh0bWxfYTNhNzk0Y2M0NTk3NGNiMmE1YjE4YjZhODM4NjhkYjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZHJlc3M6NDggTWFjZG91Z2FsIFN0LCBSYXRpbmc6OS4yLCBQcmljZSBUaWVyOk4vQSwvbiBBdm9pZCBUaW1lOk5vb27igJMxMDowMCBQTTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF85OGJkZDUxM2M0NzE0NGU2YjBiMDI0OGM5MzM0M2U2OS5zZXRDb250ZW50KGh0bWxfYTNhNzk0Y2M0NTk3NGNiMmE1YjE4YjZhODM4NjhkYjQpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfMzBkOTUxNDAwYTliNDQ4YmIzNzljMTE2ZTJjOWFhZjQuYmluZFBvcHVwKHBvcHVwXzk4YmRkNTEzYzQ3MTQ0ZTZiMGIwMjQ4YzkzMzQzZTY5KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfMzBkOTUxNDAwYTliNDQ4YmIzNzljMTE2ZTJjOWFhZjQuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgQm9id2hpdGUgQ291bnRlcgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl9jMDI0NGFhMjdmZGU0YjA3YmRkMWVmM2VmOWEwYjU4MCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyNzI3NzM1MzU4NDU4LCAtNzMuOTg0NTA1Mjk4MDAxODhdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXJrZXJfY2x1c3Rlcl83YjI0YjgzN2I2NDA0OGFlOWQ5ZjEyMzFkYmJhMDQ3Yyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fNzVhNDcyZTY3Nzg3NGVkMThiYTgzMWUyMjhkNTE3ZmYgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogIm9rLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImdyZWVuIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfYzAyNDRhYTI3ZmRlNGIwN2JkZDFlZjNlZjlhMGI1ODAuc2V0SWNvbihpY29uXzc1YTQ3MmU2Nzc4NzRlZDE4YmE4MzFlMjI4ZDUxN2ZmKTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zYWUyZWUzZTI1ZjQ0NjI1YjkyYjViZWM3YzE4M2NiOCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZGFhNTRjM2NmM2Y1NDAyYThmMWIyNmQ4YjMzMzgwNGQgPSAkKGA8ZGl2IGlkPSJodG1sX2RhYTU0YzNjZjNmNTQwMmE4ZjFiMjZkOGIzMzM4MDRkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BZGRyZXNzOjEwMSBTYWludCBNYXJrcyBQbCwgUmF0aW5nOjkuMiwgUHJpY2UgVGllcjoyLC9uIEF2b2lkIFRpbWU6MTA6MDAgQU3igJM0OjAwIFBNNjowMCBQTeKAkzExOjAwIFBNPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzNhZTJlZTNlMjVmNDQ2MjViOTJiNWJlYzdjMTgzY2I4LnNldENvbnRlbnQoaHRtbF9kYWE1NGMzY2YzZjU0MDJhOGYxYjI2ZDhiMzMzODA0ZCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl9jMDI0NGFhMjdmZGU0YjA3YmRkMWVmM2VmOWEwYjU4MC5iaW5kUG9wdXAocG9wdXBfM2FlMmVlM2UyNWY0NDYyNWI5MmI1YmVjN2MxODNjYjgpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIG1hcmtlcl9jMDI0NGFhMjdmZGU0YjA3YmRkMWVmM2VmOWEwYjU4MC5iaW5kVG9vbHRpcCgKICAgICAgICAgICAgICAgIGA8ZGl2PgogICAgICAgICAgICAgICAgICAgICBCb2J3aGl0ZSBDb3VudGVyCiAgICAgICAgICAgICAgICAgPC9kaXY+YCwKICAgICAgICAgICAgICAgIHsic3RpY2t5IjogdHJ1ZX0KICAgICAgICAgICAgKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyX2JmZjhmZWQ4YWJjMjRmZGI5MDdiZGJlMjkzZmY0Nzk0ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI2ODAyNjQ0Njk5Mzc2LCAtNzMuOTgzNDQ0MDc1MjM2NDVdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXJrZXJfY2x1c3Rlcl83YjI0YjgzN2I2NDA0OGFlOWQ5ZjEyMzFkYmJhMDQ3Yyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fMGVmMDlkNjAxNmQ2NDVmMzhiZDVlOWViZDA3ZmJhZDMgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogIm9rLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogInJlZCIsICJwcmVmaXgiOiAiZ2x5cGhpY29uIn0KICAgICAgICAgICAgKTsKICAgICAgICAgICAgbWFya2VyX2JmZjhmZWQ4YWJjMjRmZGI5MDdiZGJlMjkzZmY0Nzk0LnNldEljb24oaWNvbl8wZWYwOWQ2MDE2ZDY0NWYzOGJkNWU5ZWJkMDdmYmFkMyk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYjhlMDg5NDAxYTM4NDg0MTlhYzJjNmY2MmRhNDgxZTMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzk5OTFhYTBmNTllMDQyYmRiMDJiMmFiMjNmNDI0YmZhID0gJChgPGRpdiBpZD0iaHRtbF85OTkxYWEwZjU5ZTA0MmJkYjAyYjJhYjIzZjQyNGJmYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRkcmVzczoxMzAgU2FpbnQgTWFya3MgUGwsIFJhdGluZzo5LjIsIFByaWNlIFRpZXI6NCwvbiBBdm9pZCBUaW1lOjU6MDAgUE3igJMxMTowMCBQTTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9iOGUwODk0MDFhMzg0ODQxOWFjMmM2ZjYyZGE0ODFlMy5zZXRDb250ZW50KGh0bWxfOTk5MWFhMGY1OWUwNDJiZGIwMmIyYWIyM2Y0MjRiZmEpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfYmZmOGZlZDhhYmMyNGZkYjkwN2JkYmUyOTNmZjQ3OTQuYmluZFBvcHVwKHBvcHVwX2I4ZTA4OTQwMWEzODQ4NDE5YWMyYzZmNjJkYTQ4MWUzKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICBtYXJrZXJfYmZmOGZlZDhhYmMyNGZkYjkwN2JkYmUyOTNmZjQ3OTQuYmluZFRvb2x0aXAoCiAgICAgICAgICAgICAgICBgPGRpdj4KICAgICAgICAgICAgICAgICAgICAgQm9id2hpdGUgQ291bnRlcgogICAgICAgICAgICAgICAgIDwvZGl2PmAsCiAgICAgICAgICAgICAgICB7InN0aWNreSI6IHRydWV9CiAgICAgICAgICAgICk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl8xNWUwMmE5ODA2NDk0MzlhOWRhOGM0ZjZhZDViYjc4NyA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyMzcxNTQwMTI0NDExLCAtNzMuOTc5MTIwOTgyMjgwNjldLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXJrZXJfY2x1c3Rlcl83YjI0YjgzN2I2NDA0OGFlOWQ5ZjEyMzFkYmJhMDQ3Yyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGljb25fNjM5NGI3OGE3YTQ0NDA2OTllYmM1MzFiZDc3NTZjNjYgPSBMLkF3ZXNvbWVNYXJrZXJzLmljb24oCiAgICAgICAgICAgICAgICB7ImV4dHJhQ2xhc3NlcyI6ICJmYS1yb3RhdGUtMCIsICJpY29uIjogIm9rLXNpZ24iLCAiaWNvbkNvbG9yIjogIndoaXRlIiwgIm1hcmtlckNvbG9yIjogImdyZWVuIiwgInByZWZpeCI6ICJnbHlwaGljb24ifQogICAgICAgICAgICApOwogICAgICAgICAgICBtYXJrZXJfMTVlMDJhOTgwNjQ5NDM5YTlkYThjNGY2YWQ1YmI3ODcuc2V0SWNvbihpY29uXzYzOTRiNzhhN2E0NDQwNjk5ZWJjNTMxYmQ3NzU2YzY2KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF83YWM1ZDg0MTQzN2E0N2JhODlmZDc2OTQ0OGIwYzgxMSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZmJlNzBmZTNmMzFmNGUzZTk4OTM3OTE2NWYwMWFjOGQgPSAkKGA8ZGl2IGlkPSJodG1sX2ZiZTcwZmUzZjMxZjRlM2U5ODkzNzkxNjVmMDFhYzhkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BZGRyZXNzOjk0IEF2ZW51ZSBDLCBSYXRpbmc6OS4yLCBQcmljZSBUaWVyOjIsL24gQXZvaWQgVGltZTpOb29u4oCTMTE6MDAgUE08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfN2FjNWQ4NDE0MzdhNDdiYTg5ZmQ3Njk0NDhiMGM4MTEuc2V0Q29udGVudChodG1sX2ZiZTcwZmUzZjMxZjRlM2U5ODkzNzkxNjVmMDFhYzhkKTsKICAgICAgICAKCiAgICAgICAgbWFya2VyXzE1ZTAyYTk4MDY0OTQzOWE5ZGE4YzRmNmFkNWJiNzg3LmJpbmRQb3B1cChwb3B1cF83YWM1ZDg0MTQzN2E0N2JhODlmZDc2OTQ0OGIwYzgxMSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgbWFya2VyXzE1ZTAyYTk4MDY0OTQzOWE5ZGE4YzRmNmFkNWJiNzg3LmJpbmRUb29sdGlwKAogICAgICAgICAgICAgICAgYDxkaXY+CiAgICAgICAgICAgICAgICAgICAgIEJvYndoaXRlIENvdW50ZXIKICAgICAgICAgICAgICAgICA8L2Rpdj5gLAogICAgICAgICAgICAgICAgeyJzdGlja3kiOiB0cnVlfQogICAgICAgICAgICApOwogICAgICAgIAo8L3NjcmlwdD4= onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
# Finally,we have:
# 1. A intuitive map with top 20 rating restaurants around Chinatown in NY
# 2. If there are more than two restaurants nearby one location, there will be clucters button to click
# 3. We can mouseover to those locations to see their names
# 4. We can choose different price tiers by looking at their colors, green means cheap, red means a bit expensive, black means we dont have price info of these locations
# 5. By clicking those locations we can see details of address,rating,price tier and popular time frame to avoid queuing
```
