#Carol Pan
#SoftDev1 pd7
#HW04--Fill Up Yer Flask
#2017-09-25

from flask import Flask

app = Flask(__name__) #class as been named

@app.route("/")

def hello_world():
    return "Would you like to look at homework or projects?"

if __name__ == "__main__":
    app.debug = True
    app.run()

# this is the most colorful code I've ever written
