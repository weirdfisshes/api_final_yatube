# api_final_yatube
### Описание. 

API социальной сети Yatube. Автор: Бурцев Никита.

### Как запустить проект.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone <cсылка_на_проект_в_git>

cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

Выполнить миграции:

```
python3  api_yamdb/manage.py migrate
```

Запустить проект:

```
python3 api_yamdb/manage.py runserver
```

### Документация к API

Доступна по адресу http://127.0.0.1:8000/redoc/ . Здесь можно увидеть все возможные запросы к api и ответы.

### Ресурсы API

Доступны следующие эндпоинты:
api/v1/jwt/create/ - получить JWT- токен
api/v1/jwt/refresh/ - обновить JWT- токен
api/v1/jwt/verify/ - проверить JWT- токен
api/v1/posts/ - получаем список всех постов или создаём новый пост.
api/v1/posts/{post_id}/ - получаем, редактируем или удаляем пост по id.
api/v1/groups/ - получаем список всех групп.
api/v1/groups/{group_id}/ - получаем информацию о группе по id.
api/v1/posts/{post_id}/comments/ - получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
api/v1/posts/{post_id}/comments/{comment_id}/ - получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
api/v1/follow/ - получаем или создаем подписки

---
### Запуск теста в виртуальном окружении
```
pytest
```
### Применение и запуск миграции (для моделей)
```
python manage.py makemigrations
python manage.py migrate
```
### Создание суперпользователя
```
python manage.py createsuperuser
```
`
---
