FROM python:3.10

RUN mkdir -p /app/
WORKDIR /app/

COPY . /app/

# Обновление pip
RUN pip install --upgrade pip

# Установка poetry
RUN pip install poetry

# Не создаем виртуальное окружение
RUN poetry config virtualenvs.create false

# Установка зависимостей
RUN poetry install

EXPOSE 8000

# Запуск фронтенда
CMD ["uvicorn", "main:app", "--reload"]
