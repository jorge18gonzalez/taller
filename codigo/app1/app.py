from flask import Flask
from routes import *


app = Flask(__name__)


app.add_url_rule(routes["register"], view_func=routes["register_controllers"])
app.add_url_rule(routes["login"], view_func=routes["login_controllers"])
app.add_url_rule(routes["phone"], view_func=routes["Phone_controllers"])

