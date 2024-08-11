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

        sql = '''
        DECLARE @AirportCountryCode NVARCHAR(5) = '{}';
        DECLARE @CountryName NVARCHAR(50) = '{}';
        DECLARE @AirportContinent NVARCHAR(5) = '{}';
        DECLARE @Continent NVARCHAR(50) = '{}';
        DECLARE @AirportName NVARCHAR(50) = '{}';
        
        IF EXISTS (
            SELECT 1
            FROM Airport
            WHERE AirportCountryCode = @AirportCountryCode
            AND CountryName = @CountryName
            AND AirportContinent = @AirportContinent
            AND Continent = @Continent
            AND AirportName = @AirportName
        )
        
        BEGIN
            PRINT 'El valor existe en la columna.';
            -- Aquí puedes realizar otras acciones si el valor existe
        END
        ELSE
        BEGIN
            PRINT 'El valor no existe en la columna.';
            -- Aquí puedes realizar otras acciones si el valor no existe
            
            INSERT INTO Airport (AirportCountryCode, CountryName, AirportContinent, Continent,AirportName)
            VALUES (@AirportCountryCode, @CountryName, @AirportContinent, @Continent,@AirportName);
        END'''.format(dato['Airport Country Code'],dato['Country Name'].replace("'", "''"),dato['Airport Continent'],dato['Continents'].replace("'", "''"),dato['Airport Name'].replace("'", "''")) 
        print(sql)
        cursor.execute(sql)
        conn.commit()

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
        DECLARE @AirportCountryCode NVARCHAR(5) = '{}';
        DECLARE @CountryName NVARCHAR(50) = '{}';
        DECLARE @AirportContinent NVARCHAR(5) = '{}';
        DECLARE @Continent NVARCHAR(50) = '{}';
        DECLARE @AirportName NVARCHAR(50) = '{}';
        
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

        
        DECLARE @AirportID INT = (
            SELECT AirportID
            FROM Airport
            WHERE AirportCountryCode = @AirportCountryCode
            AND CountryName = @CountryName
            AND AirportContinent = @AirportContinent
            AND Continent = @Continent
            AND AirportName = @AirportName
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
            
            INSERT INTO FlightDetails (PassengerID,FlightID, AirportID) VALUES (@PassengerID,@FlightID,@AirportID);
        END'''.format(dato['First Name'].replace("'", "''"),dato['Last Name'].replace("'", "''"),dato['Age'],dato['Gender'],dato['Nationality'],
                    dato['Departure Date'],dato['Arrival Airport'].replace("'", "''"),dato['Pilot Name'].replace("'", "''"),dato['Flight Status'],
                    dato['Airport Country Code'],dato['Country Name'].replace("'", "''"),dato['Airport Continent'],dato['Continents'].replace("'", "''"),dato['Airport Name'].replace("'", "''")) 
        print(sql)
        cursor.execute(sql)
        conn.commit()