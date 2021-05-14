from settings import HOST, PORT
from views import app


def runserver():
    app.run(host=HOST, port=PORT)


if __name__ == "__main__":
    runserver()
