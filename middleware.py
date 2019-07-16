from firebase_admin import db
from Firebase_cred import firebase_auth
from flask import Flask, request

firebase_auth.initial()

root = db.reference()


def removeIllegalChar(str):
    return ''.join(e for e in str if e.isalnum())


def startApp():
    app = Flask(__name__)

    # To store user information
    # Email, Gender, Location, Name

    # TESTING INPUT
    """{
        "Email":"hrgutou@gmail.com",
        "Name" : "Haoran He",
        "Gender" : "Male",
        "Location":"NY"
    }"""

    @app.route('/user', methods=['POST'])
    def user_information():
        # Accept POST request but must be in "application/json" type
        info = request.json

        try:
            root.child(removeIllegalChar(info['Email'])).update(
                info
            )

        except Exception as e:
            print(e)

        return 'OK'

    # To store the result
    # If user not exist in the database, the result will NOT be saved
    # but this step can be ignore if the webapp can prevent users from performing the test BEFORE entering their info

    # TESTING INPUT
    """{
        "Email":"hrgutou@gmail.com",
        "Color" : "color",
        "Font" : "font",
        "HeartrateLow": "60",
        "HeartrateHigh" :"90"
    }"""

    @app.route('/result', methods=['POST'])
    def user_results():
        # Accept POST request but must be in "application/json" type
        results = request.json

        try:
            root.child(removeIllegalChar(results['Email'])).child("Results").update(
                results
            )

        except Exception as e:
            print(e)

        return 'OK'

    app.run()


if __name__ == '__main__':
    startApp()
