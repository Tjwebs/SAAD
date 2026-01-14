from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
sys.path.append('.')
from tenant_service.service import TenantService

#HTTP status codes key: 200 OK
#                       201 Created, For e.g. a new entry in the database
#                       400 Bad Request, An error in the client input e.g. No '@' symbol in an email entry field
#                       401 Unauthorised: No valid JWT token in the header
#                       404 Requested resource could not be found, e.g. if searching for an id that there is no match for.

app = Flask(__name__)
#In full production this would need to be restricted e.g. CORS(app, origins=['https://CMS.com'])
CORS(app)

tenant_service = TenantService()

@app.route('/tenants', methods=['GET'])
def get_tenants():
    tenants = tenant_service.get_all()
    return jsonify(tenants), 200

@app.route('/tenants/<int:tenant_id>', methods=['GET'])
def get_tenant(tenant_id):
    tenant = tenant_service.get_by_id(tenant_id)
    if not tenant:
        return jsonify({'error': 'Tenant not found'}), 404
    return jsonify(tenant), 200

@app.route('/tenants', methods=['POST'])
def create_tenant():
    data = request.get_json()
    name = data.get('name')
    
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    
    tenant_id = tenant_service.create(name)
    return jsonify({'message': 'Tenant created', 'tenID': tenant_id}), 201

if __name__ == '__main__':
    app.run(port=5003, debug=True)