# HomeSchool-Connections

Depending on your operating system, you can do a 
```
git clone https://github.com/flyboy1565/HomeSchool-Connections.git
```
to pull down the repo. Once you have the package you'll want to get into the base directory then you can do the following. 
This has been written to allow you to use pip to install all the python related packages so you'll need to do this.
*I highly recommend a virtual environment, either python3 -m venv or pyenv*
```
pip install -r requirements.txt
```
Once Django and other packages are installed, you'll do the following.
```
python manage.py migrate
```
This will create a database.
Next you'll want to create a superuser with the following command.
```
python manage.py createsuperuser
```

Once you've completed this, you can start up the Django Development server
```
python manage.py runserver
```
This will make it so you can now navigate to http://127.0.0.1:8000/. 
