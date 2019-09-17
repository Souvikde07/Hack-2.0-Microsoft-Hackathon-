from sklearn.externals import joblib 
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)
scaler = MinMaxScaler(feature_range=(0,1))
a = pd.read_csv('data.csv')
a = a.values
s = scaler.fit_transform(a)
model = joblib.load('model1.pkl')

def f(i):
	i = np.array([int(i)])
	i = i.reshape(-1,1)
	i = scaler.transform(i)
	i = np.reshape(i,(i.shape[0],i.shape[1],1))
	c = model.predict(i)
	c = scaler.inverse_transform(c)
	return c

@app.route('/get_req', methods=['POST'])
def get_req():
   val = request.form['value']
   val = f(val)[0][0]
   d = {'answer':str(val)}
   print(d)
   s = "<h1>Predicted Close value : "+str(val)+"</h1>"
   return s

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('1.html', title='Sign In', form=form)

@app.route('/test')
def t():
	return '<h1>Hello</h1>'

if __name__=='__main__':
	app.run(host='0.0.0.0', port=80)
