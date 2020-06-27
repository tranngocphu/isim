import os


# Global configurations
APP_NAME = 'Intelligent Air Traffic Simulator'


# SQL Database configuration
HOST     = '127.0.0.1'
DATABASE = 'isim'
USER     = 'root'
PASSWORD = 'root'
SQL_PORT = '3306'

DB_URL   = "mysql+mysqldb://{}:{}@{}:{}/{}".format(USER, PASSWORD, HOST, SQL_PORT, DATABASE)


# Web server configuration
SERVER_PORT   = 8888
SERVER_ROOT   = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ROOT = os.path.join(SERVER_ROOT, "client", "build")
STATIC_ROOT   = os.path.join(TEMPLATE_ROOT, "static")