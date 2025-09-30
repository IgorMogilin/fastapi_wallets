# Тесты для FastAPI Wallets API


### ✅ Основные эндпоинты
1. **test_root_endpoint** - Главная страница API
2. **test_api_docs** - Документация API
3. **test_openapi_schema** - OpenAPI схема

### ✅ Валидация и ошибки
4. **test_invalid_uuid** - Неверный формат UUID
5. **test_invalid_operation** - Неверные данные операции
6. **test_wrong_method** - Неверный HTTP метод

## Запуск тестов

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов
pytest tests/test_simple_6.py -v

# Запуск конкретного теста
pytest tests/test_simple_6.py::TestAPI::test_root_endpoint -v
```
