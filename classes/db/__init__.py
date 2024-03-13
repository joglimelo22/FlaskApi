import mysql.connector

class DB:

    def __init__(self):
        self.ip = "localhost"
        self.user = "xerp"
        self.password = "Xerp@123"
        self.port = "3306"
        self.database = "xerp"


    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                host = self.ip,
                user = self.user,
                password = self.password,
                port = self.port,
                database = self.database
            )

            self.cursor = self.cnx.cursor(dictionary=True)

            return {"status": 200, "message": "Conectado ao banco de dados"}

        except Exception as error:
            return {"status": 400, "message": f"Houve um erro ao conectar ao banco, Erro: {error}"}

    def disconnect(self):

        try:
            self.cnx.close()

            return {"status": 200, "message": "Disconectado do banco"}

        except Exception as error:
            return {"status": 400, "message": f"Houve um erro ao desconectar ao banco, Erro: {error}"}
        

    def query(self, query):
        try:
            self.cursor.execute(query)

            if "SELECT" in query:
                return {"status": 200, "message": self.cursor.fetchall()}
            else:
                self.cnx.commit()
                return {"status": 200, "message": "Os dados foram editados/aterados com sucesso"}
        
        except Exception as error:
            return {"status": 400, "message": f"Houve um erro, erro: {error}"}




    @staticmethod

    def request(query):
        db = DB()
        connectDB = db.connect()
        if connectDB["status"] == 400:
            return connectDB
        
        return db.query(query)
        
