class Cargar:
    def __init__(self):
        pass
    
    def cargar_datos(self, conn, cursor, dato):
        sql = '''
        DECLARE @firstName NVARCHAR(50) = '{}';
        DECLARE @lastName NVARCHAR(50) = '{}';
        DECLARE @Age INT = {};
        DECLARE @Gender NVARCHAR(7) = '{}';
        DECLARE @Nationality NVARCHAR(50) = '{}';
        
        IF EXISTS (
            SELECT 1
            FROM Passenger
            WHERE FirstName = @firstName AND LastName = @lastName AND Age = @Age AND Gender = @Gender AND Nationality = @Nationality
        )
        
        BEGIN
            PRINT 'El valor existe en la columna.';
            -- Aquí puedes realizar otras acciones si el valor existe
        END
        ELSE
        BEGIN
            PRINT 'El valor no existe en la columna.';
            -- Aquí puedes realizar otras acciones si el valor no existe
            
            INSERT INTO Passenger (FirstName, LastName, Age, Gender,Nationality) VALUES (@firstName, @lastName,@Age, @Gender,@Nationality);
        END'''.format(dato['First Name'].replace("'", "''"),dato['Last Name'].replace("'", "''"),dato['Age'],dato['Gender'],dato['Nationality']) #First Name,Last Name,Age
        print(sql)
        cursor.execute(sql)
        conn.commit()

        sql = '''
        DECLARE @DepartureDate Date = '{}';
        DECLARE @ArrivalAirport NVARCHAR(50) = '{}';
        DECLARE @PilotName NVARCHAR(50) = '{}';
        DECLARE @FlightStatus NVARCHAR(15) = '{}';
        
        IF EXISTS (
            SELECT 1
            FROM Flight
            WHERE DepartureDate = @DepartureDate 
            AND ArrivalAirport = @ArrivalAirport 
            AND PilotName = @PilotName
            AND FlightStatus = @FlightStatus
        )
        
        BEGIN
            PRINT 'El valor existe en la columna.';
            -- Aquí puedes realizar otras acciones si el valor existe
        END
        ELSE
        BEGIN
            PRINT 'El valor no existe en la columna.';
            -- Aquí puedes realizar otras acciones si el valor no existe
            
            INSERT INTO Flight (DepartureDate, ArrivalAirport, PilotName, FlightStatus) VALUES (@DepartureDate, @ArrivalAirport, @PilotName , @FlightStatus);
        END'''.format(dato['Departure Date'],dato['Arrival Airport'].replace("'", "''"),dato['Pilot Name'].replace("'", "''"),dato['Flight Status']) 
        print(sql)
        cursor.execute(sql)
        conn.commit()

        # sql = '''DECLARE @firstFind NVARCHAR(50) = '{}';
        # DECLARE @lastFind NVARCHAR(50) = '{}';
        # DECLARE @AgeFind INT = {};
        # DECLARE @DepartureDateFind Date = '{}';
        
        # DECLARE @GenderId INT = (SELECT GenderID
        # FROM Gender
        # WHERE Gender = '{}');
        
        # DECLARE @NationalityID INT = (SELECT NationalityID
        # FROM Nationality
        # WHERE Nationality = '{}');
        
        # DECLARE @PassengerID INT = (SELECT PassengerID
        # FROM Passenger
        # WHERE FirstName = @firstFind AND LastName = @lastFind AND Age = @AgeFind AND GenderId = @GenderId AND NationalityID = @NationalityID);
        
        # IF EXISTS (
        #     SELECT 1
        #     FROM Flight
        #     WHERE DepartureDate = @DepartureDateFind AND PassengerID = @PassengerID
        # )
        
        # BEGIN
        #     PRINT 'El valor existe en la columna.';
        #     -- Aquí puedes realizar otras acciones si el valor existe
        # END
        # ELSE
        # BEGIN
        #     PRINT 'El valor no existe en la columna.';
        #     -- Aquí puedes realizar otras acciones si el valor no existe
            
        #     INSERT INTO Flight (DepartureDate,PassengerID) VALUES (@DepartureDateFind,@PassengerID);
        # END'''.format(dato['First Name'].replace("'", "''"),dato['Last Name'].replace("'", "''"),dato['Age'],dato['Departure Date'],dato['Gender'],dato['Nationality']) #First Name,Last Name,Age
        # print(sql)
        # cursor.execute(sql)
        # conn.commit() 

        sql = '''
        DECLARE @firstName NVARCHAR(50) = '{}';
        DECLARE @lastName NVARCHAR(50) = '{}';
        DECLARE @Age INT = {};
        DECLARE @Gender NVARCHAR(7) = '{}';
        DECLARE @Nationality NVARCHAR(50) = '{}';
        DECLARE @DepartureDate Date = '{}';
        DECLARE @ArrivalAirport NVARCHAR(50) = '{}';
        DECLARE @PilotName NVARCHAR(50) = '{}';
        DECLARE @FlightStatus NVARCHAR(15) = '{}';
        
        DECLARE @PassengerID INT = (
            SELECT PassengerID
            FROM Passenger
            WHERE FirstName = @firstName AND LastName = @lastName AND Age = @Age AND Gender = @Gender AND Nationality = @Nationality
        )

        
        DECLARE @FlightID INT = (
            SELECT FlightID
            FROM Flight
            WHERE DepartureDate = @DepartureDate 
            AND ArrivalAirport = @ArrivalAirport 
            AND PilotName = @PilotName
            AND FlightStatus = @FlightStatus
        )

        IF EXISTS (
            SELECT 1
            FROM FlightDetails
            WHERE PassengerID = @PassengerID
        )
        BEGIN
            PRINT 'El valor existe en la columna.';
            -- Aquí puedes realizar otras acciones si el valor existe
        END
        ELSE
        BEGIN
            PRINT 'El valor no existe en la columna.';
            -- Aquí puedes realizar otras acciones si el valor no existe
            
            INSERT INTO FlightDetails (PassengerID,FlightID) VALUES (@PassengerID,@FlightID);
        END'''.format(dato['First Name'].replace("'", "''"),dato['Last Name'].replace("'", "''"),dato['Age'],dato['Gender'],dato['Nationality'],
                    dato['Departure Date'],dato['Arrival Airport'].replace("'", "''"),dato['Pilot Name'].replace("'", "''"),dato['Flight Status']) 
        print(sql)
        cursor.execute(sql)
        conn.commit()

        # # Obtener y mostrar el mensaje
        # cursor.execute("SELECT @@ROWCOUNT")
        # result = cursor.fetchall()
        # for row in result:
        #     print("Filas afectadas: ", row[0])
        
        # SQL_QUERY = 'SELECT * FROM Gender'
        # cursor.execute(SQL_QUERY)
        # result = cursor.fetchall()
        # for row in result:
        #     print(row)
        
        # SQL_QUERY = '''INSERT INTO Gender (Gender) VALUES (?);'''