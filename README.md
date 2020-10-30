# Mlango10 


###  Author
#### JOHN OSIKO
Mlango10 is a Python/Django application.

## Description
Mlango10 is a Python/Django application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.


## User Story
A user would:
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## BDD

## Technologies

* Python 3
* Django
* Heroku
* HTML
* Bootstrap

## Build
* Clone the repositories
    `git clone https://github.com/John-Osiko/Mlango10.git`
* Open root directory
    `cd Mlango10`
* Install requirements
    `python -m pip install -r requirements.txt`
* Create a database
    `psql`
    `CREATE DATABASE {database name}`
* Export configurations
    `export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}`
* Migrate database
    `python3 manage.py makemigrations {database name}`
    `python3 manage.py migrate`
* Run the application
    `python3.6 manage.py runserver`
* Run tests on the application
    `python3.6 manage.py test`

## Support and Contact Details
Remember to give a star to my repo if you like the web application
   ==>To reach me, send me a mail to <a href="https://mail.google.com/">johnmaxosiko@gmail.com</a>
      Thanks, for the star.
## Licensing
This is a non-profit project. The article has been created by under the terms of BSD license.