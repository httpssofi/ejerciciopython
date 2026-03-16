import random
words = [
  "python",
  "programa",
  "variable",
  "funcion",
  "bucle",
  "cadena",
  "entero",
   "lista",
]
categorias = {
  "cortas": ["python", "bucle", "lista"],
  "medianas": ["entero", "cadena", "funcion"],
  "largas": ["programa", "variable"]
}
categoria = input("Elige una categoría, cortas, medianas o largas: ")
word = random.choice(categorias[categoria])
guessed = []
attempts = 6
puntaje= 0
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
  progress = ""
  for letter in word:
    if letter in guessed:
      progress += letter + " "
    else:
      progress += "_ "
  print(progress)
# Verificar si el jugador ya adivinó la palabra completa
  if "_" not in progress:
    puntaje +=6
    print("¡Ganaste!")
    word = random.choice(categorias[categoria])
    categorias[categoria].remove(word)
    break
  print(f"Intentos restantes: {attempts}")
  print(f"Letras usadas: {', '.join(guessed)}")
  letter = input("Ingresá una letra: ")
  if not letter.isalpha():
      print("entrada no valida")
  elif len(letter) != 1:
      print("entrada no valida")
  elif letter in guessed:
    print("Ya usaste esa letra.")
  elif letter in word:
    guessed.append(letter)
    puntaje +=1
    print("¡Bien! Esa letra está en la palabra.")
  else:
    guessed.append(letter)
    attempts -= 1
    puntaje -=1
    print("Esa letra no está en la palabra.")
  print()
else:
  puntaje=0
  print(f"¡Perdiste! La palabra era: {word}")
print(f"el puntaje es: {puntaje}")