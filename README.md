# A Skeleton Flask Project

> A skeleton Flask project that uses MySQL and Marshmallow, as well as Flask API and Request libraries.

View the source code at the following [Github repository](https://github.com/transreductionist/flask_web).

Author: Aaron Peters

## What does the project do?

Every once in a while I have needed a skeleton Flask application that had some core functionality, 
e.g. validation/serialization, error handling, configuration loading, and other stuff. I would build it
and throw it away. Last night I decided to put it in a repository so it would be available whenever I
needed it.

## Terms of Use

Please use responsibly.

## Prerequisites

- Git
- Python 3.8
- MySQL Database

## Installation

Create a working directory

- mkdir flask_web
- cd flask_web

We us Conda as our package manner, which is a nice integrated framework for building environments. It installs
with `pip` and so allows packages to be added with `pip install` as well as `conda install`.

You may want to use virtualenv along with `pip install` to build and manage your environments.

Create our environment:

- conda create --name flask_web python=3.8

Install Flask:

- conda install -c flask

Install some useful Flask libraries:

- conda install -c flask-api
- conda install -c conda-forge flask-restful
- conda install -c conda-forge flask-marshmallow
- conda install -c conda-forge flask-sqlalchemy
- conda install -c conda-forge marshmallow-sqlalchemy

Install MySQL and SQLAlchemy:

- conda install -c mysql
- conda install -c pyqmysql
- pip install mysqlclient
- pip install mysql-connector-python
- conda install -c sqlalchemy

Install PyYAML to handle configuration files:

- conda install -c anaconda yaml

Now senf the requirements to a text fie:

- conda list --explicit > conda_requirements.txt

## Use case

In a terminal window in the root directory issue the command:

`(flask_web) MacBook-Pro flask_web % python app.py`

You should see something like:

```
 * Serving Flask app "flask_web" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 225-690-418
```

Now send a GET request to the endpoint:

`http://127.0.0.1:5000/splash`

and retrieve all the names from the database.

## Documentation

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask API](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/)
- [Flask Restful](https://flask-restful.readthedocs.io/en/latest/)
- [Flask Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/index.html)
- [Conda](https://docs.conda.io/en/latest/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Docker](https://docs.docker.com/docker-hub/)
