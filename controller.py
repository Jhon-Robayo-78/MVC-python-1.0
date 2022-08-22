from past.builtins import raw_input

import model
from model import Person
import view


def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    return view.show_all_view(people_in_db)


def start():
    view.start_view()
    input = raw_input()
    if input == 'y':
        return show_all()
    else:
        return view.end_view()

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
    val = True
    while val:
        view.Menu()
        selector = raw_input()
        if selector == 'A' or selector == 'a':
            InputDataU()
        elif selector == 'B' or selector == 'b':
            DeleteDataU()

        elif selector == 'C' or selector == 'c':
            view.end_view()
            val = False
        else:
            view.end_view()
            val = False