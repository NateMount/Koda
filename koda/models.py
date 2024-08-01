#[KODA - MODELS]

from koda import db
from sqlalchemy.schema import UniqueConstraint

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(128))
    code = db.Column(db.String(6), nullable=False, unique=True, index=True)
    alias = db.Column(db.String(32), nullable=False, unique=True, index=True)
    password = db.Column(db.String(64), nullable=False)
    two_factor = db.Column(db.String(64))
    photo_path = db.Column(db.String(128), nullable=False)

    __table_args__ = (
        UniqueConstraint('code', name='uq_event_code'),
        UniqueConstraint('alias', name='uq_event_alias')
    )

    def __repr__(self) -> str:
        return f"<Event(id={self.id}, title={self.title}, code={self.code}, alias={self.alias})>"

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_alias = db.Column(db.String(32), nullable=False, index=True)
    path = db.Column(db.String(16), nullable=False)
    caption = db.Column(db.String(32))

    def __repr__(self) -> str:
        return f"<Upload(id={self.id}, event_alias={self.event_alias}, path={self.path})>"
