from sqlalchemy.exc import IntegrityError
from folder.models import Users
from folder import Whisper
from flask import request, jsonify, Flask
from folder import actions

"""
! NEED TO CREATE A EMAIL WRAPPER
! WILL BE NOT AS SECURE IF ONLY USE EMAIL
"""

app = Flask(__name__)

# * Class built to inject SqlAlchemy into it
whisper = Whisper(app, "sqlite:///dad.db")

@whisper.app.post("/new_user")
def new_user():
    data = request.get_json()

    username = data["username"]
    email = data["email"]

    try:
        user: Users = actions.new_user(whisper.app.session, username, email)
    except IntegrityError:
        return jsonify({'code': 400, 'message': "Username/email already in use"})

    print(type(user))

    user = str(user)
    return jsonify({'code': 200, 'message': "User successfully cretated", 'user': f'{user}'})