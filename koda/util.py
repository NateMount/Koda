#[KODA - UTIL]

import string
import koda.config as config

from koda.models import Event, Upload
from random import randint, choice

def gen_event_code(code_len:int = 6) -> str:
    while True:
        code = "".join([
            str(randint(0,9)) for _ in range(code_len)
        ])

        if Event.query.filter_by(code=code).first() is None:
            return code

def gen_event_alias(alias_len:int = 32) -> str:

    chars:str = string.ascii_lowercase + string.digits

    while True:
        
        code = "".join(choice(chars) for _ in range(alias_len))

        if Event.query.filter_by(alias=code).first() is None:
            return code

def filename_alias(ext:str = 'png', alias_len:int = 32) -> str:

    chars:str = string.ascii_lowercase + string.digits

    while True:

        code = "".join(choice(chars) for _ in range(alias_len))

        if Upload.query.filter_by(path=config.UPLOAD_FOLDER.split('/koda')[-1] + code).first() is None:
            return f"{code}.{ext}"

def get_join_alias_by_code(code:str) -> str:
    target_event = Event.query.filter_by(code=code).first()
    return target_event.alias if target_event else None

def allowed_file(filename:str) -> bool:
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS