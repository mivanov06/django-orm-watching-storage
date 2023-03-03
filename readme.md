# Пульт охраны банка

Программа для работы с пропускной системой в хранилище банка.

## Установка и запуск

1. Скачать архив и распаковать.

2. Установить виртуальное окружение, активировать его и установить зависимости
```
python -m venv venv
```
```
venv/scripts/activate
```
```
pip install -r requirements.txt
```
3. Файл `.env.example` переименовать в `.env`. 

Изменить в `.env` значения параметров для подключения к базе данных `HOST`, `PORT`,
`NAME`, `USER`, `PASSWORD`. `SECRET_KEY`, `DEBUG`

## Использование
Для запуска сервера выполнить

``` python manage.py runserver ```

Пульт доступен по адресу: http://127.0.0.1:8000

Страницы
1. Список всех активных пользователей: http://127.0.0.1:8000/active_passcards
2. Список людей, которые находятся в хранилище в данный момент: http://127.0.0.1:8000/storage_information
3. Список всех совершенных визитов каждого пользователя: http://127.0.0.1:8000/passcard_info/

При нахождении пользователя в хранилище более определенного периода (по умолчанию 60 мин) на пульте отображается 
флаг подозрительности посещения.

![passcard](https://user-images.githubusercontent.com/77063936/222030487-9719d9ff-4c2d-4ca2-8528-ca9f6c1c7580.png)


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
