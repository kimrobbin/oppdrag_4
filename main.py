from db import *


sql_statement = "INSERT INTO varer (varenummer, navn, pris, antall, katogori) VALUES (%s, %s, %s, %s, %s)"
valus = ("1001", "Kamera", 2000, 30, "elektronikk")
mycursor.execute(sql_statement, valus)

dbconn.commit()