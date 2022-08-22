from model import Person
# from flask import Flask, render_template, request

def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))
    for item in data:
        print(item.name())


def start_view():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')


def end_view():
    print('Goodbye!')

def Menu():
    print('\nOpciones:')
    print('A - Actualizar')
    print('B - Eliminar')
    print('C - terminar')