
# Project Title

Travel Website Project Using Django.
Destination informations can be added, deleted or updated from admin panel.


## Run Locally

Clone the project

```bash
  git clone https://github.com/Rifat-47/Travel.git
```

Go to the project directory

```bash
  cd Travel
```

Install virtual environment

```bash
  pip install virtualenv
```

Create a virtual environment with name 'venvname'
```bash
  python -m venv venvname
```

Activate virtual environment
```bash
  venvname\Scripts\activate
```

Install dependencies
```bash
  pip install -r requirements.txt
```

Run Django migrations to apply database changes
```bash
  python manage.py migrate
```

Run django server
```bash
  python manage.py runserver
```

Close server using ctrl + c

Deactivate virtual environment
```bash
  .\venvname\Scripts\deactivate
```


## Documentation

To remove virtual environment completely: 
```bash
  Remove-Item -Recurse -Force .\venvname
```

To add, delete or update the destinations from admin panel, create superuser.


Create superuser command
```bash
  python manage.py createsuperuser
```
Create superuser by using name, email, password etc.
After creating superuser, run the server & go to:

```bash
  http://127.0.0.1:8000/admin
```
Destinations can be added, deleted or updated from django admin panel.


## Screenshots

Home Page
![ScreenShot-1](https://github.com/Rifat-47/Travel/blob/main/screenshots/1.PNG)

Destination Information
![ScreenShot-2](https://github.com/Rifat-47/Travel/blob/main/screenshots/2.PNG)

Admin Panel
![ScreenShot-3](https://github.com/Rifat-47/Travel/blob/main/screenshots/3.PNG)


## Authors

- [@Rifat-47](https://github.com/Rifat-47)


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/Rifat-47)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rifat-ibn-taher/)
