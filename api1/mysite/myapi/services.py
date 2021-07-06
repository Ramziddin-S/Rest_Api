from contextlib import closing
from django.db import connection


def get_authors(author_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from  myapi_author"""
        )
        author = dictfetchall(cursor)
        return author


def get_author(author_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from  myapi_author where id = %s""", [author_id]
        )
        author = dictfetchone(cursor)
        return author


def get_genres():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from  myapi_genre"""
        )
        genre = dictfetchall(cursor)
        return genre


def get_genre(genre_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from  myapi_genre where id = %s""", [genre_id]
        )
        genre = dictfetchone(cursor)
        return genre


def get_books():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select myapi_book.*, myapi_author.id as author_id, myapi_author.name as author_name, 
            myapi_genre.id as genre_id, myapi_genre.name as genre_name from myapi_book left join myapi_author on myapi_book.author_id = myapi_author.id
            left join myapi_genre on myapi_book.genre_id = myapi_genre.id 
            """)
        book = dictfetchone(cursor)
        return book


def get_book(genre_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select myapi_book.*, myapi_author.id as author_id, myapi_author.name as author_name, 
            myapi_genre.id as genre_id, myapi_genre.name as genre_name from myapi_book left join myapi_author on myapi_book.author_id = myapi_author.id
            left join myapi_genre on myapi_book.genre_id = myapi_genre.id 
            where myapi_book.id = %s""", [genre_id])
        book = dictfetchone(cursor)
        return book

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
