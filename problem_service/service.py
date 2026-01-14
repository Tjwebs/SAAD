import sys
sys.path.append('.')
from problem_service.database import get_conn

class ProblemService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def create(self, title, desc, creator_id, tenant_id):
        conn, cursor = get_conn()
        
        cursor.execute('''
            INSERT INTO Problems (creatorID, tenID, title, desc)
            VALUES (?, ?, ?, ?)
        ''', (creator_id, tenant_id, title, desc))
        
        conn.commit()
        problem_id = cursor.lastrowid
        conn.close()
        return problem_id
    
    def get_all_uID(self, uID, tenID):
        conn, cursor = get_conn()
        
        cursor.execute('SELECT * FROM Problems WHERE creatorID = ? AND tenID = ?', (uID, tenID))
        
        problems = cursor.fetchall()
        conn.close()
        return [dict(p) for p in problems]
    
    def get_by_pID(self, problem_id, tenID):
        conn, cursor = get_conn()
        
        cursor.execute('SELECT * FROM Problems WHERE probID = ? AND tenID = ?', 
                       (problem_id, tenID))
        
        problem = cursor.fetchone()
        conn.close()
        return dict(problem) if problem else None
    
    
    def update_status(self, problem_id, status, tenID):
        conn, cursor = get_conn()
        
        cursor.execute('UPDATE Problems SET status = ? WHERE probID = ? AND tenID = ?',
                       (status, problem_id, tenID))
        
        conn.commit()
        rows_affected = cursor.rowcount
        conn.close()
        return rows_affected > 0
