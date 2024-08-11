class Borrar:
    def __init__(self):
        pass
    def borrar_tabla(self, conn, cursor):
        sql = 'DROP TABLE IF EXISTS FlightDetails'
        cursor.execute(sql)
        conn.commit()
        sql = 'DROP TABLE IF EXISTS Passenger'
        cursor.execute(sql)
        conn.commit()
        sql = 'DROP TABLE IF EXISTS Flight'
        cursor.execute(sql)
        conn.commit()
        sql = 'DROP TABLE IF EXISTS Airport'
        cursor.execute(sql)
        conn.commit()
        print('Las tabla se han eliminado correctamente')
        SQL_QUERY = ''' SELECT object_id, '['+SCHEMA_NAME(schema_id)+'].['+name+']' AS [schema_table], max_column_id_used, type, type_desc, create_date, modify_date, lock_escalation_desc FROM sys.tables '''
        cursor.execute(SQL_QUERY)
        tables = cursor.fetchall()
        for table in tables:
            print(table)
            pass