from flask import Flask
from app.config import Config
# Here __name__ is predefined variable; which is set to name of the module, which is app here.
app = Flask(__name__)
app.config.from_object(Config)


from app import routes
