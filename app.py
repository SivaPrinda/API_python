from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def index():
 return "hello my app"

@app.route("/api/book", methods=['GET'])
def apiBook():
    book=[
        {
            'id':1,
            'titre' : 'un titre',
        },
        {
            'id':2,
            'titre': 'un autre titre random',
        }
    ]
    return json.dumps(book)

@app.route("/api/book/<id>", methods=['GET'])
def book(id):
    book=[
    	{
    		'id':1,
    		'titre' : 'un titre',
    	},
    	{
    		'id':2,
    		'titre': 'un autre titre random',
    	}
    ]
    if id in book:
        return json.dumps(book[id])

if __name__ == '__main__':
    app.run(debug=True)