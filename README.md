# HerokuFlaskHelloWorld
A Python Flask App with the appropriate structure to deploy to Heroku. Navigating to the URL /hi will display a Hello World message.

## Deploying a Python Web Application for Free and with Minimal Frustration

Deployment is an area that many developers find challenging. Deploying an application to the web can get complicated real fast, even for experienced developers. The goal of this repository is to show one fast, free, and relatively painless method to deploy a Python web application. Beginners may appreciate that this method doesn't require extensive Linux knowledge and experienced developers may appreciate adding a deployment method to their toolbelt that takes less than 15 minutes to get a website up and running.

We'll deploy a basic Flask Web Application to a Platform as a Service (PaaS) known as Heroku and we'll be staying within the free-tier of Heroku's services. 

Hopefully once you see how pain-free deployments can be you'll write more code to share with the world.   


## Requirements
1. Create a free Heroku account
2. Git
3. Heroku client 

### 1. Create a free Heroku account
Create a Heroku account here https://signup.heroku.com/.

### 2. Git
Directions to install Git can found here: https://github.com/git-guides/install-git.

If you're not sure if you alredy have git installed and you're on a Mac or Linux, open up a terminal and type:

```
git version
```

If you have git installed on Mac or Linux you'll see a response like:


```
git version 2.32.0
```

Your specific git version number may be slightly different.

Configuring Git:
```
git config --global user.name "your_name"
git config --global user.email "your_email_address"
```

### 3. Install the Heroku client for MacOS, Windows, or Linux
Directions to install the Heroku client can be found here: https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#set-up. Windows users: the Heroku documentation is a bit sparse for Windows. You may have better success using Windows Subsystem Linux https://docs.microsoft.com/en-us/windows/wsl/about. This article https://dev.to/wrightdotclick/heroku-cli-on-wsl-26fp may help setup Heroku on Windows Subsystem Linux. 

After you install the Heroku client, login to your account by typing:
```
heroku login
```
You will only need to type `heroku login` the first time you use the Heroku client.

## Building Our App
Go to the directory you would like to start your project, for example:
```
cd heroku_projects
```
create a virtual environment:
```
python3 -m venv venv
```
Activate the virtual environment:
```
source venv/bin/activate
```
Go to the new virutal environment:
```
cd venv
```
Clone the Git Hub Repository:
```
git clone https://github.com/jeffthomasweb/HerokuFlaskHelloWorld.git
```
Go to the HerokuFlaskHelloWorld directory:
```
cd HerokuFlaskHelloWorld
```
Install Flask, Gunicorn, and (optional) pytest:
```
pip install Flask
pip install gunicorn
pip install pytest
```
If we type `ls` in the terminal we should see the following files listed:
```
app.py   Procfile     README.md         runtime.txt  test_hello.py
LICENSE  __pycache__  requirements.txt  templates
```
`app.py`, `Procfile`, `runtime.txt`, and `requirements.txt` are 4 important files I'll discuss below.

### app.py
app.py is where we'll be placing most of our application's code.

### Procfile
Procfile (just Procfile, no file extension) let's Heroku know how we would like to setup our app. Our Procfile looks like:
```
web: gunicorn app:app --log-file -
```
In our Procfile we're letting Heroku know that we're setting up a web application using Gunicorn as the Python Web Server Gateway Interface HTTP Server, our application's code is in the file `app.py`, and we're seting up logging. 

The Procfile for Windows may be a bit different. The Heroku doucmentation is unfortunately a bit sparse on this topic. If you're on Windows it may be easiest to use Windows Subsystem Linux https://docs.microsoft.com/en-us/windows/wsl/about. Please see https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#define-a-procfile for more information about the Heroku Procfile on Windows. 

### runtime.txt
The `runtime.txt` file tells Heroku what Python version we're using for our app. Our `runtime.txt` file looks like this:
```
python-3.9.7
```
To find out what Python version you're using, type:
```
python --version
```
### requirements.txt
The `requirements.txt` file let's Heroku know what libraries we need for our app. To automatically set the requirements, type:
```
pip freeze > requirements.txt
```
Our `requirements.txt` file looks like the following if we've `pip install Flask`,`pip install gunicorn`, and `pip install pytest`:
```
attrs==21.2.0
click==8.0.3
Flask==2.0.2
gunicorn==20.1.0
iniconfig==1.1.1
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
packaging==21.2
pluggy==1.0.0
py==1.11.0
pyparsing==2.4.7
pytest==6.2.5
toml==0.10.2
Werkzeug==2.0.2
``` 

To see our Flask app run locally before deploying to Heroku, type:

```
flask run
```
and open http://127.0.0.1:5000/ in a browser. Hold the Ctrl c keys when you'd like to stop the test web server.

### Deploying to Heroku
To create a new Heroku project that we would like to deploy, type:

```
heroku create
```
Check that our git branch is "main" instead of "master" by typing:

```
git status
```
If our git branch is called master, use the following to change the name to main:

```
git branch -m master main
```

The command `git status` will also let us know if any files have changed that we need to commit to git. To add these files, type:

```
git add <file name here>
```

Run `git status` again to make sure we haven't missed any files.

When ready, commit our changes to git by typing:

```
git commit -m "commit message here"
```

To push these changes to Heroku, type:

```
git push heroku main
```

You'll see your app being deployed in the termainl and will see a message like the one below when it's deployed:

```
remote: Verifying deploy... done.
```
The website address will be displayed in the termainl and look something like https://peaceful-mountain-10820.herokuapp.com/.

If you encounter errors durirng deployment or if you receive an error when you enter the website URL into your browser, check the log for errors by typing:
```
heroku logs --tail
```

Heroku documentation links: 
   - https://www.heroku.com/python 
   - https://devcenter.heroku.com/articles/getting-started-with-python
