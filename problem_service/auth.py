import os
import jwt

SECRET_KEY = os.environ.get('SECRET_KEY', 'rodentS4551')


def decode_token(auth_header):
    
    if not auth_header or not auth_header.startswith('Bearer '):
        return None, 'Token Required'
    
    token = auth_header.split(' ')[1]
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload, None
    except jwt.ExpiredSignatureError:
        return None, 'Token Expired'
    except jwt.InvalidTokenError:
        return None, 'Invalid Token'