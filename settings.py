import os

# This settings for Heroku
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.urandom(32)
SQLALCHEMY_TRACK_MODIFICATIONS = False

APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')

# This settings for AWS
# DB_USERNAME = 'Your_Username'
# DB_PASSWORD = 'Your_Password'
# DB_DATABASE_NAME = 'Your_DB_name'
# DB_HOST = 'Your_DB_Host'
# APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# DEBUG = True
# SECRET_KEY = '<$üP3rPazzWø£DsGyL>'
# SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE_NAME}"
# STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')

# Options
# SERVER_NAME = 'localhost:5000'
# RECAPTCHA_PUBLIC_KEY = '<Your own keys from Google>'
# RECAPTCHA_PRIVATE_KEY = '<You can get these keys at https://www.google.com/recaptcha/admin>'
# RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}


