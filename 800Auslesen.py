# Datei öffnen und Zeilen einlesen
with open("namen_liste.txt", "r") as file:
    zeilen = file.readlines()

# Zeilen bereinigen
bereinigte_zeilen = [zeile.strip() for zeile in zeilen]

# Bereinigte Zeilen ausgeben
print("Bereinigte Liste:")
for index, name in enumerate(bereinigte_zeilen, start=1):
    print(f"{index}. {name}")
    
    

# Überprüfen, ob ein Name vorhanden ist
suchname = input("Gib einen Namen ein, um zu prüfen, ob er in der Liste ist: ")
if suchname in bereinigte_zeilen:
    print("Der Name ist in der Liste.")
else:
    print("Der Name ist nicht in der Liste.")