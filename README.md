# AndreiBaliyevich_com


### Portfolio of developer.


## Описание проекта

Сайт-портфолио предназначен для демонстрации своих проектов.

В приложении "main" определяется модель пользователя, которая хранит информацию о разработчике. Эта информация отображается на различных страницах сайта.

Информация о проектах хранится в приложении "portfolio". Владелец сайта может добавлять и редактировать проекты через административный сайт Django.

Приложение "contact" принимает и хранит сообщения от посетителей сайта, а также присылает владельцу сайта email о новом сообщении.


## Установка

Для запуска проекта испльзуется Docker.

##### 1. Клонировать репозиторий

    git clone https://github.com/andreibaliyevich/AndreiBaliyevich_com.git

##### 2. Перейти в папку репозитория

    cd AndreiBaliyevich_com

##### 3. Создать файл .env с переменными окружения в папке src

Например:

    SECRET_KEY=secret_key
    SQL_NAME=sql_name
    SQL_USER=sql_user
    SQL_PASSWORD=sql_password
    EMAIL_HOST_USER=email_host_user
    EMAIL_HOST_PASSWORD=email_host_password
    EMAIL_HOST_RECEIVER=email_host_receiver

##### 4. Создать файл .env с переменными окружения в папке postgres

Например:

    POSTGRES_DB=sql_name
    POSTGRES_USER=sql_user
    POSTGRES_PASSWORD=sql_password

##### 5. Создать образ

    docker-compose build

##### 6. Запустить bash в сервисе django

    docker-compose run django bash

##### 7. Применить миграции

    python manage.py migrate

##### 8. Скомпилировать файлы переводов

    django-admin compilemessages

##### 9. Создать суперпользователя

    python manage.py createsuperuser

##### 10. Выйти из bash

    exit

##### 11. Запустить контейнер

    docker-compose up


## Лицензия

[GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)

Copyright © 2021 Andrei Baliyevich
