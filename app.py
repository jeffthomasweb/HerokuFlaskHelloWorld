from flask import Flask

app = Flask(__name__)

#Anyone that visits our main site will see a general Hello World message.
@app.route("/")
def hello():
    return "Hello World!"

<<<<<<< HEAD
#Anyone that visits our site with the URL ending in /hi will see an HTTP response of Hello RocPy with emojis.
=======
#Anyone that visits our site at /hi will see a Hello RocPy message.
>>>>>>> 2b95d937bc9beb38cb4c8fa35db97269c31c815f
@app.route("/hi")
def helloroc():
    return "Hello RocPy 🪨🐍!"

#It's a good practice to include following.
if __name__ == '__main__':
    app.run()
