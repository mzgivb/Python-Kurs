---
type: Notiz
ID: 202412120156
status: published
folder: 190 - 🐍 Python
reviewed: no
tags:
  - python
  - read
  - files
---

# Allgemeines Vorgehen: Dateien auslesen und bereinigen

Das Auslesen von Dateien in Python und die Verarbeitung der Inhalte zu einer Liste ist ein häufiger Anwendungsfall. Hier ist der allgemeine Ablauf:

## 1. Datei öffnen und Zeilen einlesen

Mit open() öffnest du eine Datei, und readlines() liest alle Zeilen der Datei ein und speichert sie in einer Liste.

Code-Beispiel:
```python
with open("dateiname.txt", "r") as file:
    zeilen = file.readlines()  # Jede Zeile wird als String in die Liste geschrieben
```
	•	zeilen ist jetzt eine Liste, in der jede Zeile aus der Datei ein eigener Eintrag ist.
	•	Das with-Statement stellt sicher, dass die Datei nach dem Lesen automatisch geschlossen wird.

## 2. Bereinigen der Zeilen

Beim Einlesen enthalten die Zeilen oft unerwünschte Leerzeichen oder Zeilenumbrüche.
Mit .strip() kannst du diese entfernen:

Code-Beispiel:
```python
bereinigte_zeilen = [zeile.strip() for zeile in zeilen]
```

	•	Hier wird eine List Comprehension verwendet, um jede Zeile in der Liste zu bereinigen.
	•	.strip() entfernt führende und nachfolgende Leerzeichen sowie \n (Zeilenumbrüche).

## 3. Die bereinigte Liste nutzen

Die bereinigten Zeilen kannst du nun weiterverarbeiten. Zum Beispiel:
	•	Ausgabe der Liste:
```python
for zeile in bereinigte_zeilen:
    print(zeile)


	•	Überprüfen, ob ein bestimmtes Element in der Liste ist:

if "Gesuchter Name" in bereinigte_zeilen:
    print("Name gefunden!")

````


4. Komplettes Beispiel

Angenommen, die Datei namen_liste.txt enthält:

Jochen
Carl
Silas
Manu
Egon

Der Code zum Auslesen, Bereinigen und Weiterverarbeiten könnte so aussehen:
```python
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
````

5. Ergebnisse und Verarbeitung

Wenn du die Datei erfolgreich eingelesen und bereinigt hast, kannst du die Liste vielseitig verwenden, z. B.:
	•	Filterung: Nur bestimmte Namen ausgeben.
	•	Manipulation: Namen zur Liste hinzufügen oder entfernen.
	•	Speichern: Änderungen zurück in die Datei schreiben.


