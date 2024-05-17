import os


SECRET_KEY = 'lzyemNIn1rd0cy2QTewpoTPYvoJaOe5uAysLm3BhkhvCrO-kudNf7o4E5wAuNme3EFVlzC4ipi2iP4AXPIE7NQ'

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'local')


# Todo: all the settings here will be put into default config and value will be put into cloud environment /
#  secret manager variable
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')  # 10.86.192.5  #34.101.53.17
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5432')
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres') #loyalty_program
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '0811565827') ##;&x}MZrb%[BgMcr
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'praktek')
POSTGRES_CLOUD_INSTANCE = os.environ.get('POSTGRES_CLOUD_INSTANCE', 'appsdevtestenv:asia-southeast2:taiga-db')

SSL_ROOT_CERT = os.environ.get('SSL_ROOT_CERT', 'serverkeys/server_ca')
SSL_CERT = os.environ.get('SSL_CERT', 'serverkeys/client_cert')
SSL_KEY = os.environ.get('SSL_KEY', 'serverkeys/client_key')

if ENVIRONMENT == 'local' or ENVIRONMENT == 'development':
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/' \
                              f'{POSTGRES_DB}'
else:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/' \
                              f'{POSTGRES_DB}?sslmode=verify-ca' \
                              f'&sslrootcert={SSL_ROOT_CERT}&sslcert={SSL_CERT}&sslkey={SSL_KEY}'

SQLALCHEMY_ECHO = True
DATABASE_PATH = 'instance'
