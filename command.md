pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker-compose up -d --build
docker exec -it django /bin/sh
python manage.py startapp testapp

<!-- to open manage.py shell -->
docker exec -it django python manage.py shell