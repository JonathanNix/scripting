import json
import urllib.request
import random

def addToItemList(jdict, items):
	for i in jdict['items']:
		if not i['name'] in items.keys():
			if 'salePrice' in i.keys() and 'name' in i.keys():
				price = float("{0:.2f}".format(i['salePrice']))
				items[i['name']] = price

def createItemList():
	request = urllib.request.urlopen('http://api.walmartlabs.com/v1/taxonomy?format=json&apiKey=tkbnu8astb9xxtn2ux9vw73b')
	response = request.read()
	jdict = json.loads(response.decode())
	categories = []
	items = {}

	for i in jdict['categories']:
		categories.append(i['id'])

	nums = random.sample(range(0,len(categories)), 3)

	reqStr1 = 'http://api.walmartlabs.com/v1/paginated/items?format=json&&category='+categories[nums[0]]+'&apiKey=tkbnu8astb9xxtn2ux9vw73b'
	reqStr2 = 'http://api.walmartlabs.com/v1/paginated/items?format=json&&category='+categories[nums[1]]+'&apiKey=tkbnu8astb9xxtn2ux9vw73b'
	reqStr3 = 'http://api.walmartlabs.com/v1/paginated/items?format=json&&category='+categories[nums[2]]+'&apiKey=tkbnu8astb9xxtn2ux9vw73b'
	request = urllib.request.urlopen(reqStr1)
	response = request.read()
	jdict = json.loads(response.decode())
	addToItemList(jdict, items)

	request = urllib.request.urlopen(reqStr2)
	response = request.read()
	jdict = json.loads(response.decode())
	addToItemList(jdict, items)

	request = urllib.request.urlopen(reqStr3)
	response = request.read()
	jdict = json.loads(response.decode())
	addToItemList(jdict, items)

	return items