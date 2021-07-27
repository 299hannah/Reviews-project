# Description

An application like Awwards 


## User stories
One is able to: 

View posted projects and their details
Post a project to be rated/reviewed
Rate/ review other users' projects
Search for projects 
View projects overall score
View my profile page

## Setup/Installation
On your terminal, clone the project.
    
    $ git clone git@github.com/299hannah/Reviews-project
    

Navigate into the cloned project.

    $ cd Reviews-project

Create a `.env` file.

    $ touch .env

Inside `.env`, add the following and fill the empty fields with the appropriate values:

```python
SECRET_KEY=
DEBUG=True
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost','.herokuapp.com','127.0.0.1'
DISABLE_COLLECTSTATIC=1
CLOUD_NAME= 
API_KEY=
API_SECRET=
```
The CLOUD_NAME, API_KEY, and the API_SECRET are from your account on [Cloudinary](https://cloudinary.com/).

Create the virtual environment and install the requirements from `requirements.txt`

    $ python3 -m venv env
    $ . env/bin/activate
    $ pip install -r requirements.txt


Perform a migration.

    $ python3 manage.py migrate


Start the server to run locally.

    $ python3 manage.py runserver

## API Endpoints
This site has 2 endpoints; 
    
- **Profiles:** []()

    - Query the profiles stored in the database.
- **Projects:** []()

    -  Query data about the projects stored in the database.

## Known Bugs
No known bugs.
## Technologies Used
- Django
- Python 3.8.5
- Bootstrap 3
- Postgresql
- Cloudinary
- Heroku
## Support and contact details
If you have any suggestions, you can reach me via [email](hannahwambui022@gmail.com).
### License
 [(https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright &copy; 2021 **[299hannah](www.github.com/299hannah)**