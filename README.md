# Employee CRUD
This repository contains the source code for a Django web application that manages employee data. It provides endpoints for adding, updating, and deleting employee records.

#### Features
- Add Employee: Allows users to add new employee records using a form.
- View Employee List: Displays a list of all employees with their details.
- Update Employee: Allows users to update employee details.
- Delete Employee: Enables the deletion of employee records.
#### Installation
Clone the repository:
```
git clone <repository-url>
```
Install dependencies:
```
pip install -r requirements.txt
```
Apply migrations:
```
python manage.py migrate
```
Start the development server:
```
python manage.py runserver
```
Usage
#### Add Employee:
Navigate to /add to add a new employee record using the provided form.
#### View Employee List:
Navigate to /list to view a list of all employees and their details.
#### Update Employee:
Click on the "Update" button next to an employee record in the employee list to update their details.
#### Delete Employee:
Click on the "Delete" button next to an employee record in the employee list to delete the record.
#### API Endpoints
- GET /employees/<id>/:
***Retrieves details of a specific employee by ID.***
- POST /employees/:
***Adds a new employee record.***
- DELETE /employees/:
***Deletes an employee record by email.***
- GET /list/:
***Retrieves a list of all employees.***
- PUT /employees/:
***Updates an existing employee record.***
