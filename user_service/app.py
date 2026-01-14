from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
sys.path.append('.')
from user_service.auth import SECRET_KEY
from user_service.service import UserService
import jwt
import datetime

#HTTP status codes key: 200 OK
#                       201 Created, For e.g. a new entry in the database
#                       400 Bad Request, An error in the client input e.g. No '@' symbol in an email entry field
#                       401 Unauthorised: No valid JWT token in the header
#                       404 Requested resource could not be found, e.g. if searching for an id that there is no match for.

app = Flask(__name__)
#In full production this would need to be restricted e.g. CORS(app, origins=['https://CMS.com'])
CORS(app)

user_service = UserService()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    user = user_service.get_by_email(email)
    
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401
    
    if not user_service.verify_password(password, user['passHash']):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    token = jwt.encode({
        'uID': user['uID'],
        'email': user['email'],
        'role': user['role'],
        'tenID': user['tenID'],
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)
    }, SECRET_KEY, algorithm='HS256')
    
    return jsonify({'token': token}), 200


if __name__ == '__main__':
    app.run(port=5001, debug=True)