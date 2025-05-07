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
    userinput = input("Velg mellom 1-6: ")
    return userinput

def strek():
    print("--------------------------------------------------------------")

def ny_vare():
    os.system("cls")
    varenummer = input("Varenummer:")
    navn = input("Navn:")
    pris = input("Pris:")
    antall = input("Antall:")
    katagori = input(" A) Elektonikk B) kontor C) Klaer")
    if katagori == "A" or katagori =="a":
        katagori = "Elektronikk"
    elif katagori == "B" or katagori == "b":
        katagori = "Kontor"
    elif katagori == "C" or katagori == "c":
        katagori = "Klaer"
    
    sql_statement = "INSERT INTO varer (varenummer, navn, pris, antall, katogori) VALUES (%s, %s, %s, %s, %s)"
    valus = (varenummer, navn, pris, antall, katagori)
    mycursor.execute(sql_statement, valus)
    dbconn.commit()

def alle_varer():
    os.system("cls")
    print("LAGERLISTE")
    strek()
    valg = input(" Velg mellom: A) Vis alle Varer, B) Elektronikk, C) Kontor, D) Klaer")
    if valg == "A" or valg == "a":
        sql_statement = "SELECT * FROM varer"
        mycursor.execute(sql_statement)
        result = mycursor.fetchall()
        
        if mycursor.rowcount > 0:
            for row in result:
                print(row)
        else:
            print("Ingen varer funnet")
            
            
                
        print("Alle varer")
        
    elif valg == "B" or valg == "b":
        sql_statement = "SELECT * FROM varer WHERE katogori='Elektronikk'"
        mycursor.execute(sql_statement)
        result = mycursor.fetchall()
        
        if mycursor.rowcount > 0:
            print("Alle varer i Elektronikk")
            strek()
            for row in result:
                print(row)
            strek()
        else:
            print("Ingen varer funnet")
            
        
    elif valg == "C" or valg == "c":
        sql_statement = "SELECT * FROM varer WHERE katogori='Kontor'"
        mycursor.execute(sql_statement)
        result = mycursor.fetchall()
        
        if mycursor.rowcount > 0:
            print("Alle varer i Kontor")
            strek()
            for row in result:
                print(row)
            strek()
        else:
            print("Ingen varer funnet")
            
            
            
        
    elif valg == "D" or valg == "d":
        sql_statement = "SELECT * FROM VARER WHERE katogori='Klaer'"
        mycursor.execute(sql_statement)
        result = mycursor.fetchall()
        
        if mycursor.rowcount > 0:
            strek()
            print("Alle varer i Klaer")
            strek()
            for row in result:
                print(row)
            strek()
        else:
            print("Ingen varer funnet")
    
    
    input("Press enter to continue")
     

def finn_en_vare():
    os.system("cls")
    varenummer = input("Varenummer:")
    sql_statement = "SELECT * FROM varer WHERE varenummer=%s"
    mycursor.execute(sql_statement, (varenummer,))
    result = mycursor.fetchall()
    if result:
        for row in result:
            print(row)
        strek()
    else:
        print("Ingen varer funnet med det varenummeret.")
    
    input("Press enter to continue")
    

def Oppdater_en_vare():
    os.system("cls")
    varenummer = input("Varenummer:")
    navn = input("Navn:")
    pris = input("Pris:")
    antall = input("Antall:")
    
    
    sql_statement = "UPDATE varer SET navn=%s, pris=%s, antall=%s,  WHERE varenummer=%s"
    mycursor.execute(sql_statement, (navn, pris, antall, varenummer))
    dbconn.commit()
    
    input("Press enter to continue")
  
def slett_vare():
    os.system("cls")
    varenummer = input("Varenummer:")
    sql_statement = "DELETE FROM varer WHERE varenummer=%s"
    mycursor.execute(sql_statement, (varenummer,))
    dbconn.commit()
    if mycursor.rowcount > 0:
        print("Vare slettet")
    else:
        print("Ingen varer funnet med det varenummeret.")
    
    input("Press enter to continue")




while True:
    userinput = print_ui()
    
    if userinput == "1":
        ny_vare()
        
        
    elif userinput == "2":
        alle_varer()
        
            
    elif userinput == "3":
        finn_en_vare()
            
            
    elif userinput == "4":
        Oppdater_en_vare()
        
    elif userinput == "5":
        slett_vare()


    elif userinput == "6":
        print("Avslutter")
        quit()
    else: 
        print(" Ugyldig valg")

