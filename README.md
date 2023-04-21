# Проект QRKot
## _Приложение для Благотворительного фонда поддержки котиков_
![Python](https://img.shields.io/badge/Python-3.10.4-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.78.0-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.36-green)
![Pydantic](https://img.shields.io/badge/Pydantic-1.9.1-green)
![Flake8](https://img.shields.io/badge/flake8-4.0.1-green)
<br>
## Оглавление:
- [Введение](#введение)
- [Технические подробности](#технические-подробности)
- [Инструкция по запуску](#инструкция-по-запуску)

----
### <anchor>Введение</anchor>
Проект QRKot — приложение для Баготворительного фонда поддержки котов
Фонд может собирать на любые проекты пожертовования.<br>
**Проекты**<br>
В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект<br>
**Пожертвования**<br>
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.<br>
**Пользователи**<br>
Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

----
### <anchor>Технические подробности</anchor>
API проекта соответствует спецификации _Openapi_
После [запуска](#инструкция-по-запуску) документация по API доступна по адресами `127.0.0.1:8000/docs` по стандарту Swagger и `127.0.0.1:8000/redoc`
API разделены на группы: _проекты_, _пожертвования_, _пользователи_

**Проекты**
- Просмотр существующих проектов (_доступно всем_).
- Создавать, удалять и обновлять проекты могут только _администраторы (суперпользователи)_.

**Пожертвования**
- Просматривать существующие и создавать новые донаты могут все _зарегистрированные пользователи_.
- Каждый _зарегистрированный пользователь_ может просматривать свои созданные пожертвования.
- Удалять созданные пожертвования нельзя!

**Пользователи**
- *Зарегистрированные пользователи* могут просматривать информацию о себе, обновлять данные о себе.

----
### <anchor>Инструкция по запуску</anchor>

1. Клонировать репозиторий:<br>
`git clone git@github.com:Andrey-Kugubaev/cat_charity_fund.git`<br>
и перейти в директорию проекта `cat_charity_fund`

_Для Linux/macOS_
2. Создать и активировать вирутально окружение: <br>
`python3 -m venv venv` <br>
`source venv/bin/activate`
3. Установить зависимости из файла requirements.txt: <br>
`python3 -m pip install --upgrade pip` <br>
 `pip install -r requirements.txt` <br>
4. Применить миграции:<br>
`alembic upgrade head`
5. Запусить проект:<br>
`uvicorn app.main:app --reload`

_Для Windows_
2. Создать и активировать вирутально окружение: <br>
`python -m venv venv` <br>
`source venv/scripts/activate` <br>
3. Установить зависимости из файла requirements.txt: <br>
`python -m pip install --upgrade pip` <br>
`pip install -r requirements.txt` <br>
4. Применить миграции:<br>
`alembic upgrade head`
5. Запусить проект:<br>
`uvicorn app.main:app --reload`