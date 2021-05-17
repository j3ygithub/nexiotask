from sqlalchemy.exc import IntegrityError

from flask import abort
from . import status_codes


class SQLAlchemyActionMixin:
    """
    A mixin containing some simple wrapper about actions of `SQLAlchemy`.
    """
    def create(self, db_session):
        db_session.add(self)
        try:
            db_session.commit()
        except IntegrityError:
            abort(status_codes.BAD_REQUEST)

    def update(self, data, db_session):
        for key, value in data.items():
            setattr(self, key, value)
        try:
            db_session.commit()
        except IntegrityError:
            abort(status_codes.BAD_REQUEST)

    def delete(self, db_session):
        db_session.delete(self)
        try:
            db_session.commit()
        except IntegrityError:
            abort(status_codes.BAD_REQUEST)
