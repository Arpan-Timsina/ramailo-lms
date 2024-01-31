
# Ramailo Library Mangment System

The Library Management System is a web application built using Django, a high-level Python web framework, and PostgreSQL as the backend database. It provides a platform for managing books, library users, and borrowed books, facilitating efficient library operations.



## Installation Guide

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd library-management-system
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the Django admin interface at `http://127.0.0.1:8000/admin/` and log in using the superuser credentials created earlier.

8. Find the API REFERENCE & Documentation on /swagger endpoint.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET KEY`


`DB_HOST`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

