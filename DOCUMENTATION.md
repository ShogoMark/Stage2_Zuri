************************************************
A Flask API
************************************************

This is a simple Flask API capable of performing CRUD operations on a resource (e.g., "person").

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


******************************************
PREREQUISITES
******************************************
Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- MySQL or another compatible database server installed
- Python virtual environment (optional but recommended)

********************************************
GETTING STARTED
********************************************

Installation:

1. Clone the repository:

   git clone https://github.com/ShogoMark/Stage2_Zuri.git



2. Navigate to the project directory:
  
   cd Stage2_Zuri



3. Create and activate a python virtual environment(optional but recommended)

	python -m venv venv
	source venv/bin/activate  # On Windows, use `venv\Scripts\activate`



4. Install the required dependencies:
     
 	pip install -r requirements.txt

******************************************************
RUNNING THE API
******************************************************
1. Configure the database connection in 'app.py':
	
	Replace 'username', 'password','localhost', and 'dbname' with your database credentials.


2. Initialize the database:

	Run "python init_db.py"
	The above script will create the necessary database tables.

3. Run the Flask application:

	flask run

	The API should be accessible at `https://localhost:5000`.

*********************************************
API ENDPOINTS
*********************************************

*Create a New Person: `POST /api`
*Get Person by ID: `GET /api/<int:user_id>`
*Get Person dynamically by NAME: `GET /api/person/<string:name>`
*Update Person by ID: `PUT /api/<param>`
*Delete Person by ID: `DELETE /api/<param>`


**********************************************
USAGE
**********************************************

*CREATE A NEW PERSON:
	
	curl -X POST -H "Content-Type: application/json" -d '{"name": "John"}' http://localhost:5000/api
	response: 'Person created successfully'

*GET PERSON BY ID:

	curl http://localhost:5000/api/1
	
	response: {
  "id": 1,
  "name": "John"
}

*GET PERSON DYNAMICALLY BY NAME:

	https://localhost:5000/api/person/John
	
	response: {
  "id": 1,
  "name": "John"
}


*UPDATE PERSON BY ID:

	curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' http://localhost:5000/api/1
	response: 'Person updated successfully'

*DELETE PERSON BY ID:

	curl -X DELETE http://localhost:5000/api/1
	response: 'Person deleted successfully'

******************************************************
CONTRIBUTING
******************************************************

Contributions are welcome! Please fork the repository and create a pull request with your changes.
