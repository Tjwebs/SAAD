from flask import Flask, request, jsonify
import sys
sys.path.append('.')
from shared.database import get_db, get_conn
from shared.auth import decodeToken

app = Flask(__name__)

@app.route('/problems', methods=['POST'])
def create_problem():
    
    payload, error = decodeToken(request.headers.get('Authorization'))
    
    if error:
        return jsonify({'error': error}), 401
    
    data = request.get_json()
    title = data.get('title')
    desc = data.get('desc')
    
    if not title:
        return jsonify({'error': 'Title is required'}), 400
    if len(title) > 50:
        return jsonify({'error': 'Title must be 50 characters or less'}), 400
    if desc and len(desc) < 10:
        return jsonify({'error': 'Description must be at least 10 characters'}), 400
    
    ##conn = get_db()
    ##cursor = conn.cursor()
    conn, cursor = get_conn()
    
    cursor.execute('''
                   INSERT INTO Problems (creatorID, tenID, title, desc)
                   VALUES (?, ?, ?, ?)
                   ''', 
                   (payload['uID'], payload['tenID'], title, desc)
                   )
    
    conn.commit()
    probID = cursor.lastrowid
    conn.close()
    
    return jsonify({
        'message': 'Problem created',
        'probID': probID
    }), 201
    
@app.route('/problems', methods=['GET'])
def get_problems_tenID():
    
    payload, error = decodeToken(request.headers.get('Authorization'))
    if error:
        return jsonify({'error': error}), 401
    
    ##conn = get_db()
    ##cursor = conn.cursor()
    conn, cursor = get_conn()    
    cursor.execute('''
                   SELECT * FROM Problems WHERE tenID = ?
                   ''', (payload['tenID'],))
    
    problems = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(p) for p in problems]), 200

if __name__ == '__main__':
    app.run(port=5002, debug=True) 