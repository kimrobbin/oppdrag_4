from db import *
import os


# sql_statement = "INSERT INTO varer (varenummer, navn, pris, antall, katogori) VALUES (%s, %s, %s, %s, %s)"
# valus = ("1001", "Kamera", 2000, 30, "elektronikk")
# mycursor.execute(sql_statement, valus)

# dbconn.commit()

def print_ui():
    os.system("cls")
    print("--------------------------------------------------------------")
    print("Velkommen til Varehaandteringssystemet")
    print("1. Legg til en ny vare")
    print("2. Vis alle varer")
    print("3. Finn en vare")
    print("4. Oppdater en vare")
    print("5. Slett en vare")
    print("6. Avslutt")
    print("--------------------------------------------------------------")
    userinput = input("Velg mellom 1-5: ")
    return userinput

def ny_vare():
    os.system("cls")
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

def alle_varer():
    os.system("cls")
    sql_statement = "SELECT * FROM varer"
    mycursor.execute(sql_statement)
    result = mycursor.fetchall()

    
    for row in result:
        print(row)
    2
    Continue = input("Press enter to continue")
    if Continue == "":
        print_ui()   

def finn_en_vare():
    os.system("cls")
    varenummer = input("Varenummer:")
    sql_statement = "SELECT * FROM varer WHERE varenummer=%s"
    mycursor.execute(sql_statement, (varenummer,))
    result = mycursor.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("Ingen varer funnet med det varenummeret.")
    
    Continue = input("Press enter to continue")
    if Continue == "":
        print_ui()

def finn_Oppdater_en_vare():
    os.system("cls")
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
    
    
    Continue = input("Press enter to continue")
    if Continue == "":
        print_ui()

userinput = print_ui()



if userinput == "1":
    
    ny_vare()
    
    
elif userinput == "2":
    
    alle_varer()
    
        
elif userinput == "3":
    finn_en_vare()
        
        
elif userinput == "4":
    finn_Oppdater_en_vare()
    

elif userinput == "6":
    print("Avslutter")
    quit()
    

