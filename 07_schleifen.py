# === FOR-SCHLEIFEN ===

# Iteration über einen String
wort = "Python"
for buchstabe in wort:
    print(buchstabe)

print()  # Leerzeile

# Iteration über eine Liste
früchte = ["Apfel", "Banane", "Kirsche"]
for frucht in früchte:
    print(frucht)

print()

# for-Schleife mit range
for a in range(3, 9):
    print(a)

print()

# === WHILE-SCHLEIFEN ===

# Zählen von 1 bis 5
zahl = 1
while zahl <= 5:
    print(zahl)
    zahl += 1

print()

# Countdown
countdown = 10
while countdown >= 1:
    print(countdown)
    countdown -= 1
print("Start!")

print()

# === BREAK UND CONTINUE ===

# break beendet die Schleife vorzeitig
print("Beispiel break:")
for zahl in range(1, 11):
    if zahl == 5:
        break  # Schleife wird bei 5 abgebrochen
    print(zahl)

print()

# continue überspringt den aktuellen Durchlauf
print("Beispiel continue:")
for zahl in range(1, 11):
    if zahl == 5:
        continue  # 5 wird übersprungen
    print(zahl)
