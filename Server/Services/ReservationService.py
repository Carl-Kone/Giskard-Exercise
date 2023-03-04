import sqlite3

from ..Entities.Reservations import Reservation
from ..Repositories import reservationRepository


def addReservation(start: str, end: str, title: str, email: str):
    reservation = Reservation(start, end, title, email)
    reservationRepository.addReservation(reservation)


def deleteReservation(id: int):
    reservationRepository.deleteReservation(id)

def listReservations() -> list:
    return reservationRepository.listReservations()
