import json

from models import Publisher, Book, Shop, Stock, Sale


def filling_data(session):
    with open('fixed.json', 'r') as file:
        json_data = json.load(file)
        for i in json_data:
            data = i['fields']
            if i['model'] == 'publisher':
                object = Publisher(name=data['name'])
            if i['model'] == 'book':
                object = Book(title=data['title'], id_publisher=data['id_publisher'])
            if i['model'] == 'shop':
                object = Shop(name=data['name'])
            if i['model'] == 'stock':
                object = Stock(id_book=data['id_book'], id_shop=data['id_shop'], count=data['count'])
            if i['model'] == 'sale':
                object = Sale(price=data['price'],
                              date_sale=data['date_sale'],
                              id_stock=data['id_stock'],
                              count=data['count'])
            session.add(object)
            session.commit()


def get_data(session):
    publisher_info = input('Введите имя или индификатор издателя: ')
    if publisher_info.isdigit() is True:
        query = session.query(Publisher, Book, Stock, Shop, Sale)
        query = query.join(Book, Book.id_publisher == Publisher.id).filter(Publisher.id == publisher_info)
        query = query.join(Stock, Stock.id_book == Book.id)
        query = query.join(Shop, Shop.id == Stock.id_shop).join(Sale, Sale.id_stock == Stock.id)
        for i, j, k, l, s in query.all():
            print(j.title, l.name, s.price, s.date_sale, sep=' | ')
    else:
        query = session.query(Publisher, Book, Stock, Shop, Sale)
        query = query.join(Book, Book.id_publisher == Publisher.id).filter(Publisher.name == publisher_info)
        query = query.join(Stock, Stock.id_book == Book.id)
        query = query.join(Shop, Shop.id == Stock.id_shop).join(Sale, Sale.id_stock == Stock.id)
        for i, j, k, l, s in query.all():
            print(j.title, l.name, s.price, s.date_sale, sep=' | ')
    session.close()
