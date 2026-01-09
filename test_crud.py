#!/usr/bin/env python3

"""
Test script to demonstrate Flask-SQLAlchemy CRUD operations
This script simulates the Flask shell commands from the lab
"""

import sys
import os
sys.path.append('/home/brenda/Documents/Moringa-projects/Phase4/python-p4-v2-flask-sqlalchemy-crud-shell/server')

from app import app
from models import db, Pet
from sqlalchemy import func

def test_crud_operations():
    """Test all CRUD operations as described in the lab"""
    
    with app.app_context():
        print("=== Flask-SQLAlchemy CRUD Operations Test ===\n")
        
        # Clear existing data
        Pet.query.delete()
        db.session.commit()
        
        # CREATE operations
        print("1. CREATE Operations:")
        print("Creating pet1: Fido (Dog)")
        pet1 = Pet(name="Fido", species="Dog")
        print(f"Before adding to DB - ID: {pet1.id}, Name: {pet1.name}, Species: {pet1.species}")
        
        db.session.add(pet1)
        db.session.commit()
        print(f"After commit - ID: {pet1.id}, Name: {pet1.name}, Species: {pet1.species}")
        
        print("\nCreating pet2: Whiskers (Cat)")
        pet2 = Pet(name="Whiskers", species="Cat")
        db.session.add(pet2)
        db.session.commit()
        print(f"Pet2 - ID: {pet2.id}, Name: {pet2.name}, Species: {pet2.species}")
        
        # READ operations
        print("\n2. READ Operations:")
        print("All pets:", Pet.query.all())
        print("First pet:", Pet.query.first())
        
        # Filter operations
        print("\n3. FILTER Operations:")
        cats = Pet.query.filter(Pet.species == 'Cat').all()
        print("Cats:", cats)
        
        pets_starting_with_f = Pet.query.filter(Pet.name.startswith('F')).all()
        print("Pets starting with 'F':", pets_starting_with_f)
        
        # Filter_by operations
        print("\n4. FILTER_BY Operations:")
        cats_filter_by = Pet.query.filter_by(species='Cat').all()
        print("Cats (using filter_by):", cats_filter_by)
        
        pet_by_id = Pet.query.filter_by(id=1).first()
        print("Pet with ID 1:", pet_by_id)
        
        # Get operation
        print("\n5. GET Operations:")
        pet_get = db.session.get(Pet, 1)
        print("Pet with ID 1 (using get):", pet_get)
        
        pet_get_none = db.session.get(Pet, 20)
        print("Pet with ID 20 (should be None):", pet_get_none)
        
        # Order_by operations
        print("\n6. ORDER_BY Operations:")
        pets_ordered = Pet.query.order_by('species').all()
        print("Pets ordered by species:", pets_ordered)
        
        # Count operation
        print("\n7. COUNT Operations:")
        pet_count = db.session.query(func.count(Pet.id)).first()
        print("Total number of pets:", pet_count[0])
        
        # UPDATE operations
        print("\n8. UPDATE Operations:")
        print("Before update:", pet1)
        pet1.name = "Fido the mighty"
        db.session.commit()
        print("After update:", pet1)
        
        # DELETE operations
        print("\n9. DELETE Operations:")
        print("Before delete - All pets:", Pet.query.all())
        db.session.delete(pet1)
        db.session.commit()
        print("After deleting pet1:", Pet.query.all())
        
        # Delete all remaining pets
        remaining_count = Pet.query.delete()
        db.session.commit()
        print(f"Deleted {remaining_count} remaining pets")
        print("Final state - All pets:", Pet.query.all())
        
        print("\n=== CRUD Operations Test Complete ===")

if __name__ == "__main__":
    test_crud_operations()