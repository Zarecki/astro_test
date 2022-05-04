from flask import Flask, Blueprint, render_template, request, redirect
from models.facility import Facility
import repositories.facility_repository as facility_repository

facilities_blueprint = Blueprint("facilities", __name__)

@facilities_blueprint.route("/facilities")
def facilities():
    facilities = facility_repository.select_all()
    return render_template("/facilities/index.html", facilities = facilities)

@facilities_blueprint.route("/facilities/<id>")
def show(id):
    facility = facility_repository.select(id)
    return render_template("/facilities/show.html", facility = facility)