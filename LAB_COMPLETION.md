# Flask-SQLAlchemy CRUD Lab - Completed

## Lab Completion Summary

✅ **Completed all lab requirements:**

### 1. Database Setup
- Initialized Flask-SQLAlchemy database with `flask db init`
- Created initial migration with `flask db migrate -m "Initial migration."`
- Applied migration with `flask db upgrade head`
- Successfully created `pets` table with `id`, `name`, and `species` columns

### 2. CRUD Operations Implemented and Tested
All operations from the lab have been implemented and tested:

#### CREATE Operations
- `Pet()` - Create new pet instances
- `db.session.add()` - Add pets to database session
- `db.session.commit()` - Commit transactions to persist data

#### READ Operations
- `Pet.query.all()` - Get all pets
- `Pet.query.first()` - Get first pet
- `Pet.query.filter()` - Filter with boolean expressions
- `Pet.query.filter_by()` - Filter by column values
- `db.session.get(Pet, id)` - Get pet by primary key
- `Pet.query.order_by()` - Sort results
- `func.count()` - Count records

#### UPDATE Operations
- Modify object attributes and commit changes
- Demonstrated with updating pet name from "Fido" to "Fido the mighty"

#### DELETE Operations
- `db.session.delete()` - Delete specific records
- `Pet.query.delete()` - Delete all records
- Both operations require `db.session.commit()`

### 3. Testing
- Created comprehensive test script (`test_crud.py`) that demonstrates all CRUD operations
- All operations working correctly as verified by test output

### 4. Git Integration
- Repository initialized and connected to GitHub
- All changes committed and pushed to remote repository
- Database files properly ignored via `.gitignore`

## Key Learning Outcomes Achieved
- ✅ Used Flask-SQLAlchemy to simplify ORM tasks
- ✅ Managed database tables and schemas without writing SQL
- ✅ Used Flask Shell context for database operations
- ✅ Implemented complete CRUD functionality
- ✅ Understanding of database sessions and transactions

## Files Created/Modified
- `server/app.py` - Flask application with SQLAlchemy setup
- `server/models.py` - Pet model definition
- `server/migrations/` - Database migration files
- `test_crud.py` - Comprehensive CRUD operations test
- `LAB_COMPLETION.md` - This completion summary

## How to Run
1. Install dependencies: `pipenv install` (or use pip directly)
2. Navigate to server directory: `cd server`
3. Set environment variables:
   ```bash
   export FLASK_APP=app.py
   export FLASK_RUN_PORT=5555
   ```
4. Run migrations (if needed):
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade head
   ```
5. Test CRUD operations: `python ../test_crud.py`
6. Or use Flask shell: `flask shell`

## Repository
GitHub: https://github.com/Breechelugui/python-p4-v2-flask-sqlalchemy-crud-shell