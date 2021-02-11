![](https://upload.wikimedia.org/wikipedia/commons/9/96/Logo-unet_sin_texto_azul.png)
# Flask REST API with MongoDB
This is a REST API using python's microframework Flask, and NoSQL database MongoDB with Its mongo Atlas cloud manager. This API provides information of students at UNET, you can also make others CRUD operations like INSERT, PUT, or DELETE, but yow need to create an user and login to use JWT, to more information about this contact repo owner.

## To run this API on your local machine
1- Clone this project, on your machine:
```bash
$ git clone https://github.com/jefferson10147/unet-api.git
```
2- Create a virtual env inside the folder:
```bash
$ python3 -m venv your_venv
```
3- Activate env:
```bash
$ source your_env/bin/activate
```
4- Install dependencies:
```bash
$ pip install -r requirements.txt
```
5- Export variables to run flask:
```bash
$ export FLASK_APP=main.py
```
Also you can export another variables to put aplication into development mode:
```bash
$ export FLASK_ENV=development
```
6- Create an .env file with these variables
```
secret_key=your_app_secret_key
jwt_secret_key=your_jwt_secret_key
auth_key=your_auth_key
username_from_db=your_mongoDB_username
password_from_db=your_mongoDB_password
database_name=your_mongoDB_database
```
7- Run your app:
```bash
 $ flask run
```
If you are using a local mongo database, you need to edit this variable at app.settings.py
```python
MONGO_URI = YOUR_MONGO_URI
```

