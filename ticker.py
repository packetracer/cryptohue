import datetime
import requests
from time import sleep
import requests
import numpy as np
import sys

z = np.arange(.5,.692,.005)

coin = sys.argv[1]

def pullCHCdata():
	data  = requests.get('https://api.coinmarketcap.com/v1/ticker/'+coin+'/')
	data = data.json()
	data = str(data[0])
	data = data.replace("u'",'')
	data = data.replace("'",'')
	data = data.strip(",")
	data = data.split(',')
	return data

def getCHCPrice(data):
	price = data[1]
	price = price.split(': ')
	return price[1]

def getCHCChange(data):
	pc = data[8]
	pc = pc.split(': ')
	return pc[1]

curData = pullCHCdata()
curPrice = getCHCPrice(curData)
curPC = getCHCChange(curData)
print datetime.datetime.now()
print "Coin: " + coin
print "Price: $" + curPrice
print "Change: " + curPC + '%'

x1 = np.arange(.16001,.17,.0001)

x2 = np.arange(.63002,.65,.0002)
i = 0
y1=[]
y2=[]
for z in x1:
        y1.append((32.5 * z) - 4.825)

for z in x2:
        y2.append((.30208 * z) + 0.098958)
pairs = zip(x1,y1)
pairs2 = zip(x2,y2)


valPC = float(curPC)
print "Value of PC is: "+ str(int(valPC))


if valPC > 0:
	gain = int(valPC)
	stripped = str(pairs[gain])
	stripped = stripped.strip(')')
	stripped = stripped.strip('(')
	
	if gain < 1:
		gain = 0
	if gain > 99:
		gain = 38
	payload = '{"xy":[' + stripped +']}'
	r = requests.put("http://192.168.1.227/api/0qhTPxNaWLmya5z-1KnqURFKJNQwziy8QZNvnrLW/lights/3/state", data=payload)
if valPC < 0:
	loss = int(valPC)
	stripped = str(pairs2[loss])
        stripped = stripped.strip(')')
        stripped = stripped.strip('(')

	if loss > -1:
		loss = 0
	if loss < -99:
		loss = 99
	payload = '{"xy":[' + stripped +']}'
        r = requests.put("http://192.168.1.227/api/0qhTPxNaWLmya5z-1KnqURFKJNQwziy8QZNvnrLW/lights/3/state", data=payload)

