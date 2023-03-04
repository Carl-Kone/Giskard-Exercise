import sqlite3

from dataBase import dataBase
from ..Entities import Reservations


def addReservation(reservation: Reservations.Reservation):
    connection = dataBase.createDataBase()

    cursor = connection.cursor()

    cursor.execute("""INSERT INTO reservations VALUES (:id, :start, :end, :title, :email)""",
                   {'id': None, 'start': reservation.start,
                    'end': reservation.end, 'title': reservation.title, 'email': reservation.email})
    connection.commit()


def deleteReservation(id: int):
    connection = dataBase.createDataBase()
    cursor = connection.cursor()

    cursor.execute("""DELETE FROM reservations where id = :id """, {'id': id})

    connection.commit()

def listReservations():
    connection = dataBase.createDataBase()
    cursor = connection.cursor()
    reservations = cursor.execute("""SELECT * FROM reservations""")
    return reservations.fetchall()
