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
word = random.sample(categorias[categoria], len(categorias[categoria]))
w=word.pop(0)
guessed = []
attempts = 6
puntaje= 0
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
  progress = ""
  for letter in w:
    if letter in guessed:
      progress += letter + " "
    else:
      progress += "_ "
  print(progress)
# Verificar si el jugador ya adivinó la palabra completa
  if "_" not in progress:
    puntaje +=6 
    print("¡Ganaste!")
    guessed=[]
    if len(word) == 0:
        print("No quedan más palabras en esta categoría")
        break
    w=word.pop(0)
  print(f"Intentos restantes: {attempts}")
  print(f"Letras usadas: {', '.join(guessed)}")
  letter = input("Ingresá una letra: ")
  if not letter.isalpha():
      print("entrada no valida")
      continue
  elif len(letter) != 1:
      print("entrada no valida")
      continue
  elif letter in guessed:
    print("Ya usaste esa letra.")
  elif letter in w:
    guessed.append(letter)
    print("¡Bien! Esa letra está en la palabra.")
  else:
    guessed.append(letter)
    attempts -= 1
    puntaje -=1
    print("Esa letra no está en la palabra.")
  print()
else:
  puntaje=0
  print(f"¡Perdiste! La palabra era: {w}")
print(f"el puntaje es: {puntaje}")