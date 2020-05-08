
from flask import Flask


app = Flask(__name__)


app.config['SECRET_KEY'] = 'beb37ebec90537a85ac51a13567e276e'

from app import views