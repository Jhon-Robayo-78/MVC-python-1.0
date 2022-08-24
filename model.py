import json


class Person(object):

    def __init__(self, id, first_name=None, last_name=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    # returns Person name, ex: John Doe
    def name(self):
        return "{0} {1} {2}".format(self.id, self.first_name, self.last_name)

    @classmethod
    # returns all people inside db.txt as list of Person objects
    def get_all(cls):
        result = list()
        with open('db.json') as json_file:
            data = json.load(json_file)
            for p in data['employees']:
                person = Person(p['id'], p['first_name'], p['last_name'])
                result.append(person)
        return result

    def update(self, lastname):
        with open('db.json') as json_file:
            data = json.load(json_file)
            for p in data['employees']:
                if p['first_name'] == self and p['last_name'] == lastname:
                    print(True, 'si actualizar')
                    print('1 - nombre \n2 - apellido \n0 - terminar \nDigite la opcion:')
                    val = input()
                    if val == '1':
                        print('digite nombre:')
                        new_name = input()
                        p['first_name'] = new_name
                    elif val == '2':
                        print('digite apellido:')
                        new_lastname = input()
                        p['last_name'] = new_lastname
            with open('db.json', 'w') as JSON_NEW:
                json.dump(data, JSON_NEW, indent=4, ensure_ascii=False)
        print(self, lastname)
        print(data)

    def deleteUser(self, lastname):
        with open('db.json') as json_file:
            data = json.load(json_file)
            i = 0
            for p in data['employees']:
                if p['first_name'] == self and p['last_name'] == lastname:
                    del data['employees'][i]
                    print('!!!!!!ELIMINADO!!!!!!!')
                i = i + 1
            print(data)
            with open('db2.json', 'w') as JSON_NEW:
                json.dump(data, JSON_NEW, indent=4, ensure_ascii=False)
