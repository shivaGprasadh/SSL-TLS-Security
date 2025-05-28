
#!/usr/bin/env python3
"""
Database reset script - drops and recreates all tables
WARNING: This will delete all existing data!
"""

from app import create_app, db
import models

def reset_database():
    """Drop all tables and recreate them"""
    app = create_app()
    
    with app.app_context():
        print("WARNING: This will delete all existing data!")
        confirm = input("Are you sure you want to continue? Type 'yes' to proceed: ")
        
        if confirm.lower() != 'yes':
            print("Operation cancelled.")
            return False
            
        print("Dropping all tables...")
        try:
            # Drop all tables
            db.drop_all()
            print("All tables dropped successfully!")
            
            # Create all tables with current schema
            db.create_all()
            print("Database tables recreated successfully!")
            
            # Verify tables were created
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"Created tables: {tables}")
            
        except Exception as e:
            print(f"Error resetting database: {e}")
            return False
    
    return True

if __name__ == "__main__":
    reset_database()
