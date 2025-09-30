# Запуск проекта в Docker


## Запуск

1. Скопируйте файл с переменными окружения или переименуйте его в .env:
```bash
cp env.example .env
```

2. Запустите проект:
```bash
docker-compose up --build
```

## Доступ к приложению

- API: http://localhost:8000
- Документация API: http://localhost:8000/api/v1/docs
- База данных PostgreSQL: localhost:5432

## Полезные команды

### Остановка контейнеров
```bash
docker-compose down
```

### Остановка с удалением volumes
```bash
docker-compose down -v
```

### Просмотр логов
```bash
docker-compose logs -f app
docker-compose logs -f postgres
```

### Выполнение команд в контейнере приложения
```bash
docker-compose exec app bash
```

### Пересборка контейнеров
```bash
docker-compose up --build --force-recreate
```

## Переменные окружения:

- `DATABASE_URL` - адрес подключения к PostgreSQL
- `TESTING` - режим тестирования (true/false)

## Структура

- `Dockerfile` - конфигурация для сборки образа приложения
- `docker-compose.yml` - конфигурация для запуска приложения
- `.dockerignore` - файлы, исключаемые из Docker
