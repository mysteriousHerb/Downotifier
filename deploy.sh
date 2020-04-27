cd backend
pipenv run pip freeze > requirements.txt

cd ..
docker-compose down
docker-compose build
docker-compose up

