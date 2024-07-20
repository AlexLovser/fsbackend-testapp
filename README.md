# Test app
### Build the project
```sh
docker compose build
docker compose up -d

docker exec -it fsbackend-server-1 bash
python manage.py makemigrations
python manage.py migrate
exit

docker compose down
docker compose build
```

### Up
```sh
docker compose up
```

