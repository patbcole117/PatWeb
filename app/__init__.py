from flask import Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

from app import routes