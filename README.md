<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/96/Logo-unet_sin_texto_azul.png">
</p>

# Flask REST API with MongoDB
This is a REST API using python's microframework Flask, and NoSQL database MongoDB with Its mongo Atlas cloud manager. This API provides information of students at UNET, you can also make others CRUD operations like INSERT, PUT, or DELETE, but yow need to create an user and login to use JWT, to more information about this contact repo owner.

## To run this API on your local machine
1- Clone this project, on your local machine:
```bash
$ git clone https://github.com/jefferson10147/unet-api.git
```
2- Create a virtual env inside the folder:
```bash
$ python3 -m venv your_venv
```
3- Activate env:
```bash
$ source your_venv/bin/activate
```
4- Install dependencies:
```bash
$ pip install -r requirements.txt
```
5- Create and export variables to .flaskenv file:
```bash
$ touch .flaskenv
$ echo "FLASK_APP=main.py" > .flaskenv
```
Also you can export another variables to put aplication into development mode:
```bash
$ echo "FLASK_ENV=development" >> .flaskenv
```
6- Create an .env file with these variables
```
secret_key=your_app_secret_key
jwt_secret_key=your_jwt_secret_key
admin_key=your_admin_key
username_from_db=your_mongoDB_username
password_from_db=your_mongoDB_password
database_name=your_mongoDB_database
```
7- Run your app:
```bash
 $ flask run
```
If you are using a local mongo database, you need to edit this variable at app.settings.py:
```python
MONGO_URI = YOUR_MONGO_URI
```
You can check all endpoints when you are running this API on your local machine: [DOCS](https://documenter.getpostman.com/view/8771822/TW77fNue)

## API online

There is an online version of this API currently running at Heroku cloud. Visit [Home page](https://unet-api.herokuapp.com). You can try all search endpoints, but not Insert, Update, and Delete operations. See online documentation at [DOC](https://documenter.getpostman.com/view/8771822/TWDUoxJ2#ac0a8fec-3882-40c9-b923-39e8509137fc)
