#[CONFIG - SETTINGS]

from os import getcwd

class BaseConfig():
    LOGGING:bool = False
    DEBUG:bool = False

class DevConfig(BaseConfig):
    DEBUG:bool = True
    DB_URI:str = 'sqlite:///koda.dev.db'
    SECRET:str = '9bfbdce584969ef045b402d8db75ee33e433e2eb347d0ee5d3aac853b63d71cf'
    UPLOAD_FOLDER:str = getcwd() + '/koda/static/photos/dev'

class LiveConfig(BaseConfig):
    LOGGING:bool = True
    DB_URI:str = 'sqlite:///koda.live.db'
    SECRET:str = '49900237b92a71599a343eb029b16728035159c175a090e9007b3622adfb76b1'
    UPLOAD_FOLDER:str = getcwd() + '/koda/static/photos/live'