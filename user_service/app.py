from flask import Flask, request, jsonify
import sys
sys.path.append('.')
from shared.database import get_db, get_conn
from shared.auth import SECRET_KEY
import bcrypt
import jwt
import datetime

app = Flask(__name__)

@app.route('/login', methods = ['POST'])

def login():
    
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    print("Email:", email, "Password:", password)
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    
    ##conn = get_db()
    ##cursor = conn.cursor()
    conn, cursor = get_conn()
    cursor.execute('SELECT * FROM Users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    
    print("UID:", user['uID'], "\nEmail", user['email'], "\nRole", user['role'], "\ntenID", user['tenID'])
    
    print(type(user['uID']))
    print(type(user['email']))
    print(type(user['role']))
    print(type(user['tenID']))
    
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401
    if not bcrypt.checkpw(password.encode(), user['passHash'].encode()):
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