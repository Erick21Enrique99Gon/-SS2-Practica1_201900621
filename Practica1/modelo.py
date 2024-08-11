class ModeloBase:
    def __init__(self):
        pass

    def pruebab(self):
        print("Prueba")
    def crear_tabla(self, conn, cursor):
        sql = '''
        CREATE TABLE Passenger (
            PassengerID INT IDENTITY(1,1) PRIMARY KEY,
            Gender NVARCHAR(7),
            Nationality NVARCHAR(50),
            FirstName NVARCHAR(50),
            LastName NVARCHAR(50),
            Age INT,
        )
        
        CREATE TABLE Flight (
            FlightID INT IDENTITY(1,1) PRIMARY KEY,
            DepartureDate Date,
            ArrivalAirport NVARCHAR(50),
            PilotName NVARCHAR(50),
            FlightStatus NVARCHAR(15)
        )
        
        CREATE TABLE Airport (
            AirportID INT IDENTITY(1,1) PRIMARY KEY,
            AirportCountryCode NVARCHAR(5),
            CountryName NVARCHAR(50),
            AirportContinent NVARCHAR(5),
            Continent NVARCHAR(50),
            AirportName NVARCHAR(50)
        )
        
        CREATE TABLE FlightDetails (
            FlightDetailsID INT IDENTITY(1,1) PRIMARY KEY,
            PassengerID INT,
            FlightID INT,
            AirportID INT,
            FOREIGN KEY (PassengerID) REFERENCES Passenger(PassengerID),
            FOREIGN KEY (FlightID) REFERENCES Flight(FlightID),
            FOREIGN KEY (AirportID) REFERENCES Airport(AirportID)
        )
        '''
        cursor.execute(sql)
        conn.commit()
        
        SQL_QUERY = ''' SELECT object_id, '['+SCHEMA_NAME(schema_id)+'].['+name+']' AS [schema_table], max_column_id_used, type, type_desc, create_date, modify_date, lock_escalation_desc FROM sys.tables '''
        cursor.execute(SQL_QUERY)
        tables = cursor.fetchall()
        for table in tables:
            print(table)
            pass
    