from flask import Flask
from flask_cors import CORS, cross_origin

server = Flask(__name__)
CORS(server)