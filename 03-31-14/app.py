from flask import Flask, render_template, request, redirect
import random, string
import pymongo

client = pymongo.MongoClient()
db = client.test

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten')
def shorten():

    #this extracts the URL parameter.
    if 'url' not in request.args:
        return 'put a damn parameter bro.'
    url = request.args['url']

    # generate a random string as the short version of this URL.

    random_str = ""
    for i in range(0, 6):
        random_str += random.choice(string.ascii_uppercase)

    #with open('urls', 'a') as fh:
    #    fh.write(random_str + '|' + url + "\n")

    db.test.insert({'code': random_str, 'website': url})

    return 'your shortened url is http://localhost:9999/go?code=' + random_str

@app.route('/go')
def go():
    code = request.args['code']

    for entry in db.test.find({'code': code}):
        return redirect(entry['website'])

    return 'your url was not found'

app.run(port=9999, debug=True)
