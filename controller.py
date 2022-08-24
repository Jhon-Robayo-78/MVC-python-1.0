from flask import request, render_template
import model
from model import Person
import view
from view import app, peopleList

def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    return view.show_all_view(people_in_db)


def start():
    show_all()
    view.start_view()
    # llamado para iniciar el servidor


# Funciones para recoleccion de datos y acceso a los metodos de actualizar y eliminar en db.json
@app.route('/dataUpdate', methods=['POST'])
def InputDataU():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    model.Person.update(Person(id_person, first_name, last_name))
    peopleList.clear()
    # limpieza de la lista para ver cambios
    show_all()
    return render_template('index.html')

@app.route('/person_delete/<int:ID>')
def DeleteDataU(ID):
    for UserID in peopleList:
        if int(UserID.id) == ID:
            print('REMOVED:', 'id:', UserID.id, 'name:', UserID.first_name, 'last name:', UserID.last_name, '\n')
            model.Person.deleteUser(UserID)
            peopleList.clear()
            # limpieza de la lista para ver cambios
            show_all()
    return render_template('index.html')

@app.route('/InsertData', methods=['POST'])
def InsertNew():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person, first_name, last_name)
    model.Person.add_to_db(p)
    peopleList.clear()
    # limpieza de la lista para ver cambios
    show_all()
    return render_template('index.html')

if __name__ == "__main__":
    # running controller function
    start()
