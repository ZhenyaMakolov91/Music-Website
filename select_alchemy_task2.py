import sqlalchemy
from sqlalchemy.orm import sessionmaker

import models_task1 as mt1

db_name, password = input('Введите название БД: '), input('Пароль: ')
DSN = f'postgresql://postgres:{password}@localhost:5432/{db_name}'
engine = sqlalchemy.create_engine(DSN)

mt1.create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

pub1, pub2 = mt1.Publisher(name='Пушкин'), mt1.Publisher(name='Толстой')
session.add_all([pub1, pub2]), session.commit()

b1 = mt1.Book(title='Капитанская дочка', id_publisher=1)
b2 = mt1.Book(title='Руслан и Людмила', id_publisher=1)
b3 = mt1.Book(title='Евгений Онегин', id_publisher=1)
b4 = mt1.Book(title='Война и мир', id_publisher=2)
session.add_all([b1, b2, b3, b4]), session.commit()

sh1, sh2, sh3 = mt1.Shop(name='Буквоед'), mt1.Shop(name='Лабиринт'), mt1.Shop(name='Книжный дом')
session.add_all([sh1, sh2, sh3]), session.commit()

st1, st2 = mt1.Stock(id_book=1, id_shop=1, count=5), mt1.Stock(id_book=2, id_shop=1, count=3)
st3, st4 = mt1.Stock(id_book=1, id_shop=2, count=7), mt1.Stock(id_book=3, id_shop=3, count=4)
st5, st6 = mt1.Stock(id_book=1, id_shop=1, count=2), mt1.Stock(id_book=4, id_shop=3, count=2)
session.add_all([st1, st2, st3, st4, st5, st6]), session.commit()

sale1 = mt1.Sale(price=600, date_sale='09-11-2022', id_stock=1, count=1)
sale2 = mt1.Sale(price=500, date_sale='08-11-2022', id_stock=2, count=1)
sale3 = mt1.Sale(price=580, date_sale='05-11-2022', id_stock=3, count=1)
sale4 = mt1.Sale(price=490, date_sale='02-11-2022', id_stock=4, count=1)
sale5 = mt1.Sale(price=600, date_sale='26-10-2022', id_stock=5, count=1)
sale6 = mt1.Sale(price=1000, date_sale='24-08-2026', id_stock=6, count=1)
session.add_all([sale1, sale2, sale3, sale4, sale5, sale6]), session.commit()

obj, data_stocks = input('Введите фамилия или id автора: '), []
if obj.isdigit():
    id_publisher = session.query(mt1.Publisher).filter(mt1.Publisher.id == int(obj)).all()[0].id
else:
    id_publisher = session.query(mt1.Publisher).filter(mt1.Publisher.name == obj).all()[0].id
books = {c.id: c.title for c in session.query(mt1.Book).filter(mt1.Book.id_publisher == id_publisher).all()}

for k, v in books.items():
    for c in session.query(mt1.Stock).filter(mt1.Stock.id_book == k).all():
        data_stocks.append({'id': c.id, 'id_book': c.id_book, 'id_shop': c.id_shop, 'title': v})

shops = {c.id: c.name for c in session.query(mt1.Shop).all()}

for c in session.query(mt1.Sale).all():
    for st in data_stocks:
        if c.id_stock == st['id']:
            print(f"{st['title']} | {shops[st['id_shop']]} | {c.price} | {c.date_sale}")
            break

session.close()