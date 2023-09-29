# Установка и запуск

## Подготовка

Для запуска необходимо заполнить файл [.env.template](./app/env.template)
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
DB_HOST=127.0.0.1
DB_PORT=5431
```

## Создайте вертуально окружение
```
python -m venv template
```
## Активируйте окружение
```
template/Scripts/Activate
```
## Установите зависимости
```
pip install -r requirements.txt
```
## Запустить файл docker compose командой. Будет создана БД.
```
docker compose up -d
```
## Запустите файл server.py
[server.py](./app/server.py)

## Для отпарвки запросов используйте файл client.py
[client.py](./app/client.py)

## Подключитесь к БД для проверки. Параметры для подключения такие же как указали в [.env.template](env.template). Обратите внимение на PORT: 5431
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
DB_HOST=127.0.0.1
DB_PORT=5431
```

# Домашнее задание к лекции «Aiohttp»

Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория.

## Задание 1

Переписать сервис из [домашнего задания по Flask](../2.1-flask) на aiohttp.

Результатом работы является API, написанный на aiohttp.

## Задание 2 (необязательное)

Докеризировать API, написанный в задании 1.  
Чтобы проверить корректность работы сервиса, нужно:
1. запустить контейнер
2. проверить работу роута
