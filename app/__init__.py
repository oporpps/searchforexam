from flask import Flask


app = Flask(__name__)

# load router
from app import routes