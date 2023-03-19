from flask_sqlalchemy import SQLAlchemy

import datetime

db=SQLAlchemy()

class Alumnos(db.Model):
    _tablename_='alumnos'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apellidos=db.Column(db.String(100))
    email=db.Column(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)

class Maestros(db.Model):
    _tablename_='maestros'
    idM=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apellidos=db.Column(db.String(100))
    email=db.Column(db.String(50))
    telefono=db.Column(db.String(50))
    materia=db.Column(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)