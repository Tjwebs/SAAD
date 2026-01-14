import pytest
import sys
sys.path.append('.')
from user_service.app import app

#HTTP status codes key: 200 OK
#                       201 Created, For e.g. a new entry in the database
#                       400 Bad Request, An error in the client input e.g. No '@' symbol in an email entry field
#                       401 Unauthorised: No valid JWT token in the header
#                       404 Requested resource could not be found, e.g. if searching for an id that there is no match for.

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post('/login', 
        json={'email': 'test@barclays.com', 'password': 'password123'})
    assert response.status_code == 200
    assert 'token' in response.get_json()

def test_login_missing_fields(client):
    response = client.post('/login', 
        json={'email': 'test@barclays.com'})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Email and password required'

def test_login_wrong_password(client):
    response = client.post('/login', 
        json={'email': 'test@barclays.com', 'password': 'wrongpassword'})
    assert response.status_code == 401
    assert response.get_json()['error'] == 'Invalid credentials'

def test_login_nonexistent_user(client):
    response = client.post('/login', 
        json={'email': 'nobody@test.com', 'password': 'password123'})
    assert response.status_code == 401
    assert response.get_json()['error'] == 'Invalid credentials'