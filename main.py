import sqlite3

from dataBase import dataBase
from Server.Repositories import availabilityRepository, reservationRepository
from Server.Entities import Availabilities, Reservations
from Server.Services.AvailabilitiesService import *
from Server.Services.ReservationService import *
import datetime
from Server.apiEndPoint import app
dataBase.createDataBase()
try:
    dataBase.createReservationTable()
    dataBase.createAvailavabilityTable()
except sqlite3.OperationalError:
    pass


app.run("localhost", 6969, debug=True)
