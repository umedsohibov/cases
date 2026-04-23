получить все заметки
curl http://127.0.0.1:5001/notes

создать заметку
curl -X POST http://127.0.0.1:5001/notes -H "Content-Type: application/json" -d '{"title": "Test", "content": "Test content"}'

получить заметку по id
curl http://127.0.0.1:5001/notes/1

обновить заметку по id
curl -X PUT http://127.0.0.1:5001/notes/1 -H "Content-Type: application/json" -d '{"title": "Updated title", "content": "Updated content"}'

удалить заметку по id
curl -X DELETE http://127.0.0.1:5001/notes/1

ошибка: пустой json
curl -X POST http://127.0.0.1:5001/notes -H "Content-Type: application/json" -d '{}'

ошибка: несуществующий id
curl http://127.0.0.1:5001/notes/999

ошибка: удаление несуществующего id
curl -X DELETE http://127.0.0.1:5001/notes/999