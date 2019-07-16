import firebase_admin
from firebase_admin import credentials


def initial():
    cred = credentials.Certificate("Firebase_cred/breathing-35a93-firebase-adminsdk-1r6f8-4051c0919c.json")

    firebase_admin.initialize_app(cred, {
        'databaseURL' : 'https://breathing-35a93.firebaseio.com/'
    })
