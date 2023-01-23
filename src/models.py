from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)

    def serialize_all(self):
        return {
            "uid": self.uid,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

    def serialize_each(self):
        return {
            "uid": self.uid,
            "properties":{
                "name": self.name,
                "gender": self.gender
            }
            # do not serialize the password, its a security breach
        }