# Food Tracking Application

This is a food tracking application built using Django 4, HTML 5, CSS 3, and Bootstrap 5 that uses a MySQL database to store data.

## Product Information

Our database currently holds over 8,000 entries for food products. Each product is described according to 40+ nutritional elements, ranging from caloric value (kcal).

## Individual Needs Assessment

Each one of us is unique in our physical parameters (height, weight, body composition, etc.), daily habits, and overall physical activity. This software takes these unique factors into account to provide personalized nutritional advice.

## Nutrition Analysis

Our tool offers nutrition analysis based on a balanced diet factor. This can provide valuable insights into the aspects to consider when selecting daily food products.

## Installation

Clone the project to your local machine;

```bash
git clone https://github.com/ZygimantasB/calories_counter.git
Using VS CODE
Create a virtual environment
From the root directory run:

python -m venv venv
Activate the virtual environment
From the root directory run:
On macOS:

source venv/bin/activate
On Windows:

venv\scripts\activate
Install required dependencies
From the root directory run:

pip install -r requirements.txt
Using the Project in PyCharm
PyCharm is a popular IDE for Python development and it works great with Django and MySQL.

Open PyCharm and choose "Open".
Navigate to the root directory of your project and click "OK".
PyCharm should recognize your Django project and set up everything automatically.
You can activate your virtual environment within PyCharm by opening the terminal in PyCharm and typing the activation command (source venv/bin/activate for macOS, venv\scripts\activate for Windows).
Once your virtual environment is active, you can run your Django server from PyCharm's terminal using python manage.py runserver.
Install required dependencies from the root directory run:

pip install -r requirements.txt
Setting Up a MySQL Database
You will need MySQL Server installed and running on your machine. If you haven't already installed it, you can download it from here.

To setup a MySQL database:

Open the MySQL command-line client or MySQL Workbench on your machine.
Log in to the MySQL server as the root user or another user with sufficient permissions to create databases.
To create a new database, run the following command, replacing your_database_name with the name you want to use for the database:

CREATE DATABASE your_database_name;
You will also need to create a new user and grant them all privileges on your new database. To do this, run the following commands, replacing your_username and your_password with your desired username and password:

CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
Once you've created your database, update the DATABASES setting in your Django project's settings file (env.exmaple.py(remove.exmaple)) with your database name, user, and password.

Running the Project
Run migrations
From the root directory run:

python manage.py makemigrations
python manage.py migrate
Create an admin user to access the Django Admin interface
From the root directory run:

python manage.py createsuperuser
When prompted, enter a username, email, and password.

Run the application
From the root directory run:

python manage.py runserver
Viewing the Application
Go to http://127.0.0.1:8000/ to view the application.

Adding Data to the Application
Add data through Django Admin. Go to http://127.0.0.1:8000/admin to access the Django Admin interface and sign in using the admin credentials.