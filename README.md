# Backend-Test-Ramirez
The current process consist of a person (Nora) sending a text message via Whatsapp to all the chilean employees, the message contains today's menu with the different alternatives for lunch. 

# For run the project, you need write then the next in yours terminal:

- $ git clone https://github.com/elPintozo/Backend-Test-Ramirez.git
- $ python manage.py pip install -r requiredments.txt
- $ python manage.py makemigrations
- $ python manage.py migrate

you can load data for open the web with information

- $ python3 manage.py loaddata ingredients_03112020.json
- $ python3 manage.py loaddata employees_06112020.json.json

and then you need create a superuser (Nora) 

- $ python manage.py createsuperuser
    - $ put your name
    - $ put your email
    - $ put your password
    - $ put your password again
    
and finaly

- $ python manage.py runserver

# Functions ok
- Nora can create ingredients
- Nora can create menus
- Nora can add ingredients to the plate any menu
- Employees can look the plates of menu
- Employees can specific yours preferens

# Pendient functions 

- Send a text message via Whatsapp to all the chilean employees
- Send a Slack reminder with today's menu to all chilean employees