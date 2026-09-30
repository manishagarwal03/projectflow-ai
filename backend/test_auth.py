#!/usr/bin/env python3
"""Test authentication to debug login issues."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.services.auth_service import verify_password
from app.models.user import User

def test_authentication(email: str, password: str):
    """Test if password verification works for a user."""
    # Create database connection
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # Find user
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            print(f"❌ User not found with email: {email}")
            return False
        
        print(f"✓ User found: {user.name} ({user.email})")
        print(f"  Status: {user.status}")
        print(f"  Hash (first 50 chars): {user.password_hash[:50]}...")
        print(f"  Hash length: {len(user.password_hash)}")
        
        # Test password verification
        print(f"\nTesting password: '{password}'")
        is_valid = verify_password(password, user.password_hash)
        
        if is_valid:
            print("✅ Password verification PASSED")
        else:
            print("❌ Password verification FAILED")
        
        return is_valid
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python test_auth.py <email> <password>")
        sys.exit(1)
    
    email = sys.argv[1]
    password = sys.argv[2]
    
    result = test_authentication(email, password)
    sys.exit(0 if result else 1)
