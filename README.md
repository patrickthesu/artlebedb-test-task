Создатель: [Васильев Кирилл Александрович](https://t.me/vasylyev_kirill)

## Запуск

1. Скачать файлы данного репозитория
2. В терминале выполнить следующие команды

```
docker-compose build;
docker-compose up
```

Использование:
Все запросы должны производится по адресу:
http://0.0.0.0:8000/library
Вся информация предоставляется в json формате.
Пример ответа:
```json
{
    "id": 1,
    "contacts": {
        "id": 1,
        "email": "[tamarafatkulina@ngs.ru](mailto:tamarafatkulina@ngs.ru)",
        "phone": "73834022069"
    },
    "coordinates": {
        "id": 1,
        "posx": "83.99537200",
        "posy": "54.96136700"
    },
    "timezone": "Asia/Krasnoyarsk",
    "name": "Владимировская сельская библиотека",
    "description": "<p>Сельская библиотека с. Владимировка основана в <span>1956 году.</span></p><p><span></span><span> Она располагает книжным фондом в количестве 5 709 экземпляров. Книговыдача составляет 10 000 экземпляров. Постоянными читателями являются 505 жителей села. Посещения составляют 10 000 человек. </span></p><p><span>В библиотеке действует детский клуб по интересам «Фантазия». Работа клуба направлена на повышение культуры чтения исторической, научной, художественной и технико-технической литературы. Библиотека проводит значительную работу по привлечению детей к чтению по различным направлениям. Успешно сотрудничает с сельской школой и клубом, проводя мероприятия совместно и помогая информационно. </span></p> <p></p>",
    "fullAdress": "обл Новосибирская,р-н Тогучинский,с Владимировка,ул Центральная,зд 50"
}```

Для того чтобы получить библиотеку по id нужно обратится по адресу
http://0.0.0.0:8000/library/{id}
Например чтобы получить информацию о библиотеке с id 12 запрос будет таким:
http://0.0.0.0:8000/library/12

Чтобы найти библиотеку следует использовать параметр search. Поиск производится по имене и адресу библиотеки. Например чтобы найти библиотеку с именем lab запрос должен быть таким
http://0.0.0.0:8000/library/?search=lab

Для фильтрации запроса следует использовать следующий синтаксис {поле}={значение}
где поле это поле по которому будет использоватся фильтрация, а значение, это требуемое значение.
Возможные поля:
name: Название библиотеки
fullAdress: Адрес библиотеки
timezone: Часовой пояс библиотеки

## Информация для разработчика
Все переменные среды хранятся в файле .env
Чтобы запустить продакшн сервере обязательно нужно указать DEBUG=0 в файле .env

Чтобы запустить сервер на ином ip-адресе или хосте следует добавить ip-адрес или хост в список ALLLOWED_HOSTS  в файле backend/backend/settings.py. [Подробнее](https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-ALLOWED_HOSTS)

Обязательно следует поменять переменную SECRET_KEY в .env сгенерировав новый ключ безопасности при помощи
```Python
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

## От себя
Я знаю что у этого проекта проблемы с безопасностью (например в открытом доступе хранится django secret key или пароли базы данных )  но иначе пользователю придется много чего переделать своими руками, и вообще в таких случаях целесообразней использовать приватные репозитории.