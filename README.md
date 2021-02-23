# yellow pos
Pos system

#make migration 

    python manage.py makemigrations shops users products orders
# test coverage 
    coverage run --source='.' manage.py test --keepdb
    coverage report
    