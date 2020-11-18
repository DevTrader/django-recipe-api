## To run:

docker-compose build </br>
docker-compose run app sh -c "python manage.py migrate" </br>
docker-compose run app sh -c "python manage.py runserver 0.0.0.0:8000" </br>

## To run tests:

docker-compose run app sh -c "python manage.py test" </br>
