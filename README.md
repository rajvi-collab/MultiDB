# Django Multiple Database
Configuring Multiple Databases in Django.

## Setting Up the Project
* Firstly clone the project
```
git clone 
```
* Navigate inside the Multi_DB_Router folder
```
cd Multi_DB_Router/
```
* Install all the dependencies required for the project
```
pip install -r requirements.txt
```

## Database Setup
The project Postgresql and MySQL as backend databases.

### Postgresql Database Setup
The data of the User app is being saved in the postgresql database. Other 4 database is used to save the product details.

#### Creation of Databases in Postgresql and Mysql
* For creating the database, open psql by executing the following commands
```
sudo -u postgres psql
```
* Now create a new database named as `form`
```
postgres=# create database database_1;
```
```
postgres=# create database database_2;
```

### MySQL Database Setup
```
mysql -uroot -proot
```
* Now create a new database named as `form`
```
postgres=# create database database_3;
```
```
postgres=# create database database_4;
```
```
postgres=# create database database_5;
```
* The default database setup is in .env file for Postgresql and mysql. You can update your database username and password in .env file

## Run the Project

After setting up both the databases run the migrations

* Run the migrations for the postgresql database for User Database
```
python manage.py migrate
```
* Run the migrations for the Second postgresql database for Product
```
python manage.py migrate --database=data1_db
```
* Run the migrations for the Mysql database for Product
```
python manage.py migrate --database=data2_db
```
* Run the migrations for the Mysql database for Product
```
python manage.py migrate --database=data3_db
```
* Run the migrations for the Mysql database for Product
```
python manage.py migrate --database=data4_db
```
* Now run the server by using
```
python manage.py runserver
```
* Create admin account by running this command
```
python manage.py createsuperuser
```
* Hit the URL, Both admin and User can login with this url:
```
http://127.0.0.1:8000/
```