from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:adminPass@localhost/persons'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name


# create a new person
@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()

    # validate the 'name' field to ensure it's a string
    if 'name' not in data or not isinstance(data['name'], str):
        return jsonify({'message': 'Name must be a string'}), 400
    
    # create the new person
    new_person = Person(name=data['name'])
    db.session.add(new_person)
    db.session.commit()

    return jsonify({'message': 'Person created successfully'}), 201


# handle dynamic parameter
@app.route('/api/person/<string:name>', methods=['GET'])
def get_person_by_name(name):
    person = Person.query.filter_by(name=name).first()

    if person:
        person_data = {
            'id': person.id,
            'name': person.name
        }
        return jsonify(person_data)
    else:
        return jsonify({'message': 'Person not found'}), 404


# read person by id
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get_or_404(user_id)
    return jsonify({
        'id': person.id,
        'name': person.name
    })


# update details of an existing person by user_id
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    person = Person.query.get_or_404(user_id)
    data = request.get_json()
    person.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'})


# delete a person by user_id
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get_or_404(user_id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
