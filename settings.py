import os


if (os.environ.get('FLASK_ENV') == 'development'
        or os.environ.get('FLASK_ENV') == 'dev'):
    MONGO_URL = 'localhost'
    MONGO_PORT = str(27017)
    MONGO_URI = 'mongodb://' + MONGO_URL + ':' + MONGO_PORT + '/'
    DEBUG = True
    SECRET_KEY = 'secret'
else:
    MONGO_URL = 'mongodb'
    MONGO_PORT = str(27017)
    MONGO_URI = 'mongodb://' + MONGO_URL + ':' + MONGO_PORT + '/'
    DEBUG = True
    SECRET_KEY = 'secret'
