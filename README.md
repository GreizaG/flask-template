# Running this Flask Template App

Here's a joyful guide to set up and run this template! 🚀

## Project Structure

The project follows a structured layout conducive to the Factory Pattern for initializing and configuring various components of the application. Here's a breakdown of the directory structure:


 - `app_project`: Root directory for the project.
    - `ext`: Holds extensions and configurations, potentially housing factory functions for creating and initializing extensions.
    - `models`: Contains the data models of the application.
    - `routes`: Holds the route definitions.
    - `static`: Directory for static files.
        - `css`: Holds stylesheet files.
        - `images`: Contains image files.
        - `js`: Holds JavaScript files.
    - `templates`: Contains the HTML templates.
    - `utils`: Utility functions and classes.


The Factory Pattern is applied to ensure a clean separation of concerns, making it easy to configure and extend various components independently. The pattern helps in centralizing the creation and initialization logic, making the codebase organized and scalable.



## Table of Contents
1. [Setup a Virtual Environment](#1-setup-a-virtual-environment)
2. [Activate the Virtual Environment](#2-activate-the-virtual-environment)
3. [Install Dependencies](#3-install-dependencies)
4. [Environment Variables Configuration](#4-environment-variables-configuration-🛠️)
5. [Installing PostgreSQL on macOS and Linux](#installing-postgresql-on-macos-and-linux-🐘)
6. [Installing PostgreSQL on Windows](#installing-postgresql-on-windows-🪟)
7. [Run Your Flask Application](#run-your-flask-application-🏃)
8. [Included extensions](#🧩-included-extensions)

## 1. Setup a Virtual Environment

First, navigate to your project directory in the terminal, then create a virtual environment using the `venv` module. 

*Make sure that you have installed Python version 3.10 or 3.11. If not, you can search google or YouTube on how to install python 3.10 or 3.11 in your operating system.*

```bash
$ git clone https://github.com/devAbreu/flask-template.git
$ cd flask-template
$ python3.11 -m venv env or 3.10 -m venv env # This depends on your python version installed.
```

This will create a new directory named `env` in your project directory. 📁

## 2. Activate the Virtual Environment

Activate the virtual environment using the following command:

- On Windows:

```bash
$ env\Scripts\activate
```

- On macOS and Linux:

```bash
$ source env/bin/activate
```

Once activated, the virtual environment will isolate your Python and pip versions along with the installed dependencies from the global environment. 🌐


## 3. Install Dependencies

Now, install the necessary dependencies listed in the `requirements.txt` file:

```bash
$ pip install -r requirements.txt
```

Make sure your `requirements.txt` file is in the project directory or specify the path to it. 📜

## 4. Environment Variables Configuration 🛠️

This document describes the environment variables used in the project and provides detailed information about each one.

Create your `.env` file from the `.env.example` file. This will create a new environment file called `.env`

```bash
$ cp .env.example .env
```

### DATABASE_URI

`DATABASE_URI` is the connection string used by SQLAlchemy to connect to the database. It comprises:

- Database type: PostgreSQL
- Adapter: psycopg (a.k.a. psycopg 3) should work with psycopg v2 too.
- User: user
- Password: password
- Host: host
- Port: port
- Database Name: db_example

Example:
```plaintext
DATABASE_URI=postgresql+psycopg://user:password@host:port/db_example
```

### FLASK_APP_SECRET_KEY

`FLASK_APP_SECRET_KEY` is used to keep the client-side sessions secure. It is used to sign the session cookie. 🔐

Example:
```plaintext
FLASK_APP_SECRET_KEY=flask_secret_key
```

### JWT_SECRET_KEY

`JWT_SECRET_KEY` is used to encode JWT Tokens. It’s a secret key only known to the server. 🗝️

Example:
```plaintext
JWT_SECRET_KEY=jwt_secret_key
```

### FLASK_APP

`FLASK_APP` is the environment variable that points to the Flask application’s entry point. It is used by the flask command to find and run the application. 🚀

Example:
```plaintext
FLASK_APP=app_project/app.py
```

### FLASK_DEBUG

`FLASK_DEBUG` is an environment variable that enables/disables debug mode in Flask. When it is set to 1, the debug mode is enabled, providing more information on errors and reloading the server on code changes. 🐞

Example:
```plaintext
FLASK_DEBUG=1
```

### FLASK_RUN_PORT

`FLASK_RUN_PORT` specifies the port number where the Flask app will run. 🚪

Example:
```plaintext
FLASK_RUN_PORT=3001
```

## Notes

- It’s crucial to keep `FLASK_APP_SECRET_KEY` and `JWT_SECRET_KEY` confidential, as exposure can lead to security vulnerabilities. 🛡️
- Adjust the `FLASK_DEBUG` according to the environment; it is recommended to keep it disabled (`0`) in production environments to avoid exposing sensitive information.
- Update the `DATABASE_URI` with the correct user, password, host, port, and database name according to your setup.

# Installing PostgreSQL on macOS and Linux 🐘

To successfully run your Flask application with a PostgreSQL database, follow the steps below:

## 1. Install PostgreSQL

### macOS:
You can install PostgreSQL on macOS using Homebrew:

```bash
$ brew install postgresql@15
```

After installation, you can start PostgreSQL with:

```bash
$ brew services start postgresql@15
```
And stop PostgreSQL with:
```bash
$ brew services stop postgresql@15
```
*We execute this as postgresql@15 because we are using a specific version of PostgreSQL*

### Linux (Ubuntu/Debian):
On Linux, you can install PostgreSQL using the apt package manager:

```bash
$ sudo apt-get update
$ sudo apt-get install postgresql-15 postgresql-contrib-15
```

After installation, PostgreSQL should start automatically. If not, you can start it with:

```bash
$ sudo service postgresql start
```
Stop and Restart PostgreSQL using service:
```bash
$ sudo service postgresql stop
$ sudo service postgresql restart
```
## 2. Configure PostgreSQL

Create a new database and user for the app:

```bash
$ psql postgres
postgres=# CREATE DATABASE db_example;
postgres=# \c db_example;
db_example=# CREATE EXTENSION unaccent;
db_example=# CREATE USER myuser WITH PASSWORD 'mypassword';
db_example=# GRANT ALL PRIVILEGES ON DATABASE db_example TO myuser;
db_example=# \q
```

Replace `db_example`, `myuser`, and `mypassword` with your own values. 🔄

# Installing PostgreSQL on Windows 🪟

Follow these steps to set up a PostgreSQL database on Windows:

## 1. Install PostgreSQL

Download the PostgreSQL version 15.4 installer from the official [PostgreSQL download website](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). Run the installer and follow the on-screen instructions to install PostgreSQL on your machine. 🖥️

## 2. Set Up PostgreSQL

After the installation, launch the SQL Shell (psql) from the Start Menu.

When prompted, enter the necessary information to connect to your PostgreSQL server. You can press Enter to accept the default values for the server, database, and port. When prompted for a username, enter the username you created during the installation (or the default "postgres"), and then enter your password.

In the SQL Shell, execute the following commands to create a new database and user for your Flask application:

```bash
$ psql postgres
postgres=# CREATE DATABASE db_example;
postgres=# \c db_example;
db_example=# CREATE EXTENSION unaccent;
db_example=# CREATE USER myuser WITH PASSWORD 'mypassword';
db_example=# GRANT ALL PRIVILEGES ON DATABASE db_example TO myuser;
db_example=# \q
```

Replace `db_example`, `myuser`, and `mypassword` with your own values. 🔄


## Run Your Flask Application 🏃

With PostgreSQL installed and your Flask application configured, you can now run your Flask application:

```bash
$ flask run
```
You've successfully set up and run this Flask template app within a virtual environment! 🎉
Your Flask application should now be able to interact with your PostgreSQL database. Visit `http://127.0.0.1:3001` in your web browser to access your application, and `http://127.0.0.1:3001/routes` to view information about all the available endpoints in the application.

## 🧩 Included Extensions

This project comes pre-configured with several Flask extensions to aid development and enhance security, performance, and functionality. Below is a list of the included extensions along with a brief description of each:

- **Flask-Bcrypt**: Provides Bcrypt hashing utilities, essential for securely storing passwords.
- **Flask-CORS**: Handles Cross-Origin Resource Sharing (CORS), making cross-origin AJAX possible.
- **Flask-JWT-Extended**: Provides JSON Web Tokens (JWT) support, essential for secure user authentication.
- **Flask-Migrate**: Handles database migrations, making it easier to manage database schema changes.
>Note: There's also a commented-out initialization for the `Talisman` extension, which can be used for setting HTTP security headers. Uncomment and configure it as needed. 🔒
