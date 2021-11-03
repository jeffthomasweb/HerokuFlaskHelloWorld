from flask import Flask, jsonify
from flask.templating import render_template #Use flask.templating and render_template to display site as a html file
import feedparser #To Parse RSS Feeds
import re #Python Regular Expression Library

app = Flask(__name__)

#Parse NPR RSS Feed data using feedparser and f strings. Use regular expression to
#remove <em> and </em> tags that the feedparser library is unable to remove.
#For example below b is the story title and story summary from the RSS feed.
#b1 equals the story title and story summary with any <em> tags removed.
#b2 equals the story title and story summary with any </em> tags removed.

a = feedparser.parse("https://feeds.npr.org/1001/rss.xml")

b = f"{a.entries[0].title + '. ' + a.entries[0].summary}"
b1 = re.sub('<em>', '',b)
b2 = re.sub('</em>', '',b1)

c = f"{a.entries[1].title + '. ' + a.entries[1].summary}"
c1 = re.sub('<em>', '',c)
c2 = re.sub('</em>', '',c1)

d = f"{a.entries[2].title + '. ' + a.entries[2].summary}"
d1 = re.sub('<em>', '',d)
d2 = re.sub('</em>', '',d1)

e = f"{a.entries[3].title + '. ' + a.entries[3].summary}"
e1 = re.sub('<em>', '',e)
e2 = re.sub('</em>', '',e1)

f = f"{a.entries[4].title + '. ' + a.entries[4].summary}"
f1 = re.sub('<em>', '',f)
f2 = re.sub('</em>', '',f1)

g = f"{a.entries[5].title + '. ' + a.entries[5].summary}"
g1 = re.sub('<em>', '',g)
g2 = re.sub('</em>', '',g1)

h = f"{a.entries[6].title + '. ' + a.entries[6].summary}"
h1 = re.sub('<em>', '',h)
h2 = re.sub('</em>', '',h1)

i = f"{a.entries[7].title + '. ' + a.entries[7].summary}"
i1 = re.sub('<em>', '',i)
i2 = re.sub('</em>', '',i1)

j = f"{a.entries[8].title + '. ' + a.entries[8].summary}"
j1 = re.sub('<em>', '',j)
j2 = re.sub('</em>', '',j1)

k = f"{a.entries[9].title + '. ' + a.entries[9].summary}"
k1 = re.sub('<em>', '',k)
k2 = re.sub('</em>', '',k1)

l = f"{a.entries[10].title + '. ' + a.entries[10].summary}"
l1 = re.sub('<em>', '',l)
l2 = re.sub('</em>', '',l1)

m = f"{a.entries[11].title + '. ' + a.entries[11].summary}"
m1 = re.sub('<em>', '',m)
m2 = re.sub('</em>', '',m1)

n = f"{a.entries[12].title + '. ' + a.entries[12].summary}"
n1 = re.sub('<em>', '',n)
n2 = re.sub('</em>', '',n1)

o = f"{a.entries[13].title + '. ' + a.entries[13].summary}"
o1 = re.sub('<em>', '',o)
o2 = re.sub('</em>', '',o1)

p = f"{a.entries[14].title + '. ' + a.entries[14].summary}"
p1 = re.sub('<em>', '',p)
p2 = re.sub('</em>', '',p1)

#A list of the all the parsed stories from the RSS feed.
storieslist= [b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2,m2,n2,o2,p2]


#Anyone that visits our site with the URL ending in /hi will see an HTTP response of Hello RocPy with emojis.
@app.route("/hi")
def helloroc():
    return "Hello RocPy 🪨🐍!"

#A very basic API at the /news URL of the parsed stories from the RSS feed. Use jsonify to have the
#result as JSON instead of text/html.
@app.route("/news")
def news():
    return jsonify(storieslist)

#Visiting the main site URL will show the stories as a normal HTML site.
@app.route("/")
def rss():
    return render_template("index.html", storieslist=storieslist)

#It's a good practice to include following.
if __name__ == '__main__':
    app.run()
