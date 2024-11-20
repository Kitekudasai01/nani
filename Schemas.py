from app import ma
from app.models import Puppy

class PuppySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Puppy
        load_instance = True
