import os


# Settings constants from Environment variable

# Database settings
DB_HOST=os.environ['DB_HOST']
DB_PASSWD=os.environ['DB_PASSWORD']
DB_USER=os.getenv('DB_USER', default='root')
DB_DATABASE=os.environ['DB_DATABASE']


# Broker settings
BROKER_URL = os.environ['BROKER_URL']
