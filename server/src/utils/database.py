from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Database:
    def __init__(self):
        self.session = db.session

    def save_all(self, items):
        """Saves list of modeled (e.g. Subscriber model) items to database"""
        self.session.add_all(items)
        self.session.commit()
