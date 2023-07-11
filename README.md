# Food Tracking Application 🍽️

This is a food tracking application built using Django 4, HTML 5, CSS 3, and Bootstrap 5 that uses a MySQL database to store data.

## Table of Contents

- [📦Product Information](#product-information)
- [📊Individual Needs Assessment](#individual-needs-assessment)
- [📈Nutrition Analysis](#nutrition-analysis)
- [💾Installation](#installation)
- [🔴Using VS CODE](#using-vs-code)
- [🔵Using PyCharm](#using-pycharm)
- [🗃️Setting Up a MySQL Database](#setting-up-a-mysql-database)
- [🏃Running the Project](#running-the-project)
- [🌐Viewing the Application](#viewing-the-application)
- [📝Adding Data to the Application](#adding-data-to-the-application)

## 📦Product Information

In database you can store food products, quotes forum posts, pictures for start page. Products are divided into 
categories.

## 📊Individual Needs Assessment

Each one of us is unique in our physical parameters (height, weight, body composition, etc.), 
daily habits, and overall physical activity. This software takes these unique factors into account to 
provide personalized nutritional advice.

## 📈Nutrition Analysis

Our tool offers nutrition analysis based on a balanced diet factor. This can provide valuable insights 
into the aspects to consider when selecting daily food products.

## 💾Installation

Clone the project to your local machine;

```
git clone https://github.com/ZygimantasB/calories_counter.git
```

## 🔴Using VS CODE
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
   On Linux:
```
source venv/bin/activate
```

3. Install required dependencies. From the root directory run:

```
pip install -r requirements.txt
```

## 🔵Using PyCharm
1. Open PyCharm and choose "Open".
2. Navigate to the root directory of your project and click "OK".
3. PyCharm should recognize your Django project and set up everything automatically.
4. You can activate your virtual environment within PyCharm by opening the terminal in PyCharm and typing the 
   5. activation command
   On macOS:
```
source venv/bin/activate
```

   On Windows:
```
venv\scripts\activate
```
   On Linux:
```
source venv/bin/activate
```

5. Once your virtual environment is active, you can run your Django server from PyCharm's terminal using:
```angular2html
python manage.py runserver
```

6. Install required dependencies from the root directory run:

```
pip install -r requirements.txt
```

## 🗃️ Setting Up a MySQL Database

1. Download MySQL Server:

You will need MySQL Server installed and running on your machine. 
If you haven't already installed it, you can download it from [here](https://dev.mysql.com/downloads/). Choose the 
version that matches your operating system (Windows, macOS, Linux, etc.) and your system type (64-bit or 32-bit). 
Download the installer package.

2. Install MySQL Server:

Launch the installer package that you just downloaded. The exact steps will vary depending on your 
operating system, but generally, you will need to accept the license agreement, choose the type of 
installation (for beginners, the standard installation is usually sufficient), and choose the location 
for the installation. The installer may also ask you to set a password for the root user during the installation 
process. Make sure to remember this password as you will need it to administer your MySQL server.

3. Start MySQL Server:

How you start the server depends on your operating system:

- On Windows, you can start the server from the MySQL Server Instance Configuration Wizard, 
which can be found in the MySQL folder in your Start menu.
- On macOS, you can start the server by opening System Preferences, selecting MySQL, 
and then clicking "Start MySQL Server".
- On Linux, you can usually start the server with the following command:

```angular2html
sudo service mysql start
```

4. Access MySQL Server:

Open a terminal or command prompt and enter the following command to access the MySQL server:
    
```angular2html 
mysql -u root -p
```
When prompted, enter the root password that you set during the installation process.

5. Create a MySQL Database:

At the MySQL command prompt, enter the following command to create a new database, replacing 
your_database_name with the name you want to use for your database:
    
```angular2html
CREATE DATABASE your_database_name;
```  

6. Create a new user and grant privileges:

For security reasons, it's a good idea to create a new user that will have access to this database rather 
than using the root user. Run the following commands, replacing your_username and your_password with your 
desired username and password:

```angular2html
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
```

7. Flush privileges to ensure that the privileges table is reloaded by the MySQL server and the 
changes you made will take effect:

```angular2html
FLUSH PRIVILEGES;
```

8. Exit the MySQL command-line client:

Finally, you can exit the MySQL command prompt with the following command:

```angular2html
exit
```

Once you've set up your MySQL server and created your database and user, you will need to update 
your Django settings with the database name, user, and password you just created.

Remember to install the mysqlclient Python package in your virtual environment to interact with MySQL:

```angular2html
pip install mysqlclient
```

Everything is set up for you to run the project, you can install required dependencies from the root directory run:

```
pip install -r requirements.txt
```

Once you've created your database, update the DATABASES setting in your Django 
project's file (env.example.py (remove .example) name should be only .env) with your 
database name, user, and password.

Then you open .env file and change the following lines (your_username, your_password, your_database_name)

```angular2html
DATABASE_USERNAME=your_username
DATABASE_PASSWORD=your_password
DATABASE_NAME=your_database_name
```

## 🏃‍♀️Running the Project

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

## 🌐Viewing the Application

Go to http://127.0.0.1:8000/ to view the application.

## 📝Adding Data to the Application

Add data through Django Admin. Go to http://127.0.0.1:8000/admin to access the Django Admin 
interface and sign in using the admin credentials.