from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
sys.path.append('.')
from problem_service.auth import decode_token
from problem_service.service import ProblemService

#HTTP status codes key: 200 OK
#                       201 Created, For e.g. a new entry in the database
#                       400 Bad Request, An error in the client input e.g. No '@' symbol in an email entry field
#                       401 Unauthorised: No valid JWT token in the header
#                       404 Requested resource could not be found, e.g. if searching for an id that there is no match for.

app = Flask(__name__)
#In full production this would need to be restricted e.g. CORS(app, origins=['https://CMS.com'])
CORS(app)

problemService = ProblemService()

@app.route('/problems', methods=['POST'])

def create_problem():
    
    payload, error = decode_token(request.headers.get('Authorization'))
    if error:
        return jsonify({'error': error}), 401
    
    data = request.get_json()
    title = data.get('title')
    desc = data.get('desc')
    
    if not title:
        return jsonify({'error': 'Title is required'}), 400
    if len(title) > 50:
        return jsonify({'error': 'Title must be 50 characters or less'}), 400
    
    problem_id = problemService.create(title, desc, payload['uID'], payload['tenID'])
    
    return jsonify({'message': 'Problem created', 'probID': problem_id}), 201


@app.route('/problems', methods=['GET'])

def get_problems():
    payload, error = decode_token(request.headers.get('Authorization'))
    if error:
        return jsonify({'error': error}), 401
    
    problems = problemService.get_all_uID(payload['uID'], payload['tenID'])
    
    return jsonify(problems), 200


@app.route('/problems/<int:problem_id>', methods=['GET'])

def get_problem(problem_id):
    payload, error = decode_token(request.headers.get('Authorization'))
    if error:
        return jsonify({'error': error}), 401
    
    problem = problemService.get_by_pID(problem_id, payload['tenID'])
    
    if not problem:
        return jsonify({'error': 'Problem not found'}), 404
    
    return jsonify(problem), 200


@app.route('/problems/<int:problem_id>', methods=['PATCH'])

def update_status(problem_id):
    payload, error = decode_token(request.headers.get('Authorization'))
    if error:
        return jsonify({'error': error}), 401
    
    data = request.get_json()
    status = data.get('status')
    
    if not status:
        return jsonify({'error': 'Status is required'}), 400
    
    updated = problemService.update_status(problem_id, status, payload['tenID'])
    
    if not updated:
        return jsonify({'error': 'Problem not found'}), 404
    
    return jsonify({'message': 'Status updated'}), 200


if __name__ == '__main__':
    app.run(port=5002, debug=True)