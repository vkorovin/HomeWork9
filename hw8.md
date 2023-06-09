## Теория

### Устройство Python

- Устройство CPython: https://habr.com/ru/company/yandex/blog/511972/
- Знай и люби свой PyObject: https://www.youtube.com/watch?v=pgrmGduJVrs
- Знай и люби свой CPython: https://www.youtube.com/watch?v=0_5_zEOo8kg
- Доклады про "устройства питона": https://moscowpython.ru/speakers/zlata-obukhovskaya/
- Что не так с асинхронностью в питоне? https://www.youtube.com/watch?v=NmWzt7VdTgA

### Альтернативные интерпертаторы

- На Python: https://www.pypy.org
- На Rust: https://github.com/RustPython/RustPython

### gc

- `gc`: https://docs.python.org/3/library/gc.html
- `gc` in Python and Ruby: http://patshaughnessy.net/2013/10/30/generational-gc-in-python-and-ruby

### threading

- `threading`: https://docs.python.org/3/library/threading.html
- threading vs multiprocessing: https://blog.floydhub.com/multiprocessing-vs-threading-in-python-what-every-data-scientist-needs-to-know/
- Как использовать `threading`: https://webdevblog.ru/vvedenie-v-potoki-v-python/

### multiprocessing

- `multiprocessing`: https://docs.python.org/3/library/multiprocessing.html
- Things I Wish They Told Me About Multiprocessing in Python: https://www.cloudcity.io/blog/2019/02/27/things-i-wish-they-told-me-about-multiprocessing-in-python/

### asyncio

- `asyncio`: https://docs.python.org/3/library/asyncio.html
- `asyncio` на практике: https://habr.com/ru/post/337420/
- Как написать свой `asyncio`: https://moscowpython.ru/meetup/57/python-asynchronous-development/
- How async should have been: https://sobolevn.me/2020/06/how-async-should-have-been


## Практика

Наша задача написать полностью консольное приложение.

Наше приложение занимается хранением списка дел.

Требования:
- Команда `my-todo add 'title' 'description'` добавляет одно "дело" в список дел
- Команда `my-todo show 5` показывает нужно количество самых свежих дел
- Команда `my-todo done 1` отмечает какое-то дело как сделанное и удаляет его из списка
- Команда `my-todo find 'text'` ищет дела по заголовку или описанию

Технические требования:
- Хранение дел мы организуем в файле `todo.json` в текущей директории
- Парсинг команд и аргументов командой строки реализуем через `argparse`

Дополнительные задания (необязательные, но можно попробовать):

1. Воспользуйтесь https://github.com/wemake-services/wemake-python-package для генерации пакета
