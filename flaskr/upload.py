from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename


from flaskr.db import get_db

bp = Blueprint('upload', __name__)

@bp.route('/',methods=('GET','POST'))
def index():
    if request.method == 'POST':
        image = request.form['imagepath']