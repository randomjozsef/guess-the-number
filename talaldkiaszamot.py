import random

while True:
  options = ("0","1","2","3","4")

  y = random.choice(options)
  x = None

  while x not in options:
    x = input("Válassz egy számot 0 és 4 között: ")

  if y < x:
    print("Az én számom: " + y)
    print("A te számod: " + x)
    print("Nyertél!")

  elif y > x:
    print("Az én számom: " + y)
    print("A te számod: " + x)
    print("Vesztettél!")

  elif y == x:
    print("Az én számom: " + y)
    print("A te számod: " + x)
    print("Döntetlen!")

  újra = input("Újra akarod próbálni?: ").lower()
  if újra != "igen":
    break
print("Viszlát!")
