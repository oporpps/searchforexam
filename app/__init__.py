from flask import Flask
import os

app = Flask(__name__)
STORE_PATH = os.getcwd() + "\\app\\store\\"

# load router
from app import routes