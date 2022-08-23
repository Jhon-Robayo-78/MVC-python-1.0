from past.builtins import raw_input
# from flask import Flask, render_template, request
import model
from model import Person
import view


# app = Flask(__name__)
def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    return view.show_all_view(people_in_db)


def start():
    show_all()
    view.start_view()


# Funciones para recoleccion de datos y acceso a los metodos de actualizar y eliminar en db.json
def InputDataU():
    print('Digite en mayusculas')
    print('Nombre y la letra inicial del segundo nombre:')
    Name = raw_input()
    print('Escriba los dos Apellidos:')
    LastName = raw_input()
    model.Person.update(Name, LastName)


def DeleteDataU():
    print('Digite en mayusculas')
    print('Nombre y la letra inicial del segundo nombre:')
    Name = raw_input()
    print('Escriba los dos Apellidos:')
    LastName = raw_input()
    model.Person.deleteUser(Name, LastName)


if __name__ == "__main__":
    # running controller function
    start()
