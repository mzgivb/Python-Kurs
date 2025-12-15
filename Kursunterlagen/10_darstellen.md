---
type: Notiz
ID: 202502021948
status: published
folder: 190 - 🐍 Python
reviewed: no
tags:
  - matplotlib
  - python
  - Datenvisualisierung
---

# Darstellung von Werten mit Matplotlib

Dieses Beispielskript zeigt, wie man numerische Werte aus einer Textdatei einliest, verarbeitet und mit Matplotlib grafisch darstellt. 

## Schritte im Überblick

1. **Datei einlesen:**  
   Mit `open("zahlen.txt", "r")` wird die Datei im Lesemodus geöffnet. `file.readlines()` liest alle Zeilen in eine Liste ein.

2. **Zeilen bereinigen:**  
   Jede Zeile wird mit der Methode `strip()` von führenden und nachgestellten Leerzeichen befreit. Leere Zeilen werden entfernt.

3. **Daten konvertieren:**  
   Die bereinigten Zeichenketten werden in Fließkommazahlen (`float`) umgewandelt. Dies ist erforderlich, da Matplotlib numerische Werte erwartet.

4. **Plot erstellen:**  
   Mit `plt.plot()` wird ein Liniendiagramm erstellt. Die x-Achse entspricht dem Index der Liste und die y-Achse den jeweiligen Wert.

5. **Plot anzeigen:**  
   `plt.show()` öffnet ein Fenster, in dem der erstellte Plot dargestellt wird.

## Beispielskript

```python
import matplotlib.pyplot as plt

# 1. Datei öffnen und Zeilen einlesen
with open("zahlen.txt", "r") as file:
    zahlen = file.readlines()

# 2. Zeilen bereinigen und leere Zeilen entfernen
bereinigte_zahlen = [zeile.strip() for zeile in zahlen if zeile.strip() != ""]

# 3. Umwandeln der bereinigten Zeichenketten in float-Zahlen
werte = [float(zahl) for zahl in bereinigte_zahlen]

# 4. Erstellen des Plots
plt.plot(werte, marker='o', linestyle='-')
plt.xlabel("Index")
plt.ylabel("Wert")
plt.title("Darstellung der Werte aus 'zahlen.txt'")

# 5. Anzeigen des Plots
plt.show()
```