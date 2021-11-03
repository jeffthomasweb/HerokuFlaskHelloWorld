from flask import Flask

app = Flask(__name__)


#Anyone that visits our site with the URL ending in /hi will see an HTTP response of Hello RocPy with emojis.
@app.route("/hi")
def helloroc():
    return "Hello RocPy 🪨🐍!"

#It's a good practice to include following.
if __name__ == '__main__':
    app.run()
