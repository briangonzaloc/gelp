Requirements

    Python 3 in order to execute Django 2
    NPM

Quick Setup
    Clone this project

	Backend:

    python3 -m venv [name_of_virtualenv]
    source [path_to_virtualenv]/bin/activate
    Move into the folder backend and execute pip3 install -r requirements.txt && python3 manage.py makemigrations && python3 manage.py migrate
    Create super user inside the project root python3 manage.py createsuperuser
    python3 manage.py runserver

	Frontend:

	In package directory, execute npm install to get all dependencies
	Run server, execute npm start
