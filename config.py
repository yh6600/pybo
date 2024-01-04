import os

BASE_DIR = os.path.dirname(__file__)
print('==>',BASE_DIR)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
print('==>>>',SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

