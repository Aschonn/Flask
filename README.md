# Flask Project

<a href='https://hpforiginals.com'>Flask Project Link</a>

<br>

# Motivation:
To compare different frameworks and to see which would give me the best result. I figured the best way to test this out would be to create identical Applications using those both frameworks.

<br>

# Dependencies:
- I used python 3.8.2 but anything over 3.7 will work.
- All the related dependencies are in the requirements.txt

<br>

# Required Knowledge:
- Flask (Framework) 
- Python (Language)
- SQLAlchemy (translater)
- Jinja (HTML helper)
- Linode (Server)
- Postgresql (Database)  

<br>

# SETUP AND GETTING STARTED:

## RUNNING IN VIRTUAL ENV:
1) Install dependency: 
    
        pip install virtualenv

2) Create Virtualenv :

        virtualenv -p /usr/bin/python3 env

3) Activate Virtualenv : 

        source env/bin/activate

4) Deactivate : 
        
        deactivate

<br>

## ENVIROMENTAL VARIABLES (in project):

Install python-dotenv:

     $ pip install dotenv

Create a '.env' file:

     $ touch .env

Add DATABASE_URL:

     DATABASE_URL = "postgres://{username}:{password}@localhost:{port}/{database_name}"

Add SECRET_KEY (OPTIONAL):

     SECRET_KEY = "{SECRET_KEY}"


<br>

## INITIATE DATABASE (MIGRATIONS)

1) Initialize Migrations: 

        python manage.py db init

2) Create Migration:

        python manage.py db migrate


3) Use Migration:

        python manage.py upgrade

 <br>

## MAILTRAP SETUP:

1) Setup and account 
2) create a new inbox
3) enter in your own credentials into send_mail.py



<br>

# (MANUALLY) INSERT DATA INTO TABLES:


## ADD PLAYERS: (Required: name, year_id, and year_rank)

    insert into player(name, position, college, height, classof, position_rank, year_id, year_rank, biography) values 
    (
        'Anthony Edwards',
        'SG',
        'Georgia',
        '6-5',
        '2020,
        1,
        '2020',
        '6’4 combo guard with elite level athleticism … Shows a good feel for the game and competitiveness … Good size and length for position with a 6’9 wingspan and 8’4 standing reach … Strong build'
    );

## ADD YEARS: 

    insert into year(year) values ('2020');





# SPECIAL FEATURES:


## RESIZING IMAGE:

Using PILLOW:
-Speed up website and efficiently store minimial sized photos in database

#PAGINATION
Using the paginate() method we are able to specify page number

#passwords:
Hashed 


## Blueprints
In this project we incorporate blueprints which help efficiently scale bigger projects. This is AKA called a application factory at it makes it easier to sift through endpoint and a mutlitude of other things...it makes it easier. It divded the applcation into testing and production aka application factory


## configuation
Add enviromental variables for secrecy and condigured application so it is scalable and easy to change and fix bugs

## error Pages:
404 --Mostcommon: Page is nonexistant
403 --Mostcommon: Unathorized (user needs to login)
500 --Mostcommon: Server Error (Database Problems)

## linode (Linux from scratch)
1) ssh@ip
2) update and upgrade
3) hostname set-hostname draft-server
4) nano /ect/host
5) add ip underneath localhost (create connection)
6) create limited priv user
7) ssh username@ip and enter you custom password

### More information on Linode Setup: 
    https://www.youtube.com/watch?v=goToXTC96Co&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=13

setting up:ssh and firewalls
scp ~/.ssh/id_rsa.pub username@<ip>:~/.ssh/authorized


## encrypt:
- More information: https://letsencrypt.org/getting-started/

<br>

# OPTIONAL:

Configure firewall (UFW):
Configuration:
sudo ufw default deny incoming (nothing comes in)
sudo ufw default allow outgoing (we can send stuff out)
sudo ufw allow ssh (allows ssh)
sudo ufw allow 5000 (allow for testing)
scp -r Desktop/flaskdraft username@<ip>

sudo apt install python3-pip
sudo apt install python3-venv

## FLASKDRAFT TREE:

    ├── config.py
    ├── errors
    │   ├── handlers.py
    │   └── __init__.py
    ├── __init__.py
    ├── main
    │   ├── __init__.py
    │   └── routes.py
    ├── models.py
    ├── players
    │   ├── forms.py
    │   ├── __init__.py
    │   └── routes.py
    ├── posts
    │   ├── forms.py
    │   ├── __init__.py
    │   └── routes.py
    ├── send_mail.py
    ├── static
    │   ├── profile_pics
    │   │   ├── default.jpg
    │   └── style.css
    ├── templates
    │   ├── about.html
    │   ├── account.html
    │   ├── add_post.html
    │   ├── base.html
    │   ├── errors
    │   │   ├── 403.html
    │   │   ├── 404.html
    │   │   └── 500.html
    │   ├── feedback.html
    │   ├── home.html
    │   ├── login.html
    │   ├── post.html
    │   ├── post_player.html
    │   ├── register.html
    │   ├── reset_request.html
    │   ├── reset_token.html
    │   ├── success.html
    │   ├── user_posts.html
    │   └── year.html
    ├── test_app.py
    ├── users
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── routes.py
    │   └── utils.py
    └── years
        ├── forms.py
        ├── __init__.py
        └── routes.py



