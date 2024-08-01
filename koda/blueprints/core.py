#[BLUEPRINTS - CORE]

from flask import Blueprint, render_template, request, redirect
from os import path
from werkzeug.utils import secure_filename
from hashlib import sha256

from koda import db
from koda.models import Event
from koda.util import *

import koda.config as config

frame:Blueprint = Blueprint('core', __name__)

@frame.route('/', methods=['GET', 'POST'])
def event_join():

    if request.method == 'POST':
        event_alias = get_join_alias_by_code(request.form['join-code'])
        if not event_alias:
            return render_template('join.html')
        return redirect('/event/{}/gallery'.format(event_alias))

    return render_template('join.html')



@frame.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':

        alias = gen_event_alias()

        print(request.files)

        if 'photo' not in request.files:
            return redirect('/create')
        
        file = request.files['photo']

        if file.filename == '':
            return redirect('/create')
        
        if file and allowed_file(file.filename):
            file_ext = file.filename.rsplit('.', 1)[1].lower()
            file_alias = filename_alias(ext=file_ext)
            file_path = path.join(config.UPLOAD_FOLDER, file_alias)
            file.save(file_path)

            new_event = Event(
                title=request.form['title'],
                description=request.form['description'],
                code=gen_event_code(),
                alias=alias,
                password='null', #sha256(request.form['password'].encode()).hexdigest(),  
                photo_path=path.join(config.UPLOAD_FOLDER.split('/koda')[-1], file_alias)
            )

            try:
                db.session.add(new_event)
                db.session.commit()
                return redirect(f'/event/{alias}/gallery')
            except Exception as e:
                db.session.rollback()
                return redirect('/create')
        else:
            return redirect('/create')


    return render_template('create.html')

@frame.route('/info')
def info():
    return "tmp"

