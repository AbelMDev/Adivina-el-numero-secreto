import random

def jugar():

    print("🎯 Bienvenidos al juego: ¡Adivina el Número Secreto!")

    print("\nNiveles de dificultad:")
    print("1. Fácil (1–10)")
    print("2. Medio (1–20)")
    print("3. Difícil (1–50)")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        minimo, maximo = 1, 10
    elif opcion == "2":
        minimo, maximo = 1, 20
    elif opcion == "3":
        minimo, maximo = 1, 50
    else:
        print("❌ Opción inválida. Se usará dificultad media.")
        minimo, maximo = 1, 20

   
    numero_secreto = random.randint(minimo, maximo)

    print(f"He elegido un número entre {minimo} y {maximo}. ¡Intenta adivinarlo!\n")

    numero_usuario = None 

    while numero_usuario != numero_secreto:

        try:
            numero_usuario = int(input("👉 Ingresa tu número: "))
        except:
            print("❌ Debes ingresar un número entero válido.\n")
            continue

        if numero_usuario < minimo or numero_usuario > maximo:
            print(f"⚠️ El número debe estar entre {minimo} y {maximo}.\n")
            continue

        if numero_usuario == numero_secreto:
            print(f"🎉 ¡Felicidades! Adivinaste el número secreto ({numero_secreto})")
        elif numero_usuario > numero_secreto:
            print("🔻 El número secreto es más pequeño.\n")
        else:
            print("🔺 El número secreto es más grande.\n")


jugar_otra_vez = "s"
while jugar_otra_vez.lower() == "s":
    jugar()
    jugar_otra_vez = input("\n🔁 ¿Quieres jugar otra vez? (s/n): ")

print("\n👋 ¡Gracias por jugar!")
