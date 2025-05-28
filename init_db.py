
#!/usr/bin/env python3
"""
Database initialization script
Run this to create all required tables
"""

from app import create_app, db
import models

def init_database():
    """Initialize the database with all required tables"""
    app = create_app()
    
    with app.app_context():
        print("Creating database tables...")
        try:
            # Drop all tables first (optional - remove if you want to keep existing data)
            # db.drop_all()
            
            # Create all tables
            db.create_all()
            print("Database tables created successfully!")
            
            # Verify tables were created
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"Created tables: {tables}")
            
        except Exception as e:
            print(f"Error creating database tables: {e}")
            return False
    
    return True

if __name__ == "__main__":
    init_database()
