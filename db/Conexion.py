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

def Conexion():
    try:
        conexion = pyodbc.connect(con)
        print("Correcto")
        return conexion
    except Exception as ex:
        print(f"Error {ex.args[0]}" )
        return None

