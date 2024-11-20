from app import db

class Puppy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    is_adopted = db.Column(db.Boolean, default=False)

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.is_adopted = False

    def __repr__(self):
        return f'<Puppy {self.name}>'
