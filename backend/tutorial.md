# ===========================
# CUSTOM SHORTCUTS
# For "~/.zshrc" .... copy and paste
    # HOMEBREW
    export PATH=/opt/homebrew/bin:$PATH
    export PATH=/opt/homebrew/sbin:$PATH

    # CUSTOM ALIAS'
    alias bup="brew update && brew upgrade"
    alias delete_migrations="find . -path '*/migrations/*.py' -not -name '__init__.py' -delete && find . -path '*/migrations/*.pyc'  -delete"
    alias create_pgdb="docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -d postgres"
    alias test_migrations="python manage.py makemigrations --dry-run --verbosity 3"
    alias make_and_migrate="python manage.py makemigrations && python manage.py migrate"
    alias runserver="python manage.py runserver"
    alias start_redis="brew services start redis"
    alias reinstall_django="pip uninstall django && pip install django"
    alias rebuild_db="echo '\nEnsure db has already been deleted...\n' && sleep 5 && find . -path '*/migrations/*.py' -not -name '__init__.py' -delete && find . -path '*/migrations/*.pyc'  -delete && pip uninstall django && pip install django && docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -d postgres && sleep 5 && python manage.py makemigrations && python manage.py migrate && sleep 2 && python manage.py createsuperuser"
    alias create_postgis="docker run --name postgis -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -d postgis/postgis"

    export PATH="/opt/homebrew/opt/openssl@3/bin:$PATH"
    export PATH="/opt/homebrew/opt/llvm/bin:$PATH"
    export PATH=/Users/danm/.meteor:$PATH
# ===========================


# ===========================
# IF USING DOCKER FOR POSTGRES DATABASE
# create postgres postgis instance with the name "newapp"
docker run --name newapp -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -d postgis/postgis
# ===========================


# ===========================
## IF PROJECT DOES NOT EXIST
# create a new project named 'core' in current directory
django-admin startproject core .
# create new django 'users' app
python manage.py startapp users
# create customer user model 
# ...
# create new django 'api' app
python manage.py startapp api
# create customer api urls, views, serializers 
# ...
# ===========================



# create a new virtual environment
python3 -m venv venv         
# activate virtual environment
source venv/bin/activate
# upgrade pip
pip install --upgrade pip
# install requirements
pip install -r requirements.txt
# create superuser
python manage.py createsuperuser
# complete prompts
* Email address: 
* Password: 
* Password (again): 
* Bypass password validation and create user anyway? [y/N]: 
# runserver
python manage.py runserver
# login to admin (in browser)
http://127.0.0.1:8000/admin/





