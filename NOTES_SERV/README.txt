получить все заметки
curl http://127.0.0.1:5001/notes

создать заметку
curl -X POST http://127.0.0.1:5001/notes -H Content-Type: application/json -d '{title: Test note, content: Hello}'

получить заметку по id
curl http://127.0.0.1:5001/notes/1

обновить заметку
curl -X PUT http://127.0.0.1:5001/notes/1 -H Content-Type: application/json -d '{title: Updated title, content: Updated content}'

удалить заметку
curl -X DELETE http://127.0.0.1:5001/notes/1

ОШИБКИ
пустой json
curl -X POST http://127.0.0.1:5001/notes -H Content-Type: application/json -d '{}'

несуществующий id
curl http://127.0.0.1:5001/notes/999
