import sqlite3

from dataBase import dataBase
from ..Entities import Availabilities


def addAvailability(availability: Availabilities) -> int:
    connection = dataBase.createDataBase()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO availabilities VALUES (:id, :start, :end)",
                   {'id': None, 'start': availability.start, 'end': availability.end})
    availability_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return availability_id


def deleteAvailability(id: int):
    connection = dataBase.createDataBase()

    cursor = connection.cursor()
    cursor.execute("DELETE FROM availabilities WHERE id = :id", {'id': id})
    connection.commit()
    connection.close()


def listAvailabilities() -> list:
    connection = dataBase.createDataBase()
    cursor = connection.cursor()
    availabilities = cursor.execute("SELECT * FROM availabilities").fetchall()
    connection.close()
    return availabilities


def availabilityIsPresent(availability: Availabilities.Availability) -> bool:
    connection = dataBase.createDataBase()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM availabilities WHERE start=:start AND end=:end""",
                   {'start': availability.start, 'end': availability.end})
    result = cursor.fetchone()

    if result is not None:
        return True
    else:
        return False


def availabilityIsPresentById(availability_id: int) -> bool:
    connection = dataBase.createDataBase()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM availabilities WHERE id=:id""",
                   {'id': availability_id})
    result = cursor.fetchone()

    if result is not None:
        return True
    else:
        return False
