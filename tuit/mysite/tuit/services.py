from contextlib import closing
from django.db import connection


def get_faculty():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from  tuit_faculty"""
        )
        faculty = dictfetchall(cursor)
        return faculty


def get_group():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from tuit_group"""
        )
        group = dictfetchall(cursor)
        return group


def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from tuit_subject"""
        )
        subject = dictfetchall(cursor)
        return subject


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from tuit_teacher"""
        )
        teacher = dictfetchall(cursor)
        return teacher


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select * from tuit_student"""
        )
        teacher = dictfetchall(cursor)
        return teacher


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
