import pyodbc
from dotenv import load_dotenv 
import os

load_dotenv()

#Conexion db
server = os.getenv("DB_SERVER")
base = os.getenv("DB_NAME")
usuario = os.getenv("DB_USER")
pwd = os.getenv("DB_PASSWORD")

#Conexion db con reportes
driver = os.getenv("DRIVER_REPORTS")
jdbc_driver = os.getenv("JDBC_REPORTS")
port = os.getenv("PORT")

con = (
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server={server};"
    f"Database={base};"
    f"UID={usuario};"
    f"PWD={pwd};"
)

def Conexion():
    try:
        conexion = pyodbc.connect(con)
        return conexion
    except Exception as ex:
        print(f"Error {ex.args[0]}" )
        return None

# Conexion Reportes:
# Implementacion de los reportes AQUI
# TENER INSTALADO JDK 21 LINK: https://download.oracle.com/java/21/archive/jdk-21.0.7_windows-x64_bin.exe
# CONFIGURAR VARIABLES DE ENTORNO PARA JAVA21 
# WINDIR--->AGREGAR: "JAVA_HOME = " 
#def ConexionReportes():
#     return {
#         f'driver': '{driver}', 
#         f'username': '{usuario}',
#         f'password': '{pwd}',
#         f'jdbc_driver': '{jdbc_driver}',
#         f'jdbc_url': "jdbc:sqlserver://{server}:{port};databaseName={base};encrypt=false;trustServerCertificate=true;",
# }

# ESTO FUERA MAS FACIL CON DOCKER
# EN UN FUTURO DEBERIAMOS DE CREAR UN CONTENEDOR CON LA APP
# Y TAMBIEN LA BD, PARA PODER HACER EL SISTEMA PORTABLE 
 