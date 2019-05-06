from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    hello = '<h1>Hello World from BeautifulCode Meetup!<br></h1>'
    return  hello

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
