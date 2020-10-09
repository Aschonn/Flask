from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskdraft import db, login_manager
from flask_login import UserMixin

#usermixin = isauthenicated, anonymous, isactive, getid


#load user
@login_manager.user_loader
def load_user(userinfo_id):
    return UserInfo.query.get(int(userinfo_id))



#-----------------USERINFO AND CAPABILITES----------------#

class UserInfo(db.Model, UserMixin):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return UserInfo.query.get(user_id)


    def __repr__(self):
        return f"UserInfo('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    userinfo_id = db.Column(db.Integer, db.ForeignKey('userinfo.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


#---------------FEEDBACK MODELS--------------#


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, username, email, comments):
        self.username = username        
        self.email = email
        self.comments = comments
    
    


#-----------BASKETBALL MODELS---------------#

class Year(db.Model):
    __tablename__= 'year'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)

     # takes values from fields and allows us to use them
    def __init__(self, year, player):
        self.year = year
        self.players = players
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'year': self.year,
            'players': self.players     
            }

class Player(db.Model):
    __tablename__= 'player'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(6))
    college =  db.Column(db.String(200))
    height = db.Column(db.String(4))
    classof = db.Column(db.String(6))
    position_rank = db.Column(db.Integer)
    year_id = db.Column(db.String(6), nullable=False)
    year_rank = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(200))
    biography = db.Column(db.String(200))

    def __init__(self, name, position, college, height, classof, position_rank, year_rank, year_id, img, biography):
        self.name = name
        self.position = position
        self.college = college
        self.height = height
        self.classof = classof
        self.position_rank = position_rank
        self.year_rank = year_rank
        self.year_id = year_id
        self.img = img
        self.biography = biography
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'height' : self.height,
            'classof' : self.classof,
            'college' : self.college,
            'position_rank' : self.position_rank,
            'year_rank' : self.year_rank,
            'year_id' : self.year_id,
            'img' : self.img,
            'biography': self.biography
        }