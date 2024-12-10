
#Was ist eine Liste?

	#•	Eine Liste ist ein geordnetes, veränderbares Daten­struktur-Objekt in Python.
	#•	Sie kann verschiedene Datentypen enthalten (Strings, Zahlen, sogar andere Listen).


# Beispiele

meine_liste = ["Apfel", "Banane", "Kirsche"]
zahlen_liste = [1, 2, 3, 4, 5]
gemischt = ["Text", 42, True]


print(meine_liste[0])  # "Apfel"
print(meine_liste[-1]) # Letztes Element: "Kirsche"


meine_liste[1] = "Birne"
print(meine_liste) # ["Apfel", "Birne", "Kirsche"]


meine_liste.append("Orange")      # Fügt am Ende hinzu
meine_liste.insert(1, "Melone")   # Fügt an bestimmter Stelle hinzu

#Entfernen von Elementen

meine_liste.remove("Apfel") # entfernt erstes Vorkommen von "Apfel"
letztes_element = meine_liste.pop() # entfernt und gibt das letzte Element zurück

# Nützliche Methoden

print(len(meine_liste))  # Länge der Liste
meine_liste.sort()       # Sortiert die Liste (wenn Datentypen vergleichbar sind)
meine_liste.reverse()    # Dreht die Reihenfolge um

# Beispielaufgabe:

Vater = input(str("Bitte gebe den Vornamen deines Vaters ein: "))
Mutter = input(str("bitte gebe den Vornamen deiner Mutter ein: "))

liste = [ Vater , "Carl" , Mutter ]
Nachname = input(str("Bitte gebe deinen Nachnamen ein:"))
print ("dein Vater heisst", liste[0], Nachname)
print ("deine Mutter heisst", liste[2],Nachname)







