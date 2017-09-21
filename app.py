#Carol Pan
#SoftDev1 pd7
#HW04--Fill Up Yer Flask
#2017-09-25

from flask import Flask

app = Flask(__name__) #class as been named

@app.route("/")
def hello_world():
    return "Would you like to look at homework or projects?"

@app.route("/static")
def radio_silence():
    return "It seems like I lost my radio..."

@app.route("/homework")
def tarea():
    return "https://docs.google.com/a/stuy.edu/document/d/e/2PACX-1vQ9UQ9bgB4J3wYkqzNDU7CP17mNzMFRm0nQQzPomODClofKCpQnsD4yXktev46KimMt8AySqBEbdFWU/pub"

@app.route("/projects")
def mission():
    return "t---0oo much ---z-- static!"

if __name__ == "__main__":
    app.debug = True
    app.run()


# this is the most colorful code I've ever written
