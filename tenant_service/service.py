import sys
sys.path.append('.')
from tenant_service.database import get_conn

class TenantService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def get_by_id(self, tenant_id):
        conn, cursor = get_conn()
        cursor.execute('SELECT * FROM Tenants WHERE tenID = ?', (tenant_id,))
        tenant = cursor.fetchone()
        conn.close()
        return dict(tenant) if tenant else None
    
    def get_all(self):
        conn, cursor = get_conn()
        cursor.execute('SELECT * FROM Tenants')
        tenants = cursor.fetchall()
        conn.close()
        return [dict(t) for t in tenants]
    
    def create(self, name):
        conn, cursor = get_conn()
        cursor.execute('INSERT INTO Tenants (name) VALUES (?)', (name,))
        conn.commit()
        tenant_id = cursor.lastrowid
        conn.close()
        return tenant_id