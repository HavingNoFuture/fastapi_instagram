# FastApi_instagram

Практический проект на FastApi иммтирующий приложение Instagram.

## [Техническое задание](docs/technical_requirements.md)

## Основные технологии:
* Python 3.10
* FastApi
* SqlAlchemy
* Alembic
* PostgreSQL
* VueJS


## Основные технологии:

### Подготовка бекенда:

1. Установить Python>=3.10
> https://www.linuxcapable.com/ru/how-to-install-python-3-10-on-ubuntu-20-04/

2. Установить глобально Poetry
```
pip install poetry
```

3. Установить пакеты для бекенда
```
cd backend/
poetry install
```

4. Запуск бекенда (из корня проекта)
```
cd ..
uvicorn backend.main:app --reload
```

### Подготовка фронтенда:

1. Установить npm для фронтенда
> https://andreyex.ru/ubuntu/kak-ustanovit-node-js-i-npm-v-ubuntu-20-04/

2. Установить пакеты для фронтенда
```
cd frontend/
npm install
```

3. Запуск фронтенда
```
npm run serve
```
