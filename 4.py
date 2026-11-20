CALLS = [
    # (операция, метод, путь, успех, ошибки)
    ("Create", "POST",   "/users",     "201 Created",    "400 Bad Request, 409 Conflict"),
    ("Read (список)", "GET", "/users", "200 OK",         "-"),
    ("Read (один)", "GET", "/users/42", "200 OK",        "404 Not Found"),
    ("Update (полн.)", "PUT", "/users/42", "200 OK",     "400 Bad Request, 404 Not Found"),
    ("Update (част.)", "PATCH", "/users/42", "200 OK",   "400 Bad Request, 404 Not Found"),
    ("Delete", "DELETE", "/users/42",  "204 No Content", "404 Not Found"),
]

print(f"{'Операция':<16}{'Запрос':<22}{'Успех':<18}Ошибки")
print("-" * 80)
for op, method, path, ok, err in CALLS:
    print(f"{op:<16}{method + ' ' + path:<22}{ok:<18}{err}")

print("\nСхема:\n")
print("Клиент                                   Сервер")
for op, method, path, ok, _ in CALLS:
    req = f"{method} {path}"
    print(f"  | --- {req:<24} ---> |   [{op}]")
    print(f"  | <--- {ok:<24} ---- |")
