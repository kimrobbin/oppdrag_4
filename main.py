from db import *


# sql_statement = "INSERT INTO varer (varenummer, navn, pris, antall, katogori) VALUES (%s, %s, %s, %s, %s)"
# valus = ("1001", "Kamera", 2000, 30, "elektronikk")
# mycursor.execute(sql_statement, valus)

# dbconn.commit()

def print_ui():
    print("--------------------------------------------------------------")
    print("Velkommen til Varehaandteringssystemet")
    print("1. Legg til en ny vare")
    print("2. Vis alle varer")
    print("3. Oppdater en vare")
    print("4. Slett en vare")
    print("5. Avslutt")
    print("--------------------------------------------------------------")



while True:

    print_ui()


    userinput = input("Velg mellom 1-5: ")

    if userinput == "1":
        varenummer = input("Varenummer:")
        navn = input("Navn:")
        pris = input("Pris:")
        antall = input("Antall:")
        katagori = input(" A) Elektonikk B) kontor C) Klaer")
        if katagori == "A" or "a":
            katagori = "Elektronikk"
        elif katagori == "B" or "b":
            katagori = "Kontor"
        elif katagori == "C" or "c":
            katagori = "Klaer"
        
        sql_statement = "INSERT INTO varer (varenummer, navn, pris, antall, katogori) VALUES (%s, %s, %s, %s, %s)"
        valus = (varenummer, navn, pris, antall, katagori)
        mycursor.execute(sql_statement, valus)
        dbconn.commit()
    
        
    if userinput == "2":
        sql_statement = "SELECT * FROM varer"
        mycursor.execute(sql_statement)
        result = mycursor.fetchall()
        
        print("--------------------------------------------------------------")
        for row in result:
            print(row)
            
            
    if userinput == "3":
        varenummer = input("Varenummer:")
        navn = input("Navn:")
        pris = input("Pris:")
        antall = input("Antall:")
        katagori = input(" A) Elektonikk B) kontor C) Klaer")
        if katagori == "A" or "a":
            katagori = "Elektronikk"
        elif katagori == "B" or "b":
            katagori = "Kontor"
        elif katagori == "C" or "c":
            katagori = "Klaer"
        
        sql_statement = "UPDATE varer SET navn=%s, pris=%s, antall=%s, katogori=%s WHERE varenummer=%s"
        mycursor.execute(sql_statement, (navn, pris, antall, katagori, varenummer))
        dbconn.commit()
        

    if userinput == "5":
        print("Avslutter")
        quit()