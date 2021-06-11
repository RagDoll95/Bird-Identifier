from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
import os


from flaskr.db import get_db

bp = Blueprint('upload', __name__)

@bp.route('/',methods=('GET','POST'))
def index():
    if request.method == 'POST':
        image = request.files['file']
        if image.filename == '':
            flash('no file selected')
            return redirect(request.url)
        else:
            image_filename = secure_filename(image)
            image.save(os.path.join(app.config['UPLOAD'],image_filename))
            return redirect(url_for(results.results))

