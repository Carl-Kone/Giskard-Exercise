import flask
from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect, url_for

from Server.Services import AvailabilitiesService
from Server.Services import ReservationService
from dataBase import dataBase

app = Flask(__name__)


@app.route("/")
def home():
    availabilities = AvailabilitiesService.listAvailabilities()
    return render_template("base.html", availabilities=availabilities)


@app.post('/add')
def addAvailability():
    print("Entered addAvailability")

    start = request.form['start-time']
    end = request.form['end-time']

    availability_id = AvailabilitiesService.addAvailability(start, end)
    return redirect(url_for("home"))


@app.get('/delete/<int:availability_id>')
def deleteAvailability(availability_id):
    if AvailabilitiesService.deleteAvailability(availability_id):
        return redirect(url_for("home"))
    else:
        return make_response("No availability with id {}".format(availability_id), 400)


@app.route('/reservations', methods=["GET"])
def listReservations():
    reservations = ReservationService.listReservations()
    return render_template("reservation.html", reservations=reservations)


@app.get('/reservations/delete/<int:reservation_id>')
def deleteReservation(reservation_id):
    start = request.args.get('start-time')
    end = request.args.get('end-time')
    ReservationService.deleteReservation(reservation_id)
    AvailabilitiesService.addAvailability(start,end)
    return redirect(url_for("listReservations"))


@app.post('/reservations/add')
def addReservation():
    id = request.form['id']
    start = request.form['start-time']
    end = request.form['end-time']
    title = request.form['title']
    email = request.form['email']

    reservation_id = ReservationService.addReservation(start,end,title,email)
    deleteAvailability(id)
    return redirect(url_for("listReservations"))