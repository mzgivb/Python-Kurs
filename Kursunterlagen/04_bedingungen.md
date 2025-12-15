---
type: Notiz
ID: 202312060150
status: published
folder: 190 - 🐍 Python
reviewed: no
tags:
  - Bedingungen
  - python
---

# Bedingungen in Python

In Python können Sie Bedingungen mit `if`, `elif` (optional) und `else` (optional) erstellen. Diese Bedingungen ermöglichen es Ihrem Code, unterschiedliche Aktionen basierend auf bestimmten Kriterien auszuführen. Hier ist ein einfaches Beispiel:


```python

alter = 18  # Ändern Sie den Wert auf Ihr Alter

if alter < 18:
    print("Sie sind minderjährig.")
elif alter == 18:
    print("Sie sind genau 18 Jahre alt.")
else:
    print("Sie sind volljährig.")



```

### Hier ist deine erste Aufgabe zum Thema Bedingungen:

1. Aufgabe:
Schreibe ein Programm, das eine Zahl vom Benutzer abfragt und überprüft, ob die Zahl größer, kleiner oder gleich 10 ist. Gib je nach Bedingung eine entsprechende Nachricht aus, z. B.:
	•	“Die Zahl ist größer als 10.”
	•	“Die Zahl ist kleiner als 10.”
	•	“Die Zahl ist gleich 10.”


2. Aufgabe:
Schreibe ein Programm, das das Alter einer Person abfragt und ausgibt, ob sie:
	•	ein Kind (unter 12 Jahre),
	•	ein Teenager (12 bis 17 Jahre),
	•	ein Erwachsener (18 Jahre oder älter) ist.

Gib eine entsprechende Nachricht aus, z. B.:
	•	“Du bist ein Kind.”
	•	“Du bist ein Teenager.”
	•	“Du bist ein Erwachsener.”


3. Aufgabe: Bestimmung der Notenstufe

Schreibe ein Programm, das eine Zahl von 0 bis 100 einliest (z. B. eine Prüfungsnote) und dann die entsprechende Notenstufe ausgibt. Verwende dazu Bedingungen.

Die Notenstufen sind wie folgt:
	•	100-90 → “Sehr gut”
	•	89-80 → “Gut”
	•	79-70 → “Befriedigend”
	•	69-60 → “Ausreichend”
	•	59-0 → “Nicht bestanden”

Zusätzliche Anforderungen:
	1.	Wenn die Zahl nicht zwischen 0 und 100 liegt, soll das Programm eine Fehlermeldung ausgeben: "Ungültige Eingabe! Bitte eine Zahl zwischen 0 und 100 eingeben."
	2.	Verwende if-elif-else Bedingungen.
	3.	Die Eingabe soll über die Funktion input() erfolgen, und das Ergebnis soll ausgegeben werden.

https://colab.research.google.com/drive/1kvbeKbEoH515keeeSqwJqcjTSsdVYVZC?usp=sharing
