cislo = (input("zadej cislo: "))
hledanecislo = "1"
kolikrat = 0

for i in range(len(cislo)):
    if cislo[i] == hledanecislo:
        kolikrat = (kolikrat + 1)
print(kolikrat)
