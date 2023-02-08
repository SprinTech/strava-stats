import secrets


class Config:
    """Base config"""
    SECRET_KEY = secrets.token_hex(16)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    """Development config"""
    DEBUG = True
    TESTING = True
    FLASK_ENV = 'development'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
