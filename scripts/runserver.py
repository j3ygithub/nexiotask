from settings import HOST, PORT
from views import app

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
