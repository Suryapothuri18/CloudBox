from flask import render_template, request, redirect, url_for, flash
from . import db  # Import db from the init.py file where it's initialized
from .models import File  # Import the File model from models.py
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload():
    # Handle file upload logic here
    file = request.files['file']
    description = request.form.get('description')
    category = request.form.get('category')
    tags = request.form.get('tags')

    # Save file to database (this is just an example, modify as needed)
    new_file = File(description=description, category=category, tags=tags)
    db.session.add(new_file)
    db.session.commit()

    flash('File uploaded successfully!', 'success')
    return redirect(url_for('main.index'))
