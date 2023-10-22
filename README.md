![Static Badge](https://img.shields.io/badge/python-3.10-green)
![Static Badge](https://img.shields.io/badge/django-4.2.6-blue)
<img alt="GitHub" src="https://img.shields.io/github/license/n1ce7ry/SyncPro">

# Sync Pro      

Crm system created for the company "Ural Computer Networks".

## Quick start

Install poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Clone the project
```bash
git clone https://github.com/n1ce7ry/SyncPro
```

Install the dependencies
```bash
poetry shell
poetry install
```

Edit env.example, rename it to env.sh, and run it:
```bash
vim env.example
mv env.example env.sh
. ./env.sh
```

Apply migrations
```bash
./manage.py migrate
```

Run server 
```bash
./manage.py runserver
```

## Screenshots : 

![dashboard](docs/images/dashboard.png)
![dashboard](docs/images/tasks.png)
![dashboard](docs/images/applications.png)
![dashboard](docs/images/clients.png)
![dashboard](docs/images/settings.png)
