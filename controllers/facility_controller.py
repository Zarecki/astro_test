from flask import Flask, Blueprint, render_template, request, redirect
from models.facility import Facility
import repositories.facility_repository as facility_repository

facilities_blueprint = Blueprint("facilities", __name__)

@facilities_blueprint.route("/facilities", methods=["GET"])
def facilities():
    facilities = facility_repository.select_all()
    return render_template("/facilities/index.html", facilities = facilities)

@facilities_blueprint.route("/facilities/<id>", methods=["GET"])
def show(id):
    facility = facility_repository.select(id)
    return render_template("/facilities/show.html", facility = facility)

@facilities_blueprint.route("/facilities/<id>/edit", methods=["GET"])
def edit_facility(id):
    facility = facility_repository.select(id)
    return render_template("/facilities/edit.html", facility = facility)

@facilities_blueprint.route("/facilities/<id>", methods=["POST"])
def update(id):
    facility = facility_repository.select(id)

    print(request.form)

    form_facility = request.form['facility']
    form_center = request.form['center']
    form_contact = request.form['contact']
    form_phone = request.form['phone']

    facility.facility = form_facility
    facility.center = form_center
    facility.contact = form_contact
    facility.phone = form_phone

    facility_repository.update(facility)
    return redirect("/facilities")