# Используем образ Python
FROM python:3.10

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем зависимости
RUN pip install requests pytest

# Копируем все файлы из текущей директории в рабочую директорию контейнера
COPY . /app

# Запускаем тесты
CMD pytest tests.py
