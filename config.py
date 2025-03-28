import os

# Global configurations
APP_NAME = 'Intelligent Air Traffic Simulator'
SI       = 'SI'     # SI unit
NAUTIC   = 'NAUTIC' # Geographic unit (NM, FEET, KNOTS etc)


# Web server configuration
SERVER_PORT   = 8888
SERVER_ROOT   = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ROOT = os.path.join(SERVER_ROOT, "client", "build")
STATIC_ROOT   = os.path.join(TEMPLATE_ROOT, "static")


# SQL Database configuration
SQLITE_PATH = os.path.join(SERVER_ROOT, "bin", "sqlite", "isim.db")
DB_URL = "sqlite:///{}".format(SQLITE_PATH)


# BADA directory
BABA_DIR = os.path.join(SERVER_ROOT, "bin", "bada", 'bada36')

# ISA Temperature deviation
DELTA_TEMP_ISA = 0.0