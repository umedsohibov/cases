ЗАПУСК
uvicorn app.main:app --reload

Swagger
http://127.0.0.1:8000/docs

Эндпоинты
POST   /user/registration
POST   /user/login
POST   /password/new
GET    /password/{username}
DELETE /password/{username}/{password}

ЗАРЕГИСТРИРОВАТЬСЯ

curl -X POST "http://127.0.0.1:8000/user/registration" \
-H "Content-Type: application/json" \
-d '{
  "username": "test123",
  "password": "123456"
}'


ВОЙТИ

curl -X POST "http://127.0.0.1:8000/user/login" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=test123&password=123456"


СГЕНЕРИРОВАТЬ

curl -X POST "http://127.0.0.1:8000/password/new" \
-H "Authorization: Bearer YOUR_TOKEN"


ПОЛУЧИТЬ

curl -X GET "http://127.0.0.1:8000/password/test123" \
-H "Authorization: Bearer YOUR_TOKEN"


УДАЛИТЬ

curl -X DELETE "http://127.0.0.1:8000/password/test123/PASSWORD_TO_DELETE" \
-H "Authorization: Bearer YOUR_TOKEN"