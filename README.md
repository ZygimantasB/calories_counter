# Food Tracking Application

This is a food tracking application built using Django 4, HTML 5, CSS 3, and Bootstrap 5 that uses a MySQL database to store data.

## Table of Contents

- [Product Information](#product-information)
- [Individual Needs Assessment](#individual-needs-assessment)
- [Nutrition Analysis](#nutrition-analysis)
- [Installation](#installation)
- [Using VS CODE](#using-vs-code)
- [Using PyCharm](#using-pycharm)
- [Setting Up a MySQL Database](#setting-up-a-mysql-database)
- [Running the Project](#running-the-project)
- [Viewing the Application](#viewing-the-application)
- [Adding Data to the Application](#adding-data-to-the-application)

## Product Information

Our database currently holds over 8,000 entries for food products. Each product is described according to 40+ nutritional elements, ranging from caloric value (kcal).

## Individual Needs Assessment

Each one of us is unique in our physical parameters (height, weight, body composition, etc.), daily habits, and overall physical activity. This software takes these unique factors into account to provide personalized nutritional advice.

## Nutrition Analysis

Our tool offers nutrition analysis based on a balanced diet factor. This can provide valuable insights into the aspects to consider when selecting daily food products.

## Installation

Clone the project to your local machine;

```
git clone https://github.com/ZygimantasB/calories_counter.git
```

## Using VS CODE

1. Create a virtual environment. From the root directory run:
````
python -m venv venv
````

2. Activate the virtual environment. From the root directory run:<br>
On macOS:
```
source venv/bin/activate
```

On Windows:
```
venv\scripts\activate
```

3. Install required dependencies. From the root directory run:

```
pip install -r requirements.txt
```

## Using PyCharm

1. Open PyCharm and choose "Open".
2. Navigate to the root directory of your project and click "OK".
3. PyCharm should recognize your Django project and set up everything automatically.
4. You can activate your virtual environment within PyCharm by opening the terminal in PyCharm and typing the activation command:<br>
(source venv/bin/activate for macOS, venv\scripts\activate for Windows).
5. Once your virtual environment is active, you can run your Django server from PyCharm's terminal using python manage.py runserver.
6. Install required dependencies from the root directory run:

```
pip install -r requirements.txt
```

## Setting Up a MySQL Database

You will need MySQL Server installed and running on your machine. 
If you haven't already installed it, you can download it from here.

To setup a MySQL database:

1. Open the MySQL command-line client or MySQL Workbench on your machine.
2. Log in to the MySQL server as the root user or another user with sufficient permissions to create databases.
3. To create a new database, run the following command, replacing your_database_name with the name you want to use 
for the database:

```
CREATE DATABASE your_database_name;
```

4. You will also need to create a new user and grant them all privileges 
on your new database. To do this, run the following commands, 
replacing your_username and your_password with your desired 
username and password:
    
```
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
```

Once you've created your database, update the DATABASES setting in your Django 
project's settings file(env.exmaple.py(remove.exmaple)) with your 
database name, user, and password.

## Running the Project

1. Run migrations
   From the root directory run:

```angular2html
python manage.py makemigrations
python manage.py migrate
```

2. Create an admin user to access the Django Admin interface
   From the root directory run:

```
python manage.py createsuperuser
```
When prompted, enter a username, email, and password.

3. Run the application
   From the root directory run:
```angular2html
python manage.py runserver
```

## Viewing the Application

Go to http://127.0.0.1:8000/ to view the application.

## Adding Data to the Application

Add data through Django Admin. Go to http://127.0.0.1:8000/admin to access the Django Admin 
interface and sign in using the admin credentials.