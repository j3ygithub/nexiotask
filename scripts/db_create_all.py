from models import db


def db_create_all():
    db.create_all()


if __name__ == "__main__":
    db_create_all()
