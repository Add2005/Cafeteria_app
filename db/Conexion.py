import pyodbc
from dotenv import load_dotenv 
import os

load_dotenv()

server = os.getenv("DB_SERVER")
base = os.getenv("DB_NAME")
usuario = os.getenv("DB_USER")
psw = os.getenv("DB_PASSWORD")

con = (
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server={server};"
    f"Database={base};"
    f"UID={usuario};"
    f"PWD={psw};"
)

class Conexion:
    _instance = None
 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)    
            cls._instance.connection = pyodbc.connect(con)
            cls._instance.cursor = cls._instance.connection.cursor()
            print("Conexion Exitosa!")
        return cls._instance
        
    def Commit(self):
        Conexion.Commit()
        
    def Close(self):
        Conexion.Close()
        