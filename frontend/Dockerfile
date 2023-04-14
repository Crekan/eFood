# базовый образ
FROM node:14-alpine

# установка рабочей директории
WORKDIR /efood

# копирование файлов package.json и package-lock.json
COPY package*.json ./

# установка зависимостей
RUN npm install
RUN npm install axios

# копирование проектных файлов и папок в текущую директорию
COPY efood /efood

# сборка приложения для продакшн с минимизацией
RUN npm run build
# экспозиция порта 3000 для контейнера
EXPOSE 3000

# запуск приложения
CMD ["npm", "start"]
