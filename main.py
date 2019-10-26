from flask import Flask, render_template, send_file


app=Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/points/')
def return_files_tut():
	try:
		return send_file('json/geo.json', attachment_filename='geo.json')
	except Exception as e:
		return str(e)

if __name__=='__main__':
    app.run(debug=True,threaded=True)

