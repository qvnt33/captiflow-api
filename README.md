# **captiflow-api**

Це **API** для управління витратами, побудований на **Django REST Framework**.

Проєкт підтримує CRUD-операції для категорій витрат, підкатегорій, транзакцій та заощаджень. Реалізовано **фільтрацію**, **сортування** та **JWT-аутентифікацію**. Дані зберігаються в **PostgreSQL**.

## **Вимоги**

Для запуску проєкту вам знадобиться:

- **Python 3.9** або вище;
- **PostgreSQL**;
- Віртуальне середовище **Python** (`venv` або аналог);
- Пакети з `requirements.txt`.

## Інструкція з налаштування (локально)

### 1. Клонування репозиторію
```
git clone https://github.com/qvnt33/captiflow-api.git
cd captiflow-api
```

### 2. Створення віртуального середовища
```
python -m venv .venv
source .venv/bin/activate  # Для Linux/MacOS
```

або

```
.\.venv\Scripts\activate  # Для Windows
```

### 3. Встановлення залежностей

```
pip install -r requirements.txt
```

### 4. Налаштування середовища

1. У головній директорії знайдіть файл `.env.example`.
2. Створіть копію цього файлу та назвіть її `.env`.
3. Заповніть файл `.env` вашими даними для підключення до бази **PostgreSQL**.
4. Для локального тестування вкажіть: `DATABASE_HOST=localhost`
5. Переконайтесь, що у вас запущений **PostgreSQL** і створена база даних.

## Запуск проєкту (локально)

### 1. Застосування міграцій

```
python manage.py makemigrations
python manage.py migrate
```
### 2. Створення суперкористувача (для адмін-панелі)


```
python manage.py createsuperuser
```

### 3. Запуск сервера

```
python manage.py runserver
```

Сервер буде доступний за адресою:
`http://127.0.0.1:8000/`.

## Інструкція з налаштування (через Docker)

### 1. Клонування репозиторію
```
git clone https://github.com/qvnt33/captiflow-api.git
cd captiflow-api
```

### 2. Налаштування *.env

1. У головній директорії знайдіть файл `.env.example`.
2. Створіть копію цього файлу та назвіть її `.env`.
3. Заповніть файл `.env` вашими даними для підключення до бази **PostgreSQL**.
4. Для Docker-середовища вкажіть: `DATABASE_HOST=db`

### 3. Запуск Docker
1.	Запустіть сервіси через **Docker Compose**: `docker-compose up -d`
2.	Перевірте, чи контейнери працюють: `docker ps`

### 4. Виконання міграцій у Docker
Для застосування міграції, виконайте: `docker exec -it drf_app python manage.py migrate`

### 5. Створення суперкористувача у Docker
Щоб створити суперкористувача: `docker exec -it drf_app python manage.py createsuperuser`


## Запуск проєкту (через Docker)

### 1. Застосування міграцій

```
python manage.py makemigrations
python manage.py migrate
```
### 2. Створення суперкористувача (для адмін-панелі)


```
python manage.py createsuperuser
```

### 3. Запуск сервера

```
python manage.py runserver
```

Сервер буде доступний за адресою:
`http://127.0.0.1:8000/`.


## Використання API

### 1. Отримання токену (JWT)

Для використання **API** спершу отримайте токен доступу. Надішліть POST-запит на `/api/token/`:

```
{
    "username": "your_username",
    "password": "your_password"
}
```

**Відповідь:**

```
{
    "refresh": "refresh_token_here",
    "access": "access_token_here"
}
```

Використовуйте `access_token` для авторизації:

```
Authorization: Bearer <access_token>
```

## Основні ендпоінти API

| Маршрут               | HTTP методи         | Опис                              |
|-----------------------|---------------------|-----------------------------------|
| `/api/token/`         | POST                | Отримання JWT-токену              |
| `/api/token/refresh/` | POST                | Оновлення JWT-токену              |
| `/categories/`        | GET, POST           | Список категорій / Створення      |
| `/categories/{id}/`   | GET, PUT, DELETE    | Отримання, оновлення, видалення   |
| `/subcategories/`     | GET, POST           | Список підкатегорій / Створення   |
| `/transactions/`      | GET, POST           | Список транзакцій / Створення     |
| `/savings/`           | GET, POST           | Список заощаджень / Створення     |
