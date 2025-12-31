
### A simple Expense Management REST API built using Django REST Framework to manage expenses categorized by type.
 This project focuses on foreign key relationships, clean serialization, and CRUD fundamentals.

## Techstack: 
Python,Django,DjangoRestFramework, sqlite3

## Getting Started:
__Step 1:__ Clone the repository: 
```
git clone https://github.com/PratikG345/Expenses_api.git
```

__Step 2:__ Create virtual environment by using 
```
py -m venv env
```

__Step 3:__ Activate the virtual environment by 
```
env/Scripts/activate
```
__Step 4:__ navigate to project 
```
cd expense
```
__Step 5:__ run on local server 
```
python3 manage.py runserver
```
## API Endpoints: 
1. __GET expenses/__ - list all expenses
2. __POST expenses/add/__ - add a expense
3. __GET expenses/{id}/__ - Retrive details of expense
4. __PUT expenses/{id}/__ - Update a expense
5. __DELETE expenses/{id}/__ - Delete a expense

## Project Scope
1. This project was designed to strengthen core backend concepts:
2. Modeling one-to-many relationships using ForeignKey
3. Implementing CRUD APIs using function-based views
4. Controlling API representation using serializers
5. Practicing clean separation between models, serializers, and views

Advanced features like authentication or analytics were intentionally excluded.

No authentication or advanced features were added by design.
