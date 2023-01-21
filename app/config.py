import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'idk'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv('MAIL_SERVER') or 'smtp.sendgrid.net'
    MAIL_PORT = int(os.getenv('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS') is not None or True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') or 'apikey'
    MAIL_PASSWORD = os.getenv('SENDGRID_API_KEY')
    ADMINS = [os.getenv('MAIL_DEFAULT_SENDER')]
    POSTS_PER_PAGE = 10
    LANGUAGES = ['en', 'fr']

