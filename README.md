Intern Python
=============

## Development
### Requirement
* Python 3.6+
Ubuntu 14.04 or 16.04

```shell
$ sudo add-apt-repository ppa:jonathonf/python-3.6
# --or--
# sudo add-apt-repository ppa:fkrull/deadsnakes

$ sudo apt-get update
$ sudo apt-get install python3.6
```

* pip 9+

```shell
$ sudo apt-get install python-pip
```

* Virtual Environments

```shell
$ sudo apt-get install virtualenv virtualenvwrapper
$ virtualenv -p $(which python3.6) $HOME
```

--- Test python ---  

```shell
$ python --version
Python 3.6.1
$ pip --version
pip 9.0.1 from /home/dungdm93/lib/python3.6/site-packages (python 3.6)
```

--- Troubleshooting ---  

If virtual won't work, restart your shell:
```shell
$ exec -l $SHELL
```

If still won't work, check those lines exist in your `~/.profile` or `~/.bashrc`

```shell
# set PATH so it includes user's private bin directories
PATH="$HOME/bin:$HOME/.local/bin:$PATH"
```

### Setup project
* Clone repo

```shell
$ git@git.teko.vn:platform/saletool-notification-server.git
$ cd saletool-notification-server
```

* Install dependencies

```shell
$ pip install -r requirements.txt
```

### Run & test :gear:
#### Locally
* Upgrade database

```shell
$ flask db upgrade
```

* Run

```shell
$ export FLASK_APP=main.py
$ flask subscribe_teko_queue
$ flask run
```

* Test

```shell
# Unit test
$ py.test
# Pytest with coverage
$ py.test --cov=src --cov-report=term --cov-report=html
```

#### inside Docker
* Setup db
```shell
$ docker run -d --name mysql \
         -p 3306:3306 \
         -e MYSQL_ROOT_PASSWORD=supersecret \
         -e MYSQL_DATABASE=stn \
         mysql
$ export SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:supersecret@localhost:3306/stn"
```

* run app

```shell
$ export FLASK_APP=main.py
$ export ENV_MODE=prod
$ flask db upgrade heads # migrate db
$ gunicorn -c etc/gunicorn.conf.py main:app
```

* run nginx

```shell
$ docker run -d --name nginx \
    -v $(pwd)/var/web-gunicorn.sock:/var/www/stn/var/web-gunicorn.sock \
    -v $(pwd)/etc/stn.teko.vn.nginx:/etc/nginx/conf.d/default.conf:ro \
    -p 80:80 nginx
```

## Production
TODO
