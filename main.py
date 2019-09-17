from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/Hello')
def hello_world():
	d = {'Name':'Pranjul','Number':2}
	return jsonify(d)

if __name__=='__main__':
	app.run()