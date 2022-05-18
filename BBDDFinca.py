import pyodbc

cnxn_str = ("Driver={SQL Server};"
            "Server=DESKTOP-01U3L4M;"
            "Database=CentroMedico;"
            "Trusted_Connection=yes;")

cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()
cursor.execute("CREATE TABLE DatosFinca")
cnxn.commit()
cnxn.close()