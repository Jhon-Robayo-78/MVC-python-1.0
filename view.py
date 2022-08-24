from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
peopleList = []
# lista de objetos

def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))
    for item in data:

        peopleList.append(item)
        print(item.name()) # vista por consola


def start_view():
    app.run(debug=True, port=8000)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/people')
def view_list_web():
    print('Mostrando lista en web')

    return render_template('people.html', value=peopleList)

@app.route('/person_update/<int:ID>')
def update(ID):
    for UserID in peopleList:
        if int(UserID.id) == ID:
            print('user before change\n', 'id:', UserID.id, 'name:', UserID.first_name, 'last name:', UserID.last_name)
            return render_template('update_user.html', value = UserID)

@app.route('/person')
def Insert():
    # formulario de usuario para insertar
    return render_template('formInsert.html', value = len(peopleList))