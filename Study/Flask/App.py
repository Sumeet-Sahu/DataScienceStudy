from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello')
def hello():
	return 'Hello World!'
	
stores = [
	{
		"name" : "D-Stores",
		"items": [
			{
				'name' : "Maggie",
				'Price': 100
			}
		] 
	}
]

@app.route("/stores")
def getStores():
	return jsonify(stores) 

@app.route("/storesWithDictionaryJSON")
def getStoresAsDictionaryJSON():
	return jsonify({'Stores':stores}) 
	
@app.route('/store/<string:name>')
def getStore(name):
	for store in stores:
		if store['name']==name:
			return jsonify(store)
	return jsonify({'Message':'Store Not found'})	

@app.route('/store/<string:name>/items')
def getStoreItems(name):
	for store in stores:
		if store['name']==name:
			return jsonify({'items':store['items']})
	return jsonify({'Message':'Store Not found'})
	
@app.route('/store', methods = ['POST'])
def addStore():
	request_dict = request.get_json()
	if 'items' in request_dict.keys():
		items = request_dict['items']
	else:
		items = []
	new_store = {'name':request_dict['name'], 'items':items}
	for store in stores:
		if store['name'] == new_store['name']:
			return jsonify({"Message":" Store is already present"})
	stores.append(new_store)
	return jsonify({'Message':'Store Added!!!'})













	

	
app.run(port=5000)