from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, current_app
import requests

router = Blueprint('router', __name__)

facebook_data_port = 8050


@router.route("/", methods=["GET", "POST"])
def home():
    facebook_data_url = f"http://localhost:{facebook_data_port}"
    facebook_graph = requests.get(facebook_data_url).text
    return render_template('home.html', title="ADD TITLE HER", iframe=facebook_graph)


