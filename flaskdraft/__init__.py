from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import smtplib
from flaskdraft.settings import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


#explanation why this is better:


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    #--------import users routes----------#


    from flaskdraft.users.routes import users 
    from flaskdraft.posts.routes import posts
    from flaskdraft.main.routes import main
    from flaskdraft.players.routes import players
    from flaskdraft.years.routes import mock
    from flaskdraft.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(players)
    app.register_blueprint(mock)
    app.register_blueprint(errors)


    return app