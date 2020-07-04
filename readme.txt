1)create project directory
  cd projectname
2)change the directory to project directory
3)create virtual environment using below command.
  python -m venv venv
4)Activate virtual environment
  source venv/bin/activate
5)check pip installed or not
  pip -V
6)install Django
  python -m pip install Django
7)verify installed Django
  python
  import django
  print(django.get_version())
8)write your first django application
  django-admin startproject myskillup
9)Run Development Server
  python myskillup/manage.py runserver
10)open the link