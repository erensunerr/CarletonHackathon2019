#Version = 0.01
from flask import Flask

app = Flask(__name__)

from app import routes
