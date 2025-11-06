
hemligt_tal = 7

print("Gissa talet mellan 1 och 10!")

gissning = int(input("Skriv en gissning: "))

if gissning == hemligt_tal:
    print("Rätt!!!")
else:
    print("Fel!")

print("Det rätta talet var:", hemligt_tal)
