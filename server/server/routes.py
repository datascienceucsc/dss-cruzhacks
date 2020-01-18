from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, current_app

router = Blueprint('router', __name__)

@router.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html', title="ADD TITLE HERE")


