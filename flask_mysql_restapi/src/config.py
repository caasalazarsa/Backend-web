class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'testuser'
    MYSQL_PASSWORD = '123456789'
    MYSQL_DB = 'api_flask'


config = {
    'development': DevelopmentConfig
}
