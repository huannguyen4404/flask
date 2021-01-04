from datetime import datetime
from mongoengine import signals

from database import db

USERS = {
    'auto': 'Automation',
    'other': 'Anonymous User'
}


class UploadedImage(db.EmbeddedDocument):
    name = db.StringField()
    source_origin = db.StringField()


class BoundingBox(db.EmbeddedDocument):
    x = db.IntField()
    y = db.IntField()
    w = db.IntField()
    h = db.IntField()


class Item(db.Document):
    label = db.StringField(required=True)
    description = db.StringField(required=False)
    image = db.EmbeddedDocumentField(UploadedImage, required=False, null=True)
    bbox = db.EmbeddedDocumentField(BoundingBox, required=False, null=True)

    # audit fields
    created_by = db.StringField(
        choices=USERS.keys(), default=USERS['auto'], required=True
    )
    modified_by = db.StringField(
        choices=USERS.keys(), default=USERS['auto'], required=False, null=True
    )
    created_at = db.DateTimeField(required=True, default=datetime.now())
    updated_at = db.DateTimeField(required=True, )

    @property
    def get_creator(self):
        return USERS[self.created_by]

    @property
    def get_modifier(self):
        return USERS[self.modified_by]


def add_creator(sender, document, **kwargs):
    document.created_by = document.created_by if document.created_by else \
        'auto'


def update_timestamp(sender, document, **kwargs):
    document.updated_at = datetime.utcnow()


signals.pre_save.connect(add_creator, sender=Item)
signals.pre_save.connect(update_timestamp, sender=Item)
