---
type: Notiz
ID: 202312060156
status: published
folder: 190 - 🐍 Python
reviewed: no
tags:
  - Schleifen
  - python
---

# Schleifen in Python

In Python können Sie Schleifen verwenden, um eine bestimmte Anweisung oder einen Codeblock mehrmals auszuführen. Es gibt zwei Hauptarten von Schleifen in Python: die `for`-Schleife und die `while`-Schleife.

Hier ist ein Beispiel für eine `for`-Schleife:

```python

for zahl in range(1, 6):
    print(zahl)

```

Dieser Code würde die Zahlen von 1 bis 5 ausgeben. Die `range(1, 6)` Funktion erzeugt eine Sequenz von Zahlen von 1 bis 5.

Und hier ist ein Beispiel für eine `while`-Schleife:

```python

zahl = 1
while zahl <= 5:
    print(zahl)
    zahl += 1


```

## Übungsaufgaben

### Aufgabe 1: Summe berechnen
Schreibe ein Programm, das die Summe aller Zahlen von 1 bis 100 berechnet und ausgibt.

### Aufgabe 2: Countdown
Schreibe eine `while`-Schleife, die von 10 bis 1 herunterzählt und am Ende "Start!" ausgibt.

### Aufgabe 3: Gerade Zahlen
Gib mit einer `for`-Schleife alle geraden Zahlen von 2 bis 20 aus.

### Aufgabe 4: Passwort-Abfrage
Schreibe ein Programm, das den Benutzer so lange nach einem Passwort fragt, bis er "geheim123" eingibt.

---

## Lösungen

```python
# Lösung Aufgabe 1: Summe berechnen
summe = 0
for zahl in range(1, 101):
    summe += zahl
print(f"Die Summe von 1 bis 100 ist: {summe}")

# Lösung Aufgabe 2: Countdown
countdown = 10
while countdown >= 1:
    print(countdown)
    countdown -= 1
print("Start!")

# Lösung Aufgabe 3: Gerade Zahlen
for zahl in range(2, 21, 2):  # Schrittweite 2
    print(zahl)

# Lösung Aufgabe 4: Passwort-Abfrage
passwort = ""
while passwort != "geheim123":
    passwort = input("Bitte Passwort eingeben: ")
print("Zugang gewährt!")
```

**Live Code**

https://colab.research.google.com/drive/1S4IV2uWPwm9nrkEcDy_flM83HEryr-pr?usp=sharing