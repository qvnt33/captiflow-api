# Використання базового образу Python
FROM python:3.13-slim

# Створення робочої директорії
WORKDIR /app

# Копіювання залежності
COPY requirements.txt .

# Встановлення залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання всього коду проєкту
COPY . .

# Вимикання буферизації для зручності читання логів
ENV PYTHONUNBUFFERED=1

# Відкриття порту
EXPOSE 8000

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
