# from model import Person
from flask import Flask, render_template, request
import controller

app = Flask(__name__)
dataList = []
def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))

    for item in data:
        dataList.append(item.name())
        print(item.name())

@app.route('/')
def inicio():
    #controller.show_all()
    return render_template('HOME.html')
def start_view():
    app.run(debug=True, port=8000)

@app.route('/List')
def view_list_web():
    print('Mostrando lista en web')
    return render_template('ListPerson.html', value=dataList)

