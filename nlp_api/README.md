# Ports used by this NLP API:


| Exported port | Internal port |
| ------ | ------ |
| 5002 | 5000 |
| 5003 | 5000 |

The Nginx port assigned to those ports is 8081.


There are tow port because there are to instances of the same app for maintanability.

# Running this app
```sh
$ sudo docker-compose up --build
```
# Access this app

The app will be able from:

```http
http://localhost:8081/
```
