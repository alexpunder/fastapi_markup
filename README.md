## Описание проекта.

_**Проценка**_ - переделанное приложение с Flask на FastAPI, позволяющее обратиться к API заданных поставщиков для получения информации об интересующем товаре по введённым артикулу и/или производителю запчасти. Парсинг всех полученных данных к одному виду и вывод результатов в порядке возрастания цены за товар, по наличию, складам и дате доставки.
На данным момент доступны следующие поставщики:  
- [Фаворит](https://favorit-parts.ru/)
- [Москворечье](https://www.moskvorechie.ru/)
- [Форум-авто](https://forum-auto.ru/)
- [Росско](https://rossko.ru/)
- [Автоевро](https://shop.autoeuro.ru/)
- [ПрофитЛига](https://pr-lg.ru/)
- [Армтек](https://armtek.ru/)
- [Микадо](https://www.mikado-parts.ru/)
- [Motexc](https://motexc.ru/)

## Используемые технологии.

[![Python 3.12](https://img.shields.io/badge/Python-3.12-brightgreen.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.1-brightgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.30.1-brightgreen.svg?style=flat&logo=uvicorn&logoColor=white)](https://www.uvicorn.org/)
[![Aiohttp](https://img.shields.io/badge/Aiohttp-3.9.3-brightgreen.svg?style=flat&logo=python&logoColor=white)](https://docs.aiohttp.org/en/stable/)
[![Asyncio](https://img.shields.io/badge/Asyncio-brightgreen.svg?style=flat&logo=python&logoColor=white)](https://docs.python.org/3/library/asyncio.html)
[![Zeep](https://img.shields.io/badge/Zeep-4.2.1-brightgreen.svg?style=flat&logo=python&logoColor=white)](https://docs.python-zeep.org/en/master/)
[![PyInstaller](https://img.shields.io/badge/PyInstaller-6.8.0-brightgreen.svg?style=flat&logo=python&logoColor=white)](https://pyinstaller.org/en/stable/)

## Вспомогательная команда

Для формирования одно запускающего файла на Windows, находясь в директории `/app/`, выполните команду:
```
pyinstaller app.spec
```
