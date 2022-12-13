import uuid
from sqlalchemy.dialects.postgresql import UUID, JSON
from utils.database import db


class Subscriber(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    full_name = db.Column(db.String(100))

    def __init__(self, id, first_name, last_name, full_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name


class Demographics(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    gender = db.Column(db.String(50))
    age = db.Column(db.Integer)
    race = db.Column(db.String(50))
    marital_status = db.Column(db.String(50))
    education = db.Column(db.String(50))
    household_income = db.Column(db.String(50))
    subscriber_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("subscriber.id"), nullable=False
    )

    def __init__(
        self,
        id,
        gender,
        age,
        race,
        marital_status,
        education,
        household_income,
        subscriber_id,
    ):
        self.id = id
        self.gender = gender
        self.age = age
        self.race = race
        self.marital_status = marital_status
        self.education = education
        self.household_income = household_income
        self.subscriber_id = subscriber_id


class EmailPerformance(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    products = db.Column(JSON)
    subscriber_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("subscriber.id"), nullable=False
    )

    def __init__(self, id, products, subscriber_id):
        self.id = id
        self.products = products
        self.subscriber_id = subscriber_id
