class Config(object):
  DEBUG=False
  TESTING=False
  SECRET_KEY="ertyudfghj"
  DB_NAME="production-db"
  DB_USERNAME="root"
  DB_PASSWORD="example"
  UPLOADS="/home/username/app/app/static/images/uploads"
  SESSION_COOKIE_SECURE=True
class ProductionConfig(Config):
  pass
class DevelopmentConfig(Config):
  DEBUG=True
  DB_NAME="development-db"
  DB_USERNAME="root"
  DB_PASSWORD="example"
  UPLOADS="/home/username/app/app/static/images/uploads"
  SESSION_COOKIE_SECURE=False
  CLIENT_IMAGES="/content/app/static/client/img"
  CLIENT_CSV="/content/app/static/client/csv"
  CLIENT_REPORT="/content/app/static/client/reports"
  # app.config["CLIENT_IMAGES"]="/content/app/static/client/img"
  # app.config["CLIENT_CSV"]="/content/app/static/client/csv"
  # app.config["CLIENT_REPORT"]="/content/app/static/client/reports"
class TestingConfig(Config):
  TESTING=True  
  DB_NAME="production-db"
  DB_USERNAME="root"
  DB_PASSWORD="example"    
  UPLOADS="/home/username/app/app/static/images/uploads"
  SESSION_COOKIE_SECURE=False
  # app.config["CLIENT_IMAGES"]="/content/app/static/client/img"
  # app.config["CLIENT_CSV"]="/content/app/static/client/csv"
  # app.config["CLIENT_REPORT"]="/content/app/static/client/reports"