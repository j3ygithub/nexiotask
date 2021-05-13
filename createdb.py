from models import db, User

if __name__ == "__main__":
    db.create_all()
    # user = User(username="jimmy_lin", email="jimmy_lin@chief.com.tw")
    # db.session.add(user)
    # user = User(username="allen_yang", email="allen_yang@chief.com.tw")
    # db.session.add(user)
    # user = User(username="marco_li", email="marco_li@chief.com.tw")
    # db.session.add(user)
    db.session.commit()
