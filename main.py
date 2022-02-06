from sqlalchemy import insert, select, or_, and_
from models import User, Address
from db import engine, Base

Base.metadata.create_all(engine)

def insert_many_users(values):
    stmt = insert(User)
    with engine.connect() as conn:
        conn.execute(stmt, values)

values = [
    {'name': 'Anna', 'fullname': 'Anna Karelina', 'sexdata': 'F', 'age': '25'},
    {'name': 'John', 'fullname': 'John Karelin', 'sexdata': 'M', 'age': '15'},
    {'name': 'David', 'fullname': 'David Karelin', 'sexdata': 'M', 'age': '26'},
    {'name': 'Vasil', 'fullname': 'Vasil Karelina', 'sexdata': 'M', 'age': '55'},
    {'name': 'Michel', 'fullname': 'Michel Karelina', 'sexdata': 'F', 'age': '54'}
         ]

# insert_many_users(values)

def select_users():
    stmt = (
            select(User.name, User.fullname)
             .where(
                    and_(
                         User.sexdata.like('M'),
                        or_(
                            User.name.like('L%'),
                            User.name.like('H%')
                           )
                        )
                    ).order_by(User.name.asc())
           )
    with engine.connect() as conn:
     return list(conn.execute(stmt))

for row in select_users():
    print(f'{row.name} has fullname: {row.fullname}')