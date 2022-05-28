from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from flask import Flask, redirect, url_for, request
app = Flask(__name__, static_folder='my-app/build', static_url_path='')
CORS(app)

@app.route('/api', methods=['GET'])
@cross_origin()
def index():
    return {
        "tutorial": "Flask React Hero"
    }

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

names = []
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % names

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      names.append(user)
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)

