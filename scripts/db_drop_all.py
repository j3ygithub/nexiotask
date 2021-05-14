from models import db


def db_drop_all():
    db.drop_all()


if __name__ == "__main__":
    db_drop_all()
