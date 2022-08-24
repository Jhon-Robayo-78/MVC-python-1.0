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

    def add_to_db(self):
        with open('db.json') as json_file:
            data = json.load(json_file)
            data['employees'].append({'id': int(self.id), 'first_name': str(self.first_name), 'last_name': str(self.last_name)})
            with open('db.json', 'w') as JSON_NEW:
                json.dump(data, JSON_NEW, indent=0, ensure_ascii=False)




    def update(self):
        with open('db.json') as json_file:
            data = json.load(json_file)
            for p in data['employees']:
                if p['id'] == int(self.id):
                    print(p['id'] is int(self.id)) # validacion de datos
                    p['first_name'] = self.first_name
                    p['last_name'] = self.last_name
            with open('db.json', 'w') as JSON_NEW:
                json.dump(data, JSON_NEW, indent=0, ensure_ascii=False)
        print('\n', data) # vista db.json actualizada
        print('\nUpdated User\n', 'ID:', self.id, 'name:', self.first_name, 'last name:', self.last_name)

    def deleteUser(self):
        #print(self.id, self.first_name, self.last_name)
        with open('db.json') as json_file:
            data = json.load(json_file)
            i = 0
            for p in data['employees']:
                if p['id'] == int(self.id):
                    del data['employees'][i]
                i = i + 1
            print(data)
            with open('db.json', 'w') as JSON_NEW:
                json.dump(data, JSON_NEW, indent=4, ensure_ascii=False)
