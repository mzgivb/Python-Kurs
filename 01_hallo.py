# Das erste Python-Programm: Hallo Welt!

print("Hallo Welt")  # gibt Hallo Welt aus

# Variablen und String-Verkettung (alte Methode)
platzhalter = "dein Name"
print("Hallo " + platzhalter)  # gibt Hallo + deinen Namen aus

# f-Strings (moderne Methode - empfohlen!)
name = "Jochen"
print(f"Hallo {name}!")  # einfacher und lesbarer

# f-Strings mit Variablen und Berechnungen
alter = 25
print(f"{name} ist {alter} Jahre alt.")
print(f"In 10 Jahren ist {name} {alter + 10} Jahre alt.")
