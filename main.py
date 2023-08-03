from flask import Flask, render_template, jsonify,request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)
limiter = Limiter(key_func=get_remote_address, app=app, default_limits=["100 per second"])

counter = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['GET', 'POST'])
@limiter.limit("70 per second")
def click():
    global counter
    if request.method == 'POST':
        counter += 1
    return jsonify(counter=counter)

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0",port=80)