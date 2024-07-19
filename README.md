# HeartFailure Project

This project is a Django-based application named "HeartFailure". It includes a command-line utility for performing administrative tasks.

## Requirements

- Python 3.11.5
- Django
- Virtual environment tool (optional but recommended)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/heartfailure.git
   cd heartfailure

2. **Create a virtual environment:**

   It is recommended to use a virtual environment to manage dependencies. If you don't have virtualenv installed, you can install it using pip:

   ```sh
   pip install virtualenv
   ```

   Create and activate a virtual environment:

   ```sh
   virtualenv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the Django application:**

   Make sure to set the `DJANGO_SETTINGS_MODULE` environment variable to point to the correct settings module. This is already handled in the `main` function of the provided script.

   ```sh
   export DJANGO_SETTINGS_MODULE=heartfailure.settings  # On Windows use `set DJANGO_SETTINGS_MODULE=heartfailure.settings`
   ```

5. **Run database migrations:**

   ```sh
   python manage.py migrate
   ```

6. **Create a superuser (optional):**

   ```sh
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

## Usage

The main entry point for administrative tasks is the `manage.py` script. It is used to execute various Django commands such as running the development server, migrating the database, creating a superuser, and more.

### Common Commands

- **Run the development server:**

  ```sh
  python manage.py runserver
  ```

- **Apply database migrations:**

  ```sh
  python manage.py migrate
  ```

- **Create a new app:**

  ```sh
  python manage.py startapp <app_name>
  ```

- **Create a superuser:**

  ```sh
  python manage.py createsuperuser
  ```

## Project Structure

- **heartfailure/**: The main project directory.
- **manage.py**: The command-line utility for administrative tasks.
- **requirements.txt**: A list of Python dependencies.
- **venv/**: The virtual environment directory (if you created one).

## Troubleshooting

### ImportError: Couldn't import Django

If you encounter an `ImportError` stating that Django could not be imported, ensure that you have Django installed and that your virtual environment is activated. You can install Django using:

```sh
pip install django
```

Ensure your virtual environment is activated by running:

```sh
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Further Assistance

For further assistance, you can refer to the official Django documentation: [Django Documentation](https://docs.djangoproject.com/)

## Contributors

<a href="https://github.com/bhushankhopkarr/heart_failure_backend/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=bhushankhopkarr/heart_failure_backend" />
</a>
