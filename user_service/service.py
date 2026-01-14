import sys
sys.path.append('.')
from user_service.database import get_conn
import bcrypt

class UserService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def get_by_email(self, email):
        ##conn = get_db()
        ##cursor = conn.cursor()
        conn, cursor = get_conn()
        
        cursor.execute('SELECT * FROM Users WHERE email = ?', (email,))
        
        # print("UID:", user['uID'], "\nEmail", user['email'], "\nRole", user['role'], "\ntenID", user['tenID'])
    
        # print(type(user['uID']))
        # print(type(user['email']))
        # print(type(user['role']))
        # print(type(user['tenID']))
        
        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None
    
    def gen_hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt.encode())
        return hashed
    
    def verify_password(self, password, password_hash):
        return bcrypt.checkpw(password.encode(), password_hash.encode())
