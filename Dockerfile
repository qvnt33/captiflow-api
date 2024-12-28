# Використання базового образу Python
FROM python:3.13-slim

# Створення робочої директорії
WORKDIR /app

# Копіюємо залежності
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код проєкту
COPY . .

# Вимикання буферизацію для зручності читання логів
ENV PYTHONUNBUFFERED=1

# Відкриття порту
EXPOSE 8000

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
