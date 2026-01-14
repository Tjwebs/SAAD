import pytest
import sys
sys.path.append('.')
from tenant_service.app import app

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

def test_get_tenants(client):
    response = client.get('/tenants')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_tenant_by_id(client):
    response = client.get('/tenants/1')
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Barclays'

def test_get_tenant_not_found(client):
    response = client.get('/tenants/9999')
    assert response.status_code == 404
