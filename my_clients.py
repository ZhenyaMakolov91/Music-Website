import psycopg2

class Clients:
    def __init__(self, dbname, user, password):
        '''подключение к базе данных'''
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password)

    def structure(self):  # 1 зачет
        '''формируем таблицы клиентов и их номеров'''
        with self.conn.cursor() as cur:
            cur.execute('''DROP TABLE phones; DROP TABLE clients;''')
            cur.execute('''
                CREATE TABLE IF NOT EXISTS clients(id SERIAL PRIMARY KEY, name VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL, email VARCHAR(40) UNIQUE NOT NULL);
                ''')
            cur.execute('''
                CREATE TABLE IF NOT EXISTS phones(id SERIAL PRIMARY KEY, phone VARCHAR(40) NOT NULL,
                client_id INTEGER REFERENCES clients(id));
                ''')
            self.conn.commit()

    def add_client(self, name, surname, email):
        '''добавляем клиента'''
        with self.conn.cursor() as cur:
            cur.execute('''
            INSERT INTO clients(name, surname, email) VALUES(%s, %s, %s);''', (name, surname, email))
            self.conn.commit()

    def add_phone(self, client_id, phone):
        '''добавление телефона'''
        with self.conn.cursor() as cur:
            cur.execute('''INSERT INTO phones(phone, client_id) VALUES(%s, %s);''', (phone, client_id))
            self.conn.commit()

    def update_client(self,):
        '''изменение данных клиента'''
        with self.conn.cursor() as cur:
            print('Обновление данных клиента')
            while True:
                id_client = input('Введите id: ')
                field = int(input('Введите номер обновляемого поля. 1) name; 2) surname; 3) email: ')) - 1
                if field not in [0, 1, 2]:
                    print('Ошибка! Такого поля не существует, попробуйте еще раз.')
                    break
                value = input('Введите новое значение поля: ')
                set_requests = ['''UPDATE clients SET name=%s WHERE id=%s''',
                                '''UPDATE clients SET surname=%s WHERE id=%s''',
                                '''UPDATE clients SET email=%s WHERE id=%s''']
                cur.execute(set_requests[field], (value, id_client))
                repeat = input('Повторить операцию? ')
                if repeat.lower() in ['да', 'yes']:
                    continue
                break
            self.conn.commit()

    def delete_phone(self, client_id):
        '''удаление телефона'''
        with self.conn.cursor() as cur:
            cur.execute('''DELETE FROM phones WHERE client_id=%s;''', (client_id,))
            self.conn.commit()

    def delete_client(self, client_id):
        '''удаление клиента'''
        with self.conn.cursor() as cur:
            cur.execute('''DELETE FROM phones WHERE client_id=%s;''', (client_id,))
            cur.execute('''DELETE FROM clients WHERE id=%s;''', (client_id,))
            self.conn.commit()

    def search_client(self, value):
        '''поиск клиента'''
        with self.conn.cursor() as cur:
            cur.execute('''SELECT id, name, surname FROM clients
                        WHERE name=%s OR surname=%s OR email=%s OR id=(SELECT client_id FROM phones WHERE phone=%s);''',
                        (value,) * 4)
            print(cur.fetchone())

    def my_tables(self):
        '''вывод таблиц клиентов и телефонов'''
        with self.conn.cursor() as cur:
            cur.execute('''SELECT * FROM clients'''), print(cur.fetchall())
            cur.execute('''SELECT * FROM phones'''), print(cur.fetchall())

database, my_user, my_password = input('Введите название БД: '), input('Имя пользователя: '), input('Пароль: ')
my_database = Clients(database, my_user, my_password)
my_database.structure()
my_database.add_client('Женя', 'Мамонов', 'emamonov@bk.ru')
my_database.add_client('Наташа', 'Маколова', 'mashoshina62@mail.ru')
my_database.add_client('Мирослав', 'Клозе', 'commander@bk.ru')
my_database.add_client('Ира', 'Андриевская', 't3@mail.ru')
my_database.add_client('Лидия', 'Штурмина', 'pochtovoe@list.ru')
my_database.add_client('Оля', 'Соколовская', 'matan@mail.ru')
my_database.add_phone(1, '+7-978-86-79-685')
my_database.add_phone(1, '+7-978-245-19-04')
my_database.add_phone(2, '+7-978-228-63-31')
# my_database.update_client()
# my_database.delete_phone(1)
# my_database.delete_client(1)
my_database.search_client('t3@mail.ru')
my_database.my_tables()
my_database.conn.close()