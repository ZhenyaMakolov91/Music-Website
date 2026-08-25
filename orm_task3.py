import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import models_task1 as mt1

with open('fixtures.json', encoding='utf-8') as f:
    res = json.load(f)

user, password, db_name = input('Введите имя пользователя: '), input('Пароль: '), input('Название БД: ')
DSN = f'postgresql://{user}:{password}@localhost:5432/{db_name}'
engine = sqlalchemy.create_engine(DSN)

mt1.create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

my_requests = []
my_classes = {'publisher': mt1.Publisher, 'book': mt1.Book, 'shop': mt1.Shop, 'stock': mt1.Stock, 'sale': mt1.Sale}
[my_requests.append(my_classes[dct['model']](**dct['fields'])) for dct in res]
session.add_all(my_requests), session.commit()

session.close()