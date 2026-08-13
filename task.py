rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

perdiste = '''
         /")
        |) /|
        |   |
        |   |
        |>*<|
        |   |
     /')|   |/')
 /')|   |   |   |
|   |   |   |   |)
|   |   |   |   |  )
| *   *   *   * |>  >      
|                  /
 |               /
  |            /
   )          |
    |         |
'''

import random
opciones = ["Piedra", "Papel", "Tijeras"]
opciones_ascii = [rock, paper, scissors, perdiste]

print("Bienvenido a Piedra, Papel o Tijeras!")
#Eleccion del usuario
mano_usuario = int(input(f"Escribe 0 para elegir {opciones[0]}, 1 para {opciones[1]}, o 2 para {opciones[2]}. "))

#Respuesta a la eleccion del usuario
if 0 <= mano_usuario <= 2:
    print(f"Elegiste {opciones[mano_usuario]}")
    print(opciones_ascii[mano_usuario])

    #Eleccion del bot
    mano_bot = random.randint(0,2)
    print(f"El bot eligió {opciones[mano_bot]}")
    print(opciones_ascii[mano_bot])

    #Comparacion de manos
    if ((mano_usuario == 0 and mano_bot == 2) or (mano_usuario == 1 and mano_bot == 0)
            or (mano_usuario == 2 and mano_bot == 1)):
        print("Ganaste!")
    elif mano_usuario == mano_bot:
        print("Empate!")
    else:
        print("Perdiste.")

else:
    print("Muy chistoso. Esa opcion no existe. Perdiste")
    print(perdiste)