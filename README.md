# Тестовое задание
### Подготовка проекта
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

### Запуск
```sh
docker compose up
```


### Тестирование программы

> ***Создание пользователей***
> 
> Открываем проект Postman который я отправил. И заходим в `/auth/register`, там создаем двух пользователей (не забывая почти паролей, которые мы написали в Body запроса, а также ID пользователей которые мы получили из ответов). 
> 
> Далее идем в `/auth/login`, где в Body подставляем эти данные и получаем по очереди два токена, которые мы подставляем в переменные проекта (`FSbackend -> Variables`), как **Token** и **AnotherToken**, соответственно. А также подставляем **myID** и **AnotherID**, чтобы в последствие использовать их для тестов.

1) Теперь эти данные можно использовать для тестирования программы, можно посмотреть себя как пользователя в `users/me`. 

2) Посмотреть свои отзывы и отзывы о себе в `reviews/my_reviews` и `reviews/about_me`, соответственно.

3) Создать новый отзыв в `reviews/create` и создать отзыв о себе в `reviews/create_about_me`.

4) Отредактировать или удалить отзыв в `reviews/edit` / `reviews/delete`

5) Посмотреть все существующие ревью в `reviews/all`