## To run:

docker-compose build </br>
docker-compose run app sh -c "python manage.py migrate"
docker-compose run app sh -c "python manage.py runserver 8000" </br>

## To run tests:

docker-compose run app sh -c "python manage.py test" </br>
