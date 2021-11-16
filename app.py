from flask import Flask

app = Flask(__name__)

#Anyone that visits our main site will see a general Hello World message.
@app.route("/")
def hello():
    return "Hello World!"

#Anyone that visits our site at /hi will see a Hello RocPy message.
@app.route("/hi")
def helloroc():
    return "Hello RocPy 🪨🐍!"

#It's a good practice to include following.
if __name__ == '__main__':
    app.run()
