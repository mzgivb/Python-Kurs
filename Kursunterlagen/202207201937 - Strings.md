---
type: Notiz
date: 202207201430
status: published
folder: 190 - 🐍 Python
reviewed: no
tags:
  - strings
  - python
---
# Strings in Python

*Wichtig!*: 

Mit **Strings** kann man Zeichenketten, sprich Wörter oder Text in einem Programm ausgeben. Man muss dabei beachten, dass der + Operator hier eine andere Funktion hat. Er entspricht  nicht der mathematischen Addition wie bei Zahlen, aus diesem Grund muss man darauf achten, Zahlen in **Strings** anzugeben bzw. sie mit der *str (Funktion)* umzuwandeln.



```python

print ("Hallo Welt")

Hallo Welt

name = " Max "
print ("Ich bin: " + name)

Ich bin: Max

print ("Ich bin: " +"4")

Ich bin : 4

age = 22
print ("ich bin: " + str(age))

Ich bin : 22





```

## f-Strings (empfohlen!)

Seit Python 3.6 gibt es **f-Strings** - eine einfachere und lesbarere Methode, Variablen in Text einzufügen:

```python
name = "Max"
age = 22

# Alte Methode mit + (umständlich)
print("Ich bin " + name + " und " + str(age) + " Jahre alt.")

# Neue Methode mit f-String (einfacher!)
print(f"Ich bin {name} und {age} Jahre alt.")
```

**Vorteile von f-Strings:**
- Kein `+` zum Verketten nötig
- Keine `str()` Umwandlung bei Zahlen nötig
- Variablen stehen direkt in `{geschweiften Klammern}`
- Das `f` vor dem String aktiviert diese Funktion

```python
# Weitere Beispiele
preis = 19.99
print(f"Der Artikel kostet {preis} Euro.")

# Man kann sogar rechnen in f-Strings!
a = 5
b = 3
print(f"{a} + {b} = {a + b}")
```

**Live Code**

https://colab.research.google.com/drive/13ZXuThkclgcI1u8-T7WI2BRU_6UnHWNs?usp=sharing



