import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    books = relationship('Book', back_populates='publisher')

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship('Publisher', back_populates='books')
    stocks = relationship('Stock', back_populates='books')

class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    stocks = relationship('Stock', back_populates='shops')

class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, sq.CheckConstraint('count > 0', name='check positive count'), nullable=False)
    books = relationship('Book', back_populates='stocks')
    shops = relationship('Shop', back_populates='stocks')
    sales = relationship('Sale', back_populates='stock')


class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, sq.CheckConstraint('price > 0', name='check positive price'), nullable=False)
    data_sale = sq.Column(sq.Date, nullable=False, index=True)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, sq.CheckConstraint('count > 0', name='check positive count'), nullable=False)
    stock = relationship('Stock', back_populates='sales')