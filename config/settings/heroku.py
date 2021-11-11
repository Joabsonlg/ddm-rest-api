import environ
from config.settings.base import *

env = environ.Env()
DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY', default='secret')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
DATABASES = {
    'default': env.db(),
}