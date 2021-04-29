from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello():
    return "Welcome to Openshift Application Deployment"


if __name__ == "__main__":
   application.run("0.0.0.0")
