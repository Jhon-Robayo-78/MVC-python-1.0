import json
class Person(object):

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    # returns Person name, ex: John Doe
    def name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @classmethod
    # returns all people inside db.txt as list of Person objects
    def get_all(cls):
        result = list()
        with open('db.json') as json_file:
            data = json.load(json_file)
            for p in data['employees']:
                person = Person(p['first_name'], p['last_name'])
                result.append(person)
        return result

    def update(name, lastname):
        with open('db.json') as json_file:
            data = json.load(json_file)
            for p in data['employees']:
                if p['first_name'] == name and p['last_name'] == lastname:
                    print(True, 'si actualizar')
                    print('1 - nombre \n2 - apellido \n0 - terminar \nDigite la opcion:')
                    val = input()
                    if val == '1':
                        print('digite nombre:')
                        New_name = input()
                        p['first_name']=New_name
                    elif val == '2':
                        print('digite apellido:')
                        New_Lastname = input()
                        p['last_name']=New_Lastname
            with open('db.json','w') as JSON_NEW:
                json.dump(data, JSON_NEW, indent=4, ensure_ascii=False)
        print(name, lastname)
        print(data)

    def deleteUser(name, lastname):
        with open('db.json') as json_file:
            data = json.load(json_file)
            i = 0
            for p in data['employees']:
                if p['first_name'] == name and p['last_name'] == lastname:
                    del data['employees'][i]
                    print('!!!!!!ELIMINADO!!!!!!!')
                i = i + 1
            print(data)
            with open('db2.json', 'w') as JSON_NEW:
                json.dump(data, JSON_NEW, indent=4, ensure_ascii=False)