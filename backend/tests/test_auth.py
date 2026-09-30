import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_register():
    """Test user registration"""
    response = client.post(
        "/auth/register",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == "test@example.com"


def test_register_duplicate_email():
    """Test that duplicate email registration fails"""
    # First registration
    client.post(
        "/auth/register",
        json={
            "name": "User 1",
            "email": "duplicate@example.com",
            "password": "password123"
        }
    )
    
    # Duplicate registration
    response = client.post(
        "/auth/register",
        json={
            "name": "User 2",
            "email": "duplicate@example.com",
            "password": "password456"
        }
    )
    assert response.status_code == 409


def test_login():
    """Test user login"""
    # Register user
    client.post(
        "/auth/register",
        json={
            "name": "Login Test",
            "email": "login@example.com",
            "password": "password123"
        }
    )
    
    # Login
    response = client.post(
        "/auth/login",
        json={
            "email": "login@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == "login@example.com"


def test_login_wrong_password():
    """Test that login fails with wrong password"""
    # Register user
    client.post(
        "/auth/register",
        json={
            "name": "Wrong Pass Test",
            "email": "wrongpass@example.com",
            "password": "correct_password"
        }
    )
    
    # Login with wrong password
    response = client.post(
        "/auth/login",
        json={
            "email": "wrongpass@example.com",
            "password": "wrong_password"
        }
    )
    assert response.status_code == 401


# Cleanup
def teardown_module():
    """Clean up test database after tests"""
    import os
    if os.path.exists("./test.db"):
        os.remove("./test.db")
