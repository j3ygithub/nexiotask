import argparse

from apps import create_app


def helloworld():
    print("hello world")


def runserver():
    app = create_app("development")
    app.run()


tasks = {
    "helloworld": helloworld,
    "runserver": runserver,
}
available_task = ", ".join(tasks.keys())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "task_name", help=f"Please enter a script name. Choices are: {available_task}."
    )
    args = parser.parse_args()
    task_name = args.task_name
    task = tasks[task_name]
    task()
