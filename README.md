# Pylot MVC (beta)
Pylot MVC is a lightweight MVC framework built in Python leveraging flask.

This framework is currently still in development. If you want to play around with it read on or clone the stable version!

# Installation

First make sure you have pip installed. If you don't have it installed there are great instructions here: https://pip.pypa.io/en/latest/installing.html

Next install virtualenv
```
sudo pip install virtualenv
```

Clone the project
```
git clone https://github.com/christ-huytran/Courses-Pylot-Demo.git
```

cd into the project and source the setup file
```
cd Pylot
. setup
```

Start MAMP, open MySQLWorkBench and generate the required schema with the script in courses.sql. You can view the ERD by looking at courses.mwb.

Now you can start your development server like so:
```
python manage.py runserver
```

Enjoy! More details/features coming soon!
