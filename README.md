# nexiotask

A task from Nexio. A user model api with `flask`.

## Installation & Run

git clone
```bash
git clone https://github.com/j3ygh/nexiotask /Users/jimmy_lin/repos/nexiotask
```

CD to the repo root
```bash
cd /Users/jimmy_lin/repos/nexiotask
```

build venv & install packages
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt
```

build DB
```bash 
python manage.py db_create_all
```

run a development server
```bash 
python manage.py runserver
# Now you should see something on http://127.0.0.1:5000/ with your browser.
```

## Run tests

> All testings are written with <a href="https://docs.python.org/zh-tw/3/library/unittest.html">unittest</a>.

run all tests
```bash
python -m unittest
```
> Please make sure you have activate the venv and run this under the repo root.


run a single test
```bash
python user/tests.py
```
> It is just like how you run a python script.


## Run with docker

build image
```bash
docker build -t "your-name/nexiotask" .
```

run with port 80
```bash
docker run -p 80:5000 'nexiotask'
# Now you should see something on http://127.0.0.1/ with your browser.
```

or simpler, run with docker-compose
```bash
docker-compose up
# Now you should see something on http://127.0.0.1/ with your browser.
```


## Meta

Jimmy Lin <b00502013@gmail.com>

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/j3ygh/](https://github.com/j3ygh/)

## Contributing

1. Fork it (<https://github.com/j3ygh/nexiotask/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
