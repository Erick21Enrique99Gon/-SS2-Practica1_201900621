import pyodbc
import pandas as pd
from modelo import ModeloBase
from borrar import Borrar
from cargar import Cargar

SERVER = 'localhost'
DATABASE = 'master'
USERNAME = 'sa'
PASSWORD = 'SQL#123@@'

global cursor
global conn

class LeerArchivo:
    def __init__(self):
        pass
    def leerCVS(self, ruta):
        leido = pd.read_csv(ruta)
        return leido
    def leer(self, ruta):
        f = open(ruta, "r")
        return f.read()
class MenuInicial:
    def __init__(self):
        self.datos = None
    
    def borrar_modelo(self):
        # Implementacion código para borrar el modelo de datos
        print ("Borrando modelo")
        borrar = Borrar()
        borrar.borrar_tabla(conn=conn, cursor=cursor)
        print ("Modelo borrado")
        pass
    
    def crear_modelo(self):
        # Implementacion código para crear el modelo de datos
        print ("Creando modelo")
        modelo = ModeloBase()
        print(cursor)
        modelo.crear_tabla(conn=conn,cursor=cursor)
        print ("Modelo creado")
        pass

    def extraer_informacion(self):
        # Implementacion código para extraer información de la base de datos
        print ("Extraer")
        print ("Ingresar ruta de archivos")
        ruta = "VuelosDataSet2.csv"#input()
        print ("Ruta de archivos", ruta)
        leer = LeerArchivo()
        self.datos = leer.leerCVS(ruta)

    def cargar_informacion(self):
        # Implementacion código para cargar información a la base de datos
        if self.datos is not None:
            self.datos.drop_duplicates(keep="first")
            self.datos.dropna()
            cargar = Cargar()
            for index,fila in self.datos.iterrows():
                cargar.cargar_datos(conn=conn, cursor=cursor, dato=fila)
        
        
        SQL_QUERY = 'SELECT * FROM Airport'
        cursor.execute(SQL_QUERY)
        result = cursor.fetchall()
        for row in result:
            print(row)

        SQL_QUERY = 'SELECT * FROM Flight'
        cursor.execute(SQL_QUERY)
        result = cursor.fetchall()
        for row in result:
            print(row)

        SQL_QUERY = 'SELECT * FROM FlightDetails'
        cursor.execute(SQL_QUERY)
        result = cursor.fetchall()
        for row in result:
            print(row)

        SQL_QUERY = 'SELECT * FROM Passenger'
        cursor.execute(SQL_QUERY)
        result = cursor.fetchall()
        for row in result:
            print(row)

    def realizar_consulta(self):
        # Implementacion código para realizar consultas a la base de datos
        pass
    def create_menu(self):
        while True:
            print
            print("1.Borrar modelo")
            print("2.Crear modelo")
            print("3.Extraer informacion")
            print("4.Cargar informacion")
            print("5.Realizar consultas")
            print("6.Salir")
            selector = input("Seleccione una opcion \n->")
        
            if selector == '1':
                self.borrar_modelo()
            elif selector == '2':
                self.crear_modelo()
            elif selector == '3':
                self.extraer_informacion()
            elif selector == '4':
                self.cargar_informacion()
            # elif selector == '5':
            #     self.realizar_consultas()
            elif selector == '6':
                print("Salir")
                break

if __name__ == "__main__":
    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=YES;'
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
# #     SQL_QUERY ='''CREATE TABLE Employees (
# #     EmployeeID INT PRIMARY KEY,
# #     FirstName NVARCHAR(50),
# #     LastName NVARCHAR(50),
# #     BirthDate DATE,
# #     HireDate DATE,
# #     Position NVARCHAR(50),
# #     Salary DECIMAL(10, 2)
# # );'''
# #     cursor.execute(SQL_QUERY)
# #     conn.commit()
#     SQL_QUERY = ''' SELECT object_id, '['+SCHEMA_NAME(schema_id)+'].['+name+']' AS [schema_table], max_column_id_used, type, type_desc, create_date, modify_date, lock_escalation_desc 
# FROM sys.tables '''
#     cursor.execute(SQL_QUERY)
#     tables = cursor.fetchall()
#     for table in tables:
#         print(table)
    # conn.commit()
    menu = MenuInicial()
    menu.create_menu()
    print("Running")