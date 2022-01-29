# DDM - Final project

#### API to be used in the final project


## Project setup

Use [git](https://git-scm.com/) to clone the project:

```bash
git clone https://github.com/Joabsonlg/ddm-rest-api
```
Enter the project:
```bash
cd ddm-rest-api
```
Create a virtual environment. (replace 'X' with your python version):
```bash
pythonX -m venv venv
```

Enter the virtual environment:
```bash
source venv/bin/activate
```

Add the environment variables: (create the '.env' file and add the variables)
```bash
SECRET_KEY=mySecretKey
```

Install the dependencies:
```bash
pip install django django-cors-headers djangorestframework djoser django-environ whitenoise pyyaml psycopg2 pillow gunicorn coreapi qrcode django-autoslug sendgrid-django
```

Create a superuser
```bash
python manage.py createsuperuser
```


## Usage

Run the API
```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author
<a href="https://github.com/Joabsonlg">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/41306493?v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Joabson Arley</b></sub></a> <a href="https://github.com/Joabsonlg" title="Github">🚀</a>

[![Gmail Badge](https://img.shields.io/badge/-joabsonlg918@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:joabsonlg918@gmail.com)](mailto:joabsonlg918@gmail.com)

## License
[MIT](https://github.com/Joabsonlg/ddm-rest-api/blob/master/LICENSE)
