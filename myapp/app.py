import flask

from Alumnos.routes import alumnos
from Maestros.routes import maestros
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from config import DevelopmentConfig
from flask import jsonify
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos, Maestros
from sqlalchemy import text

app = flask.Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['DEBUG']=True
csrf = CSRFProtect()

@app.route("/", methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            )
        db.session.execute(text("CALL agrega_alumno(:nombre, :apellidos, :email)"), 
                           {'nombre': alum.nombre, 'apellidos': alum.apellidos, 'email': alum.email})
        db.session.commit()
        
    return render_template('index.html', form=create_form)

@app.route("/maestros", methods=['GET', 'POST'])
def indexM():
    create_form = forms.TeacherForm(request.form)
    if request.method == 'POST':
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data,
            materia=create_form.materia.data

            )
        db.session.execute(text("CALL agrega_maestro(:nombre, :apellidos, :email, :telefono, :materia)"), 
                           {'nombre': maes.nombre, 'apellidos': maes.apellidos, 'email': maes.email, 'telefono':maes.telefono, 'materia': maes.materia})
        db.session.commit()
        
    return render_template('indexM.html', form=create_form) 

@app.route("/ABCompleto", methods=['GET', 'POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    #SELECT * FROM alumnos
    alumnos = db.session.execute(text('CALL consultar_alumnos();'))
    return render_template('ABCompleto.html', form=create_form, alumnos=alumnos)

@app.route("/MBCompleto", methods=['GET', 'POST'])
def MBCompleto():
    create_form = forms.TeacherForm(request.form)
    #SELECT * FROM maestros
    maestros = db.session.execute(text('CALL consultar_maestros();'))
    return render_template('MBCompleto.html', form=create_form, maestros=maestros)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        db.session.execute(text("CALL actualizar_alumno(:id, :n_nombre, :n_apellidos, :n_email)"), 
                        {'id': id, 'n_nombre': alum.nombre, 'n_apellidos': alum.apellidos, 'n_email': alum.email})
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html', form=create_form)

@app.route("/modificarM", methods=['GET', 'POST'])
def modificarM():
    create_form = forms.TeacherForm(request.form)
    if request.method == 'GET':
        idM = request.args.get('id')
        maes1 = db.session.query(Maestros).filter(Maestros.idM==idM).first()
        create_form.idM.data = maes1.idM
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.email.data = maes1.email
        create_form.telefono.data = maes1.telefono
        create_form.materia.data = maes1.materia
        
    if request.method == 'POST':
        idM = create_form.idM.data
        maes = db.session.query(Maestros).filter(Maestros.idM==idM).first()
        maes.nombre = create_form.nombre.data
        maes.apellidos = create_form.apellidos.data
        maes.email = create_form.email.data
        maes.telefono = create_form.telefono.data
        maes.materia = create_form.materia.data
        db.session.execute(text("CALL actualizar_maestro(:idM, :n_nombre, :n_apellidos, :n_email, :n_telefono, :n_materia)"), 
                        {'idM': idM, 'n_nombre': maes.nombre, 'n_apellidos': maes.apellidos, 'n_email': maes.email,
                         'n_telefono': maes.telefono, 'n_materia': maes.materia})
        db.session.commit()
        return redirect(url_for('MBCompleto'))
    return render_template('modificarM.html', form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        db.session.execute(text("CALL eliminar_alumno(:ida)"), {'ida': id})
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('eliminar.html', form=create_form)


@app.route("/eliminarM", methods=['GET', 'POST'])
def eliminarM():
    create_form = forms.TeacherForm(request.form)
    if request.method == 'GET':
        idM = request.args.get('id')
        maes1 = db.session.query(Maestros).filter(Maestros.idM==idM).first()
        create_form.idM.data = maes1.idM
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.email.data = maes1.email
        create_form.telefono.data = maes1.telefono
        create_form.materia.data = maes1.materia
        
    if request.method == 'POST':
        idM = create_form.idM.data
        maes = db.session.query(Maestros).filter(Maestros.idM==idM).first()
        db.session.execute(text("CALL eliminar_maestro(:id)"), {'id': idM})
        db.session.commit()
        return redirect(url_for('MBCompleto'))
    return render_template('eliminarM.html', form=create_form)


@app.route("/", methods=['GET'])
def home():
    return flask.jsonify({'Datos':'Home'})

app.register_blueprint(alumnos)
app.register_blueprint(maestros)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)