import os
commands = ["pip install -r requirements.txt",
	"python manage.py makemigrations",
	"python manage.py migrate",
	"python manage.py runserver",
#"gunicorn --bind 0.0.0.0:8000 leavemanagement.wsgi --workers=10",
	]
for cmd in commands:
	os.system(cmd)
