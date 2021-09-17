from sqlalchemy import create_engine
from flask import Flask, _app_ctx_stack
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session
from .models import __base__

class Whisper:
    def __init__(self, app: Flask, dbURI: str):
        self.app = app
        self._engine = create_engine(dbURI)
        ses = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        __base__.metadata.create_all(bind=self._engine)
        self.app.session = scoped_session(ses, scopefunc=_app_ctx_stack.__ident_func__)

    def get_sesion(self) -> scoped_session:
        return self.app.session