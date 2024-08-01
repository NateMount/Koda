#[BLUEPRINTS - INIT]

from koda.blueprints import event, core

def register_blueprints(app):
    app.register_blueprint(event.frame, url_prefix='/event')
    app.register_blueprint(core.frame)