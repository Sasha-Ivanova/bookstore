# Домашнее задание к лекции «Python и БД. ORM»

## Задание 1

Составить модели классов SQLAlchemy по схеме:

![](readme/book_publishers_scheme.png)   
Легенда: система хранит информацию об издателях (авторах), их книгах и фактах продажи. Книги могут продаваться в разных магазинах, поэтому требуется учитывать не только что за книга была продана, но и в каком магазине это было сделано, а также когда.
Интуитивно необходимо выбрать подходящие типы и связи полей.  

## Задание 2

Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python скрипт, который:

- Подключается к БД любого типа на ваш выбор.  
- Импортирует необходимые модели данных.
- Выводит издателя (publisher), имя или идентификатор которого принимается через `input`.  


## Задание 3.1 (необязательное)

- Настроить миграции через alembic. Миграция инициализации таблиц создается автоматически на основе модели данных. 

## Задание 3.2 (необязательное)

- Заполнение тестовых данных через миграцию или внешний скрипт.  
- Тестовые данные берутся из папки `fixtures`. Пример содержания в JSON файле.  

Возможно несколько вариантов реализации:

1. Парсится json, создаются соотведствующие экземляры моделей и сохраняются в БД.
2. Создаются новые фикстуры взамен JSON на основе [SQLAlchemy-Fixtures](https://sqlalchemy-fixtures.readthedocs.io/en/latest/) или [FactoryBoy](https://github.com/FactoryBoy/factory_boy)

## Общие советы:

- Параметры подключения к БД выносятся в отдельные переменные.  
- Загружать значения из окружения ОС, например через `os.getenv`.  
- Для самотестирования задания 2 рекомендуется выполнить задание 3.1, чтобы не создавать БД вручную или применить [create_all](https://docs.sqlalchemy.org/en/13/core/metadata.html#creating-and-dropping-database-tables).
- Заполнять можно вручную или выполнить 3.2.
