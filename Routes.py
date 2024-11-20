from flask import request, jsonify
from app import app, db
from app.models import Puppy
from app.schemas import PuppySchema

puppy_schema = PuppySchema()
puppies_schema = PuppySchema(many=True)

@app.route('/puppies', methods=['POST'])
def register_puppy():
    data = request.get_json()
    new_puppy = Puppy(name=data['name'], breed=data['breed'], age=data['age'])
    
    db.session.add(new_puppy)
    db.session.commit()
    
    return puppy_schema.jsonify(new_puppy), 201

@app.route('/puppies', methods=['GET'])
def get_puppies():
    all_puppies = Puppy.query.filter_by(is_adopted=False).all()
    return puppies_schema.jsonify(all_puppies)

@app.route('/puppy/adopt/<int:id>', methods=['PUT'])
def adopt_puppy(id):
    puppy = Puppy.query.get(id)
    if not puppy:
        return jsonify({"message": "Puppy not found"}), 404
    
    puppy.is_adopted = True
    db.session.commit()
    
    # Automatically delete the puppy once adopted
    db.session.delete(puppy)
    db.session.commit()
    
    return puppy_schema.jsonify(puppy)
