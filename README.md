# growthX
assignment-portal


### Local Setup Guide
1. Install Softwares: 
    1. Python 
    2. mongodbcompass
    3. Visual Studio Code editor
    4. Postman
2. Clone the repository using the the following command: git clone ['https://github.com/ramadevi2001/growthX.git']

3. Virtual Enviroment and package installation
   1. create virtual environment using the command `python -m venv venv`
   2. activate virtual environment using the command `.\venv\Scripts\activate` for windows, for mac and linux using the command `source venv/bin/activate`
   3. install the packages using the command `pip install -r requirements.txt`

4. Setup Database :
    1. create database using the mongodb 
    2. In the code go to setttings.py 
    we are using the Nosql database, so we are not using the default database in the settings, we have to use the mongoengine like this 
    "from mongoengine import connect
connect(
    db='assignment_portal_db',
    host='localhost',
    port=27017
)"# with your created database name
    


4. Migrations and creating the collections in database
   1. please make sure your database connections one more time
   2. change to project directory using the command `cd assignment_portal`
   3. run the command for makign the migrations `python manage.py makemigrations`
   4. run the command for migrting and making the database connections `python manage.py migrate`
5. Running the server and checking the APIS
   1. By the step above create all the connections required, now run the application or server using the command `python manage.py runserver`
   2. Go the postman import this collection [https://api.postman.com/collections/34747528-14531f1c-b3a6-4a8c-92af-d22df0509cd3?access_key=PMAT-01J9X61J0XS7MTRCFRZYW2HXY5]
   3. create enviroment postman with variables BaseUrl as `http://127.0.0.1:8000`, token value you can steup when you logged in

   4. call the create API You will get the result following image![image](https://github.com/user-attachments/assets/1fbb5f43-ceab-46bb-be0e-2512ac4971fc)

   5. Congrats your backend setup for this project is done.





### Aditional Commands
1. whenever installed new package is update the requirements.txt using the command `pip freeze > requirements.txt` make sure your virtual environment is active before running this command.




