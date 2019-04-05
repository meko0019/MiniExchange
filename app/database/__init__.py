import datetime
import time

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression
from sqlalchemy.sql import text
from sqlalchemy.types import DateTime


__all__ = [
    "db",
    "DATETIME_FORMAT",
    "DATE_FORMAT",
    "NULL",
    "FALSE",
    "TRUE",
    "UTCNOW",
    "isofmt",
    "MetadataModel",
    "BaseModel",
]


db = SQLAlchemy(session_options={"autoflush": True, "autocommit": False})

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
NULL = text("NULL")
FALSE = text("false")
TRUE = text("true")


def isofmt(dt):
    if dt is None:
        return None
    return dt.strftime(DATETIME_FORMAT)


class UTCNOW(expression.FunctionElement):
    type = DateTime()


@compiles(UTCNOW, "postgresql")
def postgres_utcnow(element, compiler, **kwargs):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


MetadataModel = db.Model


class BaseModel(MetadataModel):
    """Base model which comes with an `id` primary key.
    """

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    modified_at = Column(
        DateTime,
        server_default=UTCNOW(),
        onupdate=datetime.datetime.utcnow,
        nullable=False,
    ) 
    _created_at = db.Column(DateTime, server_default=UTCNOW(), nullable=False)

    def __json__(self):
        return {"id": self.id, "created_at": self._created_at, "modified_at": isofmt(self.modified_at)}


