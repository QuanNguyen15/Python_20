def connections():
    import pyodbc

    print(pyodbc.drivers())

    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                                SERVER=DESKTOP-9HGBU5H\SQLEXPRESS; '
                                'Database=QLTKBSV; UID=mq; PWD=151611')

    cursor = connection.cursor()
    # for row in cursor.execute("select * from ACCOUNT"):
    #     print(row.username)
    #     print(row[0])
    #     print(row)

    cursor.execute("select * from ACCOUNT")
    # cursor.execute("insert ACCOUNT values('quan', '54321')")

    a = 'Tram'
    b = '06-10-2011'

    cursor.execute("insert ACCOUNT values(?, ?)", a, b)

    connection.commit()

    data = cursor.fetchall()

    print(data)
    connection.close()


connections()
