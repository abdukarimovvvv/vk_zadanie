# Процессор JSON-документов

Этот проект предоставляет систему для обработки JSON-документов на основе пользовательских схем.
## Настройка
1. Установите зависимости:
 `pip install -r requirements.txt`
2. Настройте базу данных, используя схему в `db/schema.sql`.

## Использование

1. Создайте JSON-схему для вашего типа документа.
2. Используйте инструмент CLI для генерации моделей и контроллеров:
 `python cli/generator.py`
3. Запустите REST-приложение:
 `python rest_app/main.py`

## API Endpoints

- POST /{kind}/ - Создать новый документ
- GET /{kind}/{uuid} - Получить документ
- PUT /{kind}/{uuid}/configuration - Обновить конфигурацию
- PUT /{kind}/{uuid}/settings - Обновить настройки
- PUT /{kind}/{uuid}/state - Обновить состояние
- DELETE /{kind}/{uuid} - Удалить документ
- GET /{kind}/{uuid}/state - Получить состояние документа

For more details, refer to the generated controller files in `rest_app/routes/`.