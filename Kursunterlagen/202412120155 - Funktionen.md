---
type: Notiz
ID: 202412120156
status: published
folder: 190 - 🐍 Python
reviewed: no
tags:
  - python
  - funktionen
---

Python-Funktionen: Kurzer Überblick

Was sind Funktionen?
	•	Funktionen sind wiederverwendbare Code-Blöcke, die eine bestimmte Aufgabe ausführen.
	•	Sie helfen, den Code zu organisieren, lesbar zu machen und Wiederholungen zu vermeiden.
	•	Funktionen werden mit dem Schlüsselwort def definiert.

Aufbau einer Funktion:

def funktionsname(parameter):
    # Funktionskörper
    return rückgabewert

	•	def: Definiert die Funktion.
	•	funktionsname: Der Name der Funktion, der sie beschreibt.
	•	parameter: Optional, ermöglicht der Funktion, Daten entgegenzunehmen.
	•	return: Gibt einen Wert zurück (optional).

Beispiel:

# Funktion, die zwei Zahlen addiert
```python
def addiere(zahl1, zahl2):
    ergebnis = zahl1 + zahl2
    return ergebnis

# Aufruf der Funktion
summe = addiere(3, 5)
print(summe)  # Ausgabe: 8
```


## Aufgaben

1. Schreibe eine Funktion `quadrat`, die eine Zahl als Parameter entgegennimmt und das Quadrat dieser Zahl zurückgibt.
2. Teste die Funktion mit den Zahlen 4 und 7 und gib die Ergebnisse aus.
3. Schreibe eine Funktion `ist_gerade`, die prüft, ob eine Zahl gerade ist (gibt `True` oder `False` zurück).
4. Schreibe eine Funktion `begruessung`, die einen Namen als Parameter nimmt und einen Standardwert "Welt" hat.

---

## Lösungen

```python
# Lösung Aufgabe 1 & 2: Quadrat-Funktion
def quadrat(zahl):
    return zahl * zahl

print(quadrat(4))  # Ausgabe: 16
print(quadrat(7))  # Ausgabe: 49

# Lösung Aufgabe 3: Gerade Zahl prüfen
def ist_gerade(zahl):
    return zahl % 2 == 0

print(ist_gerade(4))   # Ausgabe: True
print(ist_gerade(7))   # Ausgabe: False
print(ist_gerade(10))  # Ausgabe: True

# Lösung Aufgabe 4: Begrüßung mit Standardparameter
def begruessung(name="Welt"):
    print(f"Hallo, {name}!")

begruessung()          # Ausgabe: Hallo, Welt!
begruessung("Jochen")  # Ausgabe: Hallo, Jochen!
```

## Tipps für gute Funktionen

- **Eine Aufgabe pro Funktion**: Jede Funktion sollte nur eine Sache tun
- **Sprechende Namen**: Der Name sollte verraten, was die Funktion macht
- **Kurz halten**: Wenn eine Funktion zu lang wird, aufteilen

Viel Erfolg!