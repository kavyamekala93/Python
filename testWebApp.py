# "pip" is a package manager for python like nuget for dotnet
# to install flask: pip install flask
# PyPi- Python Package Index


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__== "__main__":
    app.run()
