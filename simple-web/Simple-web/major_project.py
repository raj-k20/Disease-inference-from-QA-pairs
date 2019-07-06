from flask import *
from mark3 import *
app = Flask(__name__)

@app.route('/enterQuery/')
def enterquery():
	return render_template('majorHome.html')

@app.route('/handle/',methods=['GET','POST'])
def handle():
	if request.method == 'POST':
		result=request.form
		query=result['searchQuery']
		res = classify(query)
		try:
			resu= res[0][0]
		except:
			resu="Please Try Again With Another Query"
		return redirect(url_for('finalAnswer',result=resu))

@app.route('/result/',methods=['GET'])
def finalAnswer():
	result=request.args.get('result')
	return render_template('resultFinal.html',result=result)
if __name__=='__main__':
	app.run('0.0.0.0',1465)
