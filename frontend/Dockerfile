FROM node:14.18.3

RUN mkdir -p /app/
WORKDIR /app/
COPY . /app/

# Установка зависимостей
RUN npm install

EXPOSE 8080

# Запуск фронтенда
CMD ["npm", "run", "serve"]
