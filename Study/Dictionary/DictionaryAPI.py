from flask import Flask, jsonify, request
import json
from difflib import get_close_matches

app = Flask(__name__)

data = json.load(open("data.json"))

def find_meaning_response(word):
    word = word.lower()

    if word in data:
        return {word : data[word]}
    
    close_matches = get_close_matches(word, data)
    
    if len(close_matches) > 0:
        return {'message' : 'Word not found but the closest match and its meaning is provided', close_matches[0]:data[close_matches[0]]}
    else:
        return {'message' : 'Word not found and no closest match present'}


@app.route("/getMeaning", methods = ['POST'])
def getMeaning():
	input_data = request.get_json()
	if 'word' in input_data:
		return jsonify(find_meaning_response(input_data['word']))
	return jsonify({'Message':'Bad Request, word key not found'})

	
app.run(port=5000)