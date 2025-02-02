import matplotlib.pyplot as plt

# Datei lesen und Zeilen bereinigen
with open("zahlen.txt", "r") as file:
    zahlen = file.readlines()
bereinigte_zahlen = [zeile.strip() for zeile in zahlen if zeile.strip() != ""]

# Werte in float umwandeln
werte = [float(zahl) for zahl in bereinigte_zahlen]

# Plot erstellen
plt.plot(werte, marker='o', linestyle='-')
plt.xlabel("Index")
plt.ylabel("Wert")
plt.title("Werte aus zahlen.txt")
plt.show()
