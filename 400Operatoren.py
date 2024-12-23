a = 6
b = 3
c = a + b

print(c)

d = a * b

print(d)

e = a / b

print(e)

# Beispiel Vergleichsoperatoren

alter = 20
punkte = 120

if alter >= 18 and punkte >= 100:
    print("Teilnahme erlaubt")
else:
    print("Teilnahme nicht erlaubt")

# Beispiel Modulo Operator - prüfen ob eine Zahl gerade oder ungerade ist

zahl = int(input("Gib eine Zahl ein: "))

if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
