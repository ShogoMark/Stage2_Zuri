import unittest
import json
from app import app, db, Person

class FlaskApiTestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:adminPass@localhost/test_persons'
        app.config['TESTING'] = True
        self.app = app.test_client()


        app.app_context().push()
        db.create_all()

    def tearDown(self):
        db.drop_all()

        app.app_context().pop()

    def test_create_person(self):
        data = {'name': 'John Doe'}
        response = self.app.post('/api', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['message'], 'Person created successfully')

    def test_get_person_by_name(self):
        person = Person(name='John Doe')
        db.session.add(person)
        db.session.commit()

        response = self.app.get(f'/api/{person.name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['name'], person.name)

    def test_get_person_by_id(self):
        person = Person(name='John Doe')
        db.session.add(person)
        db.session.commit()

        response = self.app.get(f'/api/{person.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['id'], person.id)

    def test_update_person(self):
        person = Person(name='John Doe')
        db.session.add(person)
        db.session.commit()

        data = {'name': 'Jane Doe'}
        response = self.app.put(f'/api/{person.id}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'Person updated successfully')

        updated_person = Person.query.get(person.id)
        self.assertEqual(updated_person.name, 'Jane Doe')

    def test_delete_person(self):
        person = Person(name='John Doe')
        db.session.add(person)
        db.session.commit()

        response = self.app.delete(f'/api/{person.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], 'Person deleted successfully')

        deleted_person = Person.query.get(person.id)
        self.assertIsNone(deleted_person)

if __name__ == '__main__':
    unittest.main()

