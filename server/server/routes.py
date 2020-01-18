from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, current_app
from .constants import ip_address, facebook_port


router = Blueprint('router', __name__)


@router.route("/", methods=["GET", "POST"])
def home():
    facebook_addr = f"{ip_address}:{facebook_port}"
    return render_template('home.html', title="Transparency USA", iframesrc=facebook_addr)
