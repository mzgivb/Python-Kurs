---
type: Notiz
date: 202207201430
status: published
folder: 190 - 🐍 Python
reviewed: no
tags:
  - Listen
  - python
---
# Listen in Python

Mithilfe von Listen kann man sich sparen viele Variablen zu einem Thema zu erstellen. 
Man kann auf die Listenelemente zugreifen, indem man ```[]``` auswählt. Eine Besonderheit ist, dass alle Listen mit 0 anfangen.

```python

enduro_fahrer = ["Carl", "Silas" , "Lynn", "Lion", "Justus", "Luca"]

print (enduro_fahrer[2]) # hier greift man auf Lynn zu
print (enduro_fahrer[4]) # hier greift man auf Justus zu



print ("im AMC sind folgende Fahrer flott unterwegs: " + (enduro_fahrer[0]) + " & "  +  (enduro_fahrer[4]))

enduro_fahrer = ["Carl", "Silas" , "Lynn", "Lion", "Justus", "Luca"]
enduro_fahrer.append("Jochen")

# mit der appendfunktion kann man Elemente zu einer Liste hinzufügen

print (enduro_fahrer)





```

## Wichtige Listen-Methoden

| Methode | Beschreibung | Beispiel |
|---------|-------------|----------|
| `append()` | Element am Ende hinzufügen | `liste.append("neu")` |
| `remove()` | Erstes Vorkommen entfernen | `liste.remove("Lynn")` |
| `pop()` | Letztes Element entfernen und zurückgeben | `liste.pop()` |
| `sort()` | Liste sortieren | `liste.sort()` |
| `reverse()` | Reihenfolge umkehren | `liste.reverse()` |
| `len()` | Anzahl der Elemente | `len(liste)` |

```python
# Beispiele für Listen-Methoden
zahlen = [5, 2, 8, 1, 9]

print(len(zahlen))      # Ausgabe: 5

zahlen.sort()
print(zahlen)           # Ausgabe: [1, 2, 5, 8, 9]

zahlen.reverse()
print(zahlen)           # Ausgabe: [9, 8, 5, 2, 1]

letztes = zahlen.pop()
print(letztes)          # Ausgabe: 1
print(zahlen)           # Ausgabe: [9, 8, 5, 2]
```

## Übungsaufgaben

1. Erstelle eine Liste mit 5 Städten.
2. Füge eine weitere Stadt hinzu mit `append()`.
3. Entferne eine Stadt mit `remove()`.
4. Sortiere die Liste alphabetisch.
5. Gib die Anzahl der Städte aus.
6. **Bonus:** Erstelle eine Liste mit Zahlen und filtere alle geraden Zahlen heraus.

---

## Lösungen

```python
# Aufgabe 1-5
staedte = ["Berlin", "München", "Hamburg", "Köln", "Frankfurt"]
staedte.append("Stuttgart")      # Aufgabe 2
staedte.remove("Hamburg")        # Aufgabe 3
staedte.sort()                   # Aufgabe 4
print(f"Anzahl Städte: {len(staedte)}")  # Aufgabe 5

# Bonus: Gerade Zahlen filtern
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade = [z for z in zahlen if z % 2 == 0]
print(gerade)  # Ausgabe: [2, 4, 6, 8, 10]
```

**Live Code**

https://colab.research.google.com/drive/1s3bi-Vzafc_T15_K2ZtPJCGDgA77nzyv?usp=sharing


