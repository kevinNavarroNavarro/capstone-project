import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import update

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')  
DB_USER = os.getenv('DB_USER', 'postgres')  
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')  
DB_NAME = os.getenv('DB_NAME', 'capstone')  
database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
db = SQLAlchemy()

'''
setup_db(app)
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://zewbxmiiplimja:cb26dc6425078dadd69f4b76413f3a7f345efb613eb6893a4b57337934ee2cac@ec2-52-23-87-65.compute-1.amazonaws.com:5432/dej3ejogen0c6f'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all

'''

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    
    #TODO
    # Demo row which is helping in POSTMAN test

    movie = Movie(
        title= 'Mr. Bean',
        release_date= "2019-05-21T21:30:00.000Z"
    )

    actor = Actor(
        name='Agust Hellmans',
        age= 23,
        gender= 'M'
    )

    movie_actor = Movie_Actor(
        movie_id= 1,
        actor_id = 1 
    )

    movie.insert()
    actor.insert()
    movie_actor.insert()
    

'''
Movies
a persistent movies entity, extends the base SQLAlchemy Model
'''

class Movie(db.Model):
    __tablename__ = 'movies'

    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), autoincrement=True, primary_key=True)
    # String Title
    title = Column(String(140), nullable=False)
    # Release Date
    release_date = Column(db.DateTime, nullable=False)

    movie_actor = db.relationship('Movie_Actor', backref='movies', lazy=True)
    
    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def __repr__(self):
      return f"<Movie {self.id}>"

    '''
    representation()
    Form representation of the movie model
    '''

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a name and release date
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
    '''

    def update(self):
        db.session.commit()


'''
Actor
a persistent actors entity, extends the base SQLAlchemy Model
'''

class Actor(db.Model):
    __tablename__ = 'actors'
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), autoincrement=True, primary_key=True)
    # String Name
    name = Column(String(150), nullable=False)
    # Age
    age = Column(Integer, nullable=False)
    # Gender
    gender = Column(String(1), nullable=False)

    movie_actor = db.relationship('Movie_Actor', backref='actors', lazy=True)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
      return f"<Actor {self.id}>"

    '''
    representation()
    Form representation of the movie model
    '''

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a name and release date
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
    '''

    def update(self):
        db.session.commit()



class Movie_Actor(db.Model):
    __tablename__ = 'movie_actor'

    movie_id = db.Column(db.Integer, db.ForeignKey(
        'movies.id'), primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey(
        'actors.id'), primary_key=True)

    def __init__(self, actor_id, movie_id):
        self.movie_id = movie_id
        self.actor_id = actor_id

    '''
    representation()
    Form representation of the movie model
    '''
    def format(self):
        return {
            'movie_id': self.movie_id,
            'actor_id': self.actor_id
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a name and release date
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
    '''

    def update(self):
        db.session.commit()