import pytest
import sys
sys.path.append('.')
from problem_service.app import app
from problem_service.auth import SECRET_KEY
import jwt
import datetime

@pytest.fixture

#HTTP status codes key: 200 OK
#                       201 Created, For e.g. a new entry in the database
#                       400 Bad Request, An error in the client input e.g. No '@' symbol in an email entry field
#                       401 Unauthorised: No valid JWT token in the header
#                       404 Requested resource could not be found, e.g. if searching for an id that there is no match for.

def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture

def auth_token():
    token = jwt.encode({
        'uID': 1,
        'email': 'test@barclays.com',
        'role': 'consumer',
        'tenID': 1,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm='HS256')
    
    return token

def test_create_problem_success(client, auth_token):
    response = client.post('/problems',
        json={'title': 'Test Problem', 'desc': 'This is a test description'},
        headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 201
    assert 'probID' in response.get_json()

def test_create_problem_no_token(client):
    response = client.post('/problems',
        json={'title': 'Test Problem'})
    
    assert response.status_code == 401

def test_create_problem_missing_title(client, auth_token):
    response = client.post('/problems',
        json={'desc': 'Description only'},
        headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Title is required'

def test_create_problem_title_too_long(client, auth_token):
    response = client.post('/problems',
        json={'title': 'x' * 51},
        headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Title must be 50 characters or less'

def test_get_problems_success(client, auth_token):
    response = client.get('/problems',
        headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_problems_no_token(client):
    response = client.get('/problems')
    assert response.status_code == 401
    
def test_get_problem_by_uID_success(client, auth_token):
    response = client.get('/problems/1',
        headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert 'probID' in response.get_json()

def test_get_problem_by_uID_not_found(client, auth_token):
    response = client.get('/problems/9999',
        headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 404

def test_update_status_success(client, auth_token):
    response = client.patch('/problems/1',
        json={'status': 'Closed'},
        headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Status updated'

def test_update_status_missing_status(client, auth_token):
    response = client.patch('/problems/1',
        json={},
        headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 400

def test_update_status_not_found(client, auth_token):
    response = client.patch('/problems/9999',
        json={'status': 'Closed'},
        headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 404