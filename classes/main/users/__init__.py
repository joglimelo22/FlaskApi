from classes.db import DB

class USERS:

    @staticmethod

    def GET():
        return DB.request("SELECT * FROM users")
    
    def POST(name, usersname, password, permissionID):
        return DB.request(f"INSERT INTO users(name, username, password, permission_id, date_created) VALUE('{name}', '{usersname}', '{password}', '{permissionID}', NOW())")