# Contacts App
A website where a user can login and add his contacts by entering the following fields.
* Contact Name
* Contact Number
* Contact Email
-----
## Virtual Environment setup

**<ins>Ubuntu</ins>**

Install virtualenv **cmd: sudo apt install python3-virtualenv**

create virtual environment  **cmd: virtualenv env**

activate virtual environemt **cmd: source env/bin/activate**

## Database
Create a file db.sqlite3 in the parent directory

## Django setup
Step1 : pip install -r requirements.txt

Step2 : python manage.py makemigrations

Step3 : python manage.py migrate

## To run server 
Step1 : python manage.py runserver
