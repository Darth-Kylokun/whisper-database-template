"""
* uuid = Column(String, primary_key=True, nullable=False)
* username = Column(String, nullable=False, unique=True)
* email = Column(String, nullable=False, unique=True)
"""
import uuid as ud
from typing import Union
from folder.models import Users
from sqlalchemy.orm import scoped_session
from sqlalchemy.exc import IntegrityError

DBResult = Union[Users, IntegrityError]
DBOption = Union[Users, None]

def new_user(session: scoped_session, username: str, email: str) -> DBResult:
    try:
        uuid = ud.uuid4().hex
        user = Users(uuid=uuid, username=username, email=email)
        session.add(user)
        session.commit()
        return user
    except IntegrityError as ie:
        raise ie # Here so in case I want to do something about his

# * Since all values are unique in the user database we dont need to check for multiple results

def get_user_by_username(session: scoped_session, username: str) -> DBOption:
    return session.query(Users).filter(Users.username == username).one_or_none()

def get_user_by_uuid(session: scoped_session, uuid: str) -> DBOption:
    return session.query(Users).filter(Users.uuid == uuid).one_or_none()

def get_user_by_email(session: scoped_session, email: str) -> DBOption:
    return session.query(Users).filter(Users.email == email).one_or_none()