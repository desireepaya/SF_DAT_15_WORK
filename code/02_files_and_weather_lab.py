'''
Lab: Reading and Writing Files in Python
'''

'''
PART 1:
Read in drinks.csv
Store the header in a list called 'header'
Store the data in a list of lists called 'data'
Hint: you've already seen this code!
'''
import csv
with open('../data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

'''
PART 2:
Isolate the beer_servings column in a list of integers called 'beers'
Hint: you can use a list comprehension to do this in one line
Expected output:
    beers == [0, 89, ..., 32, 64]
    len(beers) == 193
'''
beers= []
for row in data:
    beers.append(row[1])
beers = map(int,beers)

beers2 = map(lambda row:int(row[1]), data)
# lambda defines a function inline

'''
PART 3:
Create separate lists of NA and EU beer servings: 'NA_beers', 'EU_beers'
Hint: you can use a list comprehension with a condition
Expected output:
    NA_beers == [102, 122, ..., 197, 249]
    len(NA_beers) == 23
    EU_beers == [89, 245, ..., 206, 219]
    len(EU_beers) == 45
'''
NA_beers = []
EU_beers = []
for row in data:
    if row[5] == 'NA':
        NA_beers.append(int(row[1]))
    elif row[5] == 'EU':
        EU_beers.append(int(row[1]))

NA_beers2 = filter(lambda row:row[5] == 'NA', data)

'''
PART 4:
Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
Hint: don't forget about data types!
Expected output:
    NA_avg == 145.43
    EU_avg == 193.78
'''
NA_avg = '{:.2f}'.format(float(sum(NA_beers)) / len(NA_beers))
print NA_avg
EU_avg = '{:.2f}'.format(float(sum(EU_beers)) / len(EU_beers))
print EU_avg

'''
PART 5:
Write a CSV file called 'avg_beer.csv' with two columns and three rows.
The first row is the column headers: 'continent', 'avg_beer'
The second and third rows contain the NA and EU values.
Hint: think about what data structure will make this easy
Expected output (in the actual file):
    continent,avg_beer
    NA,145.43
    EU,193.78
'''
output = [['continent', 'avg_beer'],['NA',NA_avg],['EU',EU_avg]]
with open('avg_beer.csv', 'wb') as f:
    csv.writer(f).writerows(output)

'''
Part 6:
Use the requests module to pull in weather data for any city
Hint: you can use Istanbul from the other code file but you can search
for cities at http://openweathermap.org/find

Create a dates list that stores the date of each datapoint as well as
temperature and humidity

You've already seen this code!
'''
import requests
api_endpoint = 'http://api.openweathermap.org/data/2.5/forecast/city'
params = {}
params['id'] = '5856195'
params['units'] = 'imperial'
params['APPID'] = '80575a3090bddc3ce9f363d40cee36c2'

response = requests.get(api_endpoint, params = params)
weather = response.json()
weather

weather.keys()
weather_data = weather['list']

dates = [data_point['dt'] for data_point in weather_data]

from datetime import datetime
dates = [datetime.fromtimestamp(epoch) for epoch in dates]

temperatures = [data_point['main']['temp'] for data_point in weather_data]
humidity = [data_point['main']['humidity'] for data_point in weather_data]
dates_list = []
for i in range(len(dates)):
    dates_list.append([dates[i],temperatures[i],humidity[i]])

dates_list1 = [([dates[i],temperatures[i],humidity[i]]) for i in range(len(dates))]


'''
Part 7
Create a list of the pressure measurements and plot it against dates
'''
pressure = [data_point['main']['pressure'] for data_point in weather_data]
import matplotlib.pyplot as plt
plt.plot(dates_list, pressure)
plt.plot(dates,temperatures,humidity)

plt.xlabel('Date')
plt.ylabel('Pressure')
plt.title('Pressure over time -- Honolulu')
locs, labels = plt.xticks()
plt.setp(labels, rotation=70)
plt.plot(dates,pressure)

'''
Part 8
Make a scatter plot plotting pressure against temperature and humidity
'''
# normalize pressure, humidity, temperatures
pressure_norm = [float(p) / max(pressure) for p in pressure]
humidity_norm = [float(h) / max(humidity) for h in humidity]
temp_norm = [float(t) / max(temperatures )for t in temperatures]
plt.xlabel('Date')
plt.xlim((dates[0]),(dates[-1]))
ocs, labels = plt.xticks()
plt.setp(labels, rotation=70)
plt.title('Pressure vs. Temperature & Humidity -- Honolulu')
plt.legend()
plt.scatter(dates,pressure_norm, label='Pressure')
plt.plot(dates,humidity_norm, label='Humidity')
plt.plot(dates,temp_norm, label='Temperature')

'''
BONUS:
Learn csv.DictReader() and use it to redo Parts 1, 2, and 3.
'''