# === EINFACHE FUNKTION ===

def auto():
    """Eine einfache Funktion ohne Parameter"""
    print("Audi 80")

auto()  # Funktion aufrufen

print()

# === FUNKTION MIT PARAMETERN UND RÜCKGABEWERT ===

def addieren(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück"""
    return a + b

ergebnis = addieren(3, 5)
print(f"3 + 5 = {ergebnis}")

print()

# === FUNKTION MIT STANDARDPARAMETER ===

def begruessung(name="Welt"):
    """Begrüßt eine Person, Standard ist 'Welt'"""
    print(f"Hallo, {name}!")

begruessung()          # Ausgabe: Hallo, Welt!
begruessung("Jochen")  # Ausgabe: Hallo, Jochen!

print()

# === FUNKTION ZUR BERECHNUNG ===

def quadrat(zahl):
    """Berechnet das Quadrat einer Zahl"""
    return zahl * zahl

print(f"4 zum Quadrat = {quadrat(4)}")
print(f"7 zum Quadrat = {quadrat(7)}")

print()

# === FUNKTION MIT BOOLEAN-RÜCKGABE ===

def ist_gerade(zahl):
    """Prüft ob eine Zahl gerade ist"""
    return zahl % 2 == 0

print(f"Ist 4 gerade? {ist_gerade(4)}")   # True
print(f"Ist 7 gerade? {ist_gerade(7)}")   # False

