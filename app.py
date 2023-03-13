from flask import Flask
fapp = Flask(__name__)

@fapp.route('/')
def hello_world():
    return 'GreyMatters'


if __name__ == "__main__":
    fapp.run()