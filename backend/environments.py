# coding: utf-8
import socket

PROD = True

# if socket.gethostname() in ("ks-MacBook-Pro.local",):
#     PROD = False

print("PRODUCTION ENV : %s" % PROD)

if PROD:
    ALLOWED_HOSTS = ['apicig.online', 'www.apicig.online']

    MYSQL = {
        'NAME': 'fga_db',
        'USER': 'root',
        # Mot de passe serveur prod. Attention!
        'PASSWORD': "CIGdev",
        'HOST' : 'localhost',
        # 'PASSWORD': "MoDu",
    }

    STATIC_URL = '/static/'

    MEDIA_URL = '/media/'

    CORS_ORIGIN_WHITELIST = [
        'https://inscription.forumgalienafrique.com',
        'https://apicig.online',
    ]

else:
    MYSQL = {
        'NAME': 'fga_db',
        'USER': 'root',
        # 'PASSWORD': "CIGdev",
        'PASSWORD': "MoDu",
        'HOST' : 'localhost',
        'PORT': 3306
    }

    ALLOWED_HOSTS = [
        '*'
        # 'localhost',
        # '127.0.0.1',
        # '164.92.125.149',
        #'http://51.77.215.159'
    ]

    STATIC_URL = '/static/'

    MEDIA_URL = '/media/'

    CORS_ORIGIN_WHITELIST = [
        'http://localhost:4200',
    ]

print(PROD, MYSQL)
