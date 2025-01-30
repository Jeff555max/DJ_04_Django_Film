# DJ_04_Django_Film

## Для запуска проекта, выполните следующие команды:

pip install django

python -m pip install Pillow

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


## Задание
Создайте проект с именем movie_project и приложение
в нем films. Создайте модель(таблицу) в которой будет
поле для названия фильма, поле для описание фильма и 
поле для отзыва.

Создайте две html страницы, на одной из которых нужно заполнить 3 поля и отправить эту информацию в базу данных, а на второй будет публиковаться информация которую вы записали в базу данных.
## Основные команды при создании проекта Django

.venv/Scripts/activate   
pip install django

django-admin startproject (название проекта) -создание проекта

python manage.py startapp (название приложения) -создание приложения

python manage.py runserver -запуск проекта

остановить- CTRL C

Миграции создают связь между базой данных и между приложением, соединяет их.
В пакете migrations через терминал создаём файл:

python manage.py makemigrations

В пакете создастся файл 0001_initial.py. В нём более подробно описаны поля таблицы, а также создано ключевое поле ‘id’.
Такое поле должно быть в каждой таблице.
Запускаем миграции через терминал.

python manage.py migrate -запуск миграции 

python manage.py createsuperuser- создание пароля и имени администратора


## Дополнительные команды
cd (название папки проекта)-зайти в нужную директорию с файлом manage.py

cd..  выйти из текущей папки на одну директорию выше

