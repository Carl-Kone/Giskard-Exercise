import datetime

from ..Entities.Availabilities import Availability
from ..Repositories import availabilityRepository


def addAvailability(start: str, end: str) -> int:
    start_obj = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    end_obj = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

    if end_obj <= start_obj:
        return -1

    availability = Availability(start, end)

    if availabilityRepository.availabilityIsPresent(availability):
        return -2

    return availabilityRepository.addAvailability(availability)


def deleteAvailability(id: int) -> bool:
    if availabilityRepository.availabilityIsPresentById(id):
        availabilityRepository.deleteAvailability(id)
        return True
    else:
        return False



def listAvailabilities() -> list:
    return availabilityRepository.listAvailabilities()
