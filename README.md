# Практика: HTTP/1.1 и REST API

Все скрипты написаны на Python 3 и используют только стандартную библиотеку.

## Задания

| № | Файл | Описание |
|---|------|----------|
| 1 | `task1_raw_http.py` | HTTP вручную: запрос `GET / HTTP/1.1` с заголовком `Host` через сокет (аналог netcat) |
| 2 | `task2_static_server.py` | Статический сервер: ответы 200, 404, 405; `Content-Type` по расширению файла |
| 3 | `task3_rest_client.py` | REST-клиент: получение данных публичного API, разбор JSON, вывод полей |
| 4 | `task4_crud_scheme.py` | Схема вызовов: CRUD-запросы и ожидаемые статусы для `/users` |

## Запуск

```bash
# 1. Ручной HTTP-запрос (хост по умолчанию example.com)
python task1_raw_http.py example.com

# 2. Статический сервер (порт и папка необязательны)
python task2_static_server.py 8000 public
# проверка:
curl -i http://localhost:8000/          # 200
curl -i http://localhost:8000/nope      # 404
curl -i -X POST http://localhost:8000/  # 405

# 3. REST-клиент (нужен доступ в интернет)
python task3_rest_client.py

# 4. Схема CRUD для /users
python task4_crud_scheme.py
```

## Статусы для /users

| Операция | Запрос | Успех | Ошибки |
|----------|--------|-------|--------|
| Create | `POST /users` | 201 Created | 400, 409 |
| Read (список) | `GET /users` | 200 OK | - |
| Read (один) | `GET /users/42` | 200 OK | 404 |
| Update | `PUT /users/42`, `PATCH /users/42` | 200 OK | 400, 404 |
| Delete | `DELETE /users/42` | 204 No Content | 404 |
