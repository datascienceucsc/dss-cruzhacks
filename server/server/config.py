import os
import json

class BaseConfig:
    SECRET_KEY = None

class DevelopmentConfig(BaseConfig):
    FLASK_ENV="development"

class ProductionConfig(BaseConfig):
    FLASK_ENV="production"


