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

### Installing/Running the Volunteer Tracking app
Install git (if not already installed)
_sudo apt install git_

Create a new directory <VolApp>
_mkdir <VolApp>_

Navigate to the new directory
_cd <VolApp>_

Clone git repository
_git clone https://github.com/asibarr2/salvation-website.git_

Navigate to the app directory
_cd volunteerEPICS/_

Make migrations and migrate before continuing

Run the application server
_python3 manage.py runserver_
