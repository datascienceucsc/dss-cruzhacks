from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, current_app
from .constants import ip_address, overall_facebook_spending, overall_facebook_spending_chloro, google_trends

router = Blueprint('router', __name__)

overall_facebook_spending_addr = f"{ip_address}:{overall_facebook_spending}"
overall_facebook_spending_chloro_addr = f"{ip_address}:{overall_facebook_spending_chloro}"
google_trends_addr = f"{ip_address}:{google_trends}"

@router.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html', title="Transparency USA", iframesrc=overall_facebook_spending_chloro_addr)

@router.route("/single", methods=["GET", "POST"])
def single():
    return render_template('single_candidate.html', title="Transparency USA - Single Candidates", iframesrc=google_trends_addr)


