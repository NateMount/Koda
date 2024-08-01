#[BLUEPRINTS - EVENT]

from flask import Blueprint, render_template, redirect, request
from os import path
from werkzeug.utils import secure_filename


import koda.config as config
from koda import db
from koda.models import Event, Upload
from koda.util import filename_alias, allowed_file

frame:Blueprint = Blueprint('event', __name__)

@frame.route('/<event_alias>/gallery', methods=['GET', 'POST'])
def event_main(event_alias:str):

    if request.method == 'POST':

        if 'photo-upload' not in request.files:
            return redirect("/event/{}/gallery".format(event_alias))
        
        file = request.files['photo-upload']

        if file.filename == '':
            return redirect("/event/{}/gallery".format(event_alias))
        
        if file and allowed_file(file.filename):
            file_ext = file.filename.rsplit('.', 1)[1].lower()
            file_alias = filename_alias(ext=file_ext)
            file_path = path.join(config.UPLOAD_FOLDER, file_alias)
            file.save(file_path)

            new_upload = Upload(
                event_alias=event_alias, 
                path=path.join(config.UPLOAD_FOLDER.split('/koda')[-1], file_alias), 
                caption=""
            )
            try:
                db.session.add(new_upload)
                db.session.commit()
            except Exception as e:
                db.session.rollback()

        return redirect(f"/event/{event_alias}/gallery")

    event_target:Event = Event.query.filter_by(alias = event_alias[:32]).first()
    if not event_target:
        return redirect('/')
    
    uploads = Upload.query.filter_by(event_alias=event_target.alias).all()[::-1]
    return render_template('event.html', event=event_target, content=uploads)

@frame.route('/<event_alias>/live')
def event_live_view(event_alias:str):
    
    event_target = Event.query.filter_by(alias=event_alias[:32]).first()
    if not event_target:
        return redirect('/')
    
    next_path = Upload.query.filter_by(event_alias=event_alias).order_by(Upload.id.desc()).first()
    if not next_path:
        return redirect(f"/event/{event_alias}/gallery")
    
    return render_template('live.html', next_path=next_path.path, event=event_target)

#@frame.route('/<event_alias>/manage')
#def event_manage(event_alias:str):
#    event_target:Event = Event.query.filter_by(alias = event_alias[:32]).first()
#    return render_template('manage.html', event=event_target)