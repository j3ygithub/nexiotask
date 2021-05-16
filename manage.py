import argparse

from app import create_app, db


def runserver():
    app = create_app("development")
    app.run(host="0.0.0.0")


def db_create_all():
    app = create_app("development")
    app.app_context().push()
    db.create_all()


def db_drop_all():
    app = create_app("development")
    app.app_context().push()
    db.drop_all()


tasks = {
    "runserver": runserver,
    "db_create_all": db_create_all,
    "db_drop_all": db_drop_all,
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "task_name",
        help=f'Please enter a script name. Choices are: {", ".join(tasks.keys())}.',
    )
    args = parser.parse_args()
    task_name = args.task_name
    task = tasks[task_name]
    task()
