# NavjivanCMS

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-green.svg)
![CMS](https://img.shields.io/badge/Project-Type--CMS-blue)
![Contributions welcome](https://img.shields.io/badge/Contributions-welcome-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

NavjivanCMS is a real-time content management system (CMS) built with Django. It is designed to securely store and manage comprehensive user data, including personal information, government documents, and educational records. The CMS ensures that all user information is stored efficiently, securely, and can be accessed or updated in real-time.

## Features

- Secure management of user data such as full name, birth date, Aadhaar card, educational documents, and more
- Real-time access and updates for sensitive data
- Built-in security for data integrity and privacy

## Prerequisites

To run this project, you need to have the following installed on your system:

- Python 3.x (using `pyenv` to manage Python versions)
- Django
- Virtualenv (optional but recommended)
- A database (e.g., PostgreSQL, MySQL, SQLite)

## Installation

Follow the steps below to set up the project on your local machine.

### 1. Install `pyenv`

Make sure `pyenv` is installed and configured. You can install it by following the instructions [here](https://github.com/pyenv/pyenv#installation).

### 2. Clone the repository

```bash
git clone https://github.com/your-username/NavjivanCMS.git
cd NavjivanCMS
```

### 3. Set the Python version using `pyenv`

```bash
pyenv install 3.10.0  # or Replace with the appropriate Python version
pyenv local 3.10.0
```
### 4. Set up a virtual environment using `pyenv-virtualenv`

```bash
pyenv virtualenv 3.10.0 navjivan-cms-env
pyenv activate navjivan-cms-env
```
### 5. Install dependencies
```bash
pip install -r requirements.txt
```

### 6. Configure environment variables
Create a `.env` file in the root directory of the project (At the same level of `manage.py` file) and set up the required environment variables for your database, secret key, etc.

Example `.env`:

```bash
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_PORT=your_database_port
DB_HOST=localhost
```
### 7. Apply migrations
Run the following commands to set up the database schema:
```bash
python manage.py migrate
```
### 8. Create a superuser
To access the Django admin panel, you’ll need a superuser. Create one using the following command:
```bash
python manage.py createsuperuser
```
### 9. Run the development server
Start the Django development server by running:
```bash
python manage.py runserver
```
Now, you can access the application at http://127.0.0.1:8000/.

## Development (Docker with live-reload)

We provide a development compose file which mounts your local source into the container and runs the Django development server with auto-reload support.

Start the dev environment:

```bash
# build and start services
docker compose -f docker-compose.yml up --build
```

Edit Python files locally and the Django autoreloader (helped by `watchdog`) will restart the server inside the container so changes reflect in near real-time. If file changes are not detected on Linux hosts, increase inotify watchers:

```bash
# on host
sudo sysctl fs.inotify.max_user_watches=524288
echo "fs.inotify.max_user_watches=524288" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

Notes:
- This mode is intended for local development only. Do NOT use volume mounts in production images.
- For production builds, use `docker-compose.yml` and run via your CI/CD with a production-ready WSGI server like Gunicorn.

### Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue.
