# API Tests — JSONPlaceholder

Учебный проект автотестов на Python. Тестирую REST API сервиса JSONPlaceholder.

## Стек
- Python 3.14
- pytest
- requests

## Что тестируется

**Users** (`/users`):
- GET существующих юзеров
- GET несуществующих юзеров (негативные кейсы)
- POST создание юзера
- PUT обновление юзера
- DELETE удаление юзера

**Posts** (`/posts`):
- GET существующих постов
- GET несуществующих постов (негативные кейсы)
- POST создание поста
- PUT обновление поста
- DELETE удаление поста

## Структура проекта
```
APITestminiproj/
├── conftest.py
├── tests/
│   ├── test_users.py
│   └── test_posts.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Как запустить

Установить зависимости:
pip install pytest requests

Запустить все тесты:
pytest tests/ -v

## Результат
32 теста, все проходят.