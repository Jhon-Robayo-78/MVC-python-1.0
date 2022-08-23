from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
dataList = []
peopleList = []


def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))

    for item in data:
        dataList.append(item.name())
        peopleList.append(item)
        print(item.name())


def start_view():
    app.run(debug=True, port=8000)


@app.route('/')
def inicio():
    # controller.show_all()
    return render_template('index.html')


@app.route('/people')
def view_list_web():
    print('Mostrando lista en web')

    return render_template('people.html', value=peopleList)
