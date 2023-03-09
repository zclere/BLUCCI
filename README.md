# BLUCCI

This is a Magazine App that you can use to store your fav magazines and share with people you love.


## Installation
The master branch is the standard branch, we're gonna work with it to set this project up.


## STEP 1:
Download/Fork this project

Open terminal inside the root folder
```
ls
```
Check if manage.py appears in the list, if it does then move onto the next step 


## STEP 2:
Install Virtualenv
```
pip install virtualenv
```
Create Virtual Environment inside the root folder
```
virtualenv env
```
Activate Environment

on MAC/Linux:
```
source env/bin/activate
```
on Windows:
```
env/scripts/activate
```

## STEP 3:
Install Requirements for this project
```
pip install -r requirements.txt
```

## STEP 4:
Create a .env file to store project secrets inside the root folder

on MAC/Linux:
```
touch .env
```
on Windows:

 - use a text editor or git bash to create the file

Add Project Secret Key inside the .env file
```
project_secret_key = make_this_value_unique_and_50_characters_long
```

## STEP 5:
Migrate Database
```
python manage.py makemigrations
python manage.py migrate
```
Create a Super User to log in on the Admin Panel
```
python manage.py createsuperuser
```

## STEP 6:
Now we just need to change the username from "blucci" to whatever username you created previously, inside these files:

	- home/views.py
	- magazine/views.py


## STEP 7:
Start the development server
```
python manage.py runserver
```
Access the Admin Panel
```
http://127.0.0.1:8000/admin
```
Access the Webapp
```
http://127.0.0.1:8000
```
