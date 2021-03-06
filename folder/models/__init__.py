from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

__base__ = declarative_base()

class Users(__base__):
    __tablename__ = "users"

    uuid = Column(String, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self) -> str:
        return '<Users %r>' % self.username

    def __str__(self) -> str:
        return f"(uuid: {self.uuid}, username: {self.username}, email: {self.email})"