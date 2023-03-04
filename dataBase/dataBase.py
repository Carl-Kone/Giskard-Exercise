import sqlite3

path = "dataBase/dataBase.db"


def createDataBase():
    connection = sqlite3.connect(path)
    return connection


def createAvailavabilityTable():
    connection = sqlite3.Connection(path)
    cursor = connection.cursor()
    cursor.execute(""" CREATE TABLE availabilities (
        id integer primary key,
        start TIMESTAMP,
        end TIMESTAMP
    )""")
    connection.commit()


def createReservationTable():
    connection = sqlite3.Connection(path)
    cursor = connection.cursor()
    cursor.execute(""" CREATE TABLE reservations (
        id integer primary key,
        start TIMESTAMP,
        end TIMESTAMP,
        title text,
        email text
    )""")
    connection.commit()
