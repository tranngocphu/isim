import os


# Global configurations
APP_NAME = 'Intelligent Air Traffic Simulator'

# Web server configuration
SERVER_PORT   = 8888
SERVER_ROOT   = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ROOT = os.path.join(SERVER_ROOT, "client", "build")
STATIC_ROOT   = os.path.join(TEMPLATE_ROOT, "static")


# SQL Database configuration
SQL_MODE = 'sqlite' # 'sqlite' or 'mysql
HOST     = '127.0.0.1'
DATABASE = 'isim'
USER     = 'root'
PASSWORD = 'root'
SQL_PORT = '3306'
SQLITE_PATH = os.path.join(SERVER_ROOT, "bin", "sqlite", "isim.db")
DB_URL   = "mysql+mysqldb://{}:{}@{}:{}/{}".format(USER, PASSWORD, HOST, SQL_PORT, DATABASE) if SQL_MODE == 'mysql' else "sqlite:///{}".format(SQLITE_PATH)


