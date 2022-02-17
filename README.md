
# api_yamdb

![example workflow](https://github.com/frollow/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке. (Коллективный проект 3 студентов Яндекс.Практикум)

## Описание
API для сервиса YaMDb.
Позволяет работать со следующими сущностями:
- Отзывы
- Коментарии к отзывам
- Пользователи
- Категории (типы) произведений
- Категории жанров
- Произведения (на которые пишут отзывы)

 ##  Шаблон .env файла
Создайте файл в этой директории:

    /infra_sp2/infra/...

 Заполните его, и придумайте логин и пароль пользователя для базы данных, 
 вместо postgres укажите свои значения.

    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432

## Запуск программы

Выполните команду для запуска контейнеров:

    docker-compose -f infra/docker-compose.yaml up -d --build

Сделайте миграции:

    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate

Создайте пользователя:

    docker-compose exec web python manage.py createsuperuser

## Описание Api методов
http://localhost/redoc/

### Автор
Артем Фролов