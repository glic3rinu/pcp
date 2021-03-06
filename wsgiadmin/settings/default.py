# File with default setting values
# Copy this file to local.py and change it there

BANK_NAME = ""
BANK_ACCOUNT = ""
BANK_CODE = ""

# Token for access to Czeck FIOBank
FIO_TOKEN = None

# When user will be reminded in case of insufficient amount of resources
CREDIT_TRESHOLD = 20
# When users apps will be killed
KILLER_TRESHOLD = -20
NUMBER_OF_REMINDS_TO_KILL = 20

GUNICORN_PROXY_PORT = 12000

NODE_VERSIONS = (
    ("0.10", "0.10.x"),
)

PHP_INI_PATH = "/etc/php5/cgi/php.ini"