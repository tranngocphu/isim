# Global configurations
APP_NAME = 'Intelligent Air Traffic Simulator'


# SQL Database configuration
HOST     = '127.0.0.1'
DATABASE = 'isim'
USER     = 'root'
PASSWORD = 'root'
PORT     = '3306'
DB_URL   = "mysql+mysqldb://{}:{}@{}:{}/{}".format(USER, PASSWORD, HOST, PORT, DATABASE)