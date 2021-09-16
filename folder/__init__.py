from typing import Any
from sqlalchemy import create_engine
from flask import Flask, _app_ctx_stack
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session
from .models import __base__

def ignite_whisper(name: str, database_uri: str, *args: Any, **kwargs: Any) -> Flask:
    app = Flask(name)
    engine = create_engine(database_uri, *args, *kwargs)
    ses = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    __base__.metadata.create_all(bind=engine)
    app.session = scoped_session(ses, scopefunc=_app_ctx_stack.__ident_func__)

    return app