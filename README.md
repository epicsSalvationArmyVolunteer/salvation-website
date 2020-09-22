# salvation-website
The Salvation Army Volunteer Tracking Website directory. This package contains the files for Django Package, HTML/CSS Views,
and SQL database.
The volunteerEPICS directory contains the Django project for the Salvation Army Server.


## Development Environment Installation Guide
This guide assumes you are using some version of Linux as a development environment. 
It was developed on Windows Subsystem for Linux 2, running Ubuntu 18.04 LTS. 

### Prerequisites

#### Python installation

#### Django Installation

#### MariaDB Installation
Update the server: 
~~~
$ sudo apt update && sudo apt upgrade -y
~~~

Install MariaDB:
~~~
$ sudo apt install mariadb-server libmariadbclient-dev libssl-dev
~~~

Choose a secure administrative password, you will need it for the next step.

Run the MariaDB secure installation script:
~~~
$ sudo mysql_secure_installation
~~~
Answer yes to every question that does not ask you to choose a new password.

MariaDB is now installed, and should be started. Login to the MariaDB server as the root user using the previously created administrative password:
~~~
$ sudo mysql -u root -p
~~~
If the server is not started, start it now, then attempt to login again:
~~~
$ sudo service mysql start
~~~

Create a new database for the app named volunteer_app
~~~
> CREATE DATABASE volunter_app CHARACTER SET UTF8;
~~~

Create a new user named 'django' with secure password \<password\> and grant it all privileges on volunteer_app:
~~~
> CREATE USER django@localhost IDENTIFIED BY <password>;
> GRANT ALL PRIVILEGES ON volunteer_app.* TO django@localhost;
~~~

Flush privileges so they are available during the current session, then exit the MariaDB server.
It will continue to run in the background.
~~~
> FLUSH PRIVILEGES;
> exit
~~~

### Installing/Running the Volunteer Tracking app
Install git (if not already installed)
~~~
$ sudo apt install git
~~~

Create a new directory \<VolApp\>
~~~
$ mkdir <VolApp>
~~~

Navigate to the new directory
~~~
$ cd <VolApp>
~~~

Clone git repository
~~~
$ git clone https://github.com/asibarr2/salvation-website.git
~~~

Navigate to the app directory
~~~
$ cd volunteerEPICS/
~~~
Make migrations and migrate before continuing

Run the application server
~~~
$ python3 manage.py runserver
~~~


The application should now be running. 
Go to the web address created earlier (WHERE IS THIS CREATED?) to test and use the application.
Please direct any questions to (PERSON IN CHARGE OF ANSWEREING QUESTIONS)