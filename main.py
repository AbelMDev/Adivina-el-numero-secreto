import random

print("🎯 Bienvenidos al juego: ¡Adivina el Número Secreto!")

jugar_otra_vez = "s"

while jugar_otra_vez.lower() == "s":

    # -------------------------
    #  SELECCIÓN DE DIFICULTAD
    # -------------------------
    print("\nSelecciona un nivel de dificultad:")
    print("1. Fácil (1–10)")
    print("2. Medio (1–20)")
    print("3. Difícil (1–50)")

    while True:
        try:
            nivel = int(input("👉 Elige una opción (1-3): "))
            if nivel == 1:
                limite_superior = 10
                break
            elif nivel == 2:
                limite_superior = 20
                break
            elif nivel == 3:
                limite_superior = 50
                break
            else:
                print("❌ Opción inválida. Debe ser 1, 2 o 3.")
        except:
            print("❌ Ingresa un número válido.")

    # -------------------------
    #      GENERAR SECRETO
    # -------------------------
    numero_secreto = random.randint(1, limite_superior)
    intentos_restantes = 5

    print(f"\nHe elegido un número entre 1 y {limite_superior}.")
    print("Tienes solo 5 intentos. ¡Buena suerte!\n")

    acertado = False

    # -------------------------
    #        BUCLE DEL JUEGO
    # -------------------------
    while intentos_restantes > 0:

        print(f"Intentos restantes: {intentos_restantes}")

        try:
            numero_usuario = int(input("👉 Ingresa tu número: "))
        except:
            print("❌ Debes ingresar un número entero válido.\n")
            continue

        if numero_usuario < 1 or numero_usuario > limite_superior:
            print(f"⚠️ El número debe estar entre 1 y {limite_superior}.\n")
            continue

        if numero_usuario == numero_secreto:
            print(f"🎉 ¡Felicidades! Adivinaste el número secreto ({numero_secreto})")
            acertado = True
            break
        elif numero_usuario > numero_secreto:
            print("🔻 El número secreto es más pequeño.\n")
        else:
            print("🔺 El número secreto es más grande.\n")

        intentos_restantes -= 1

    # -------------------------
    #       RESULTADO FINAL
    # -------------------------
    if not acertado:
        print(f"💥 Te quedaste sin intentos. El número era {numero_secreto}.")

    # -------------------------
    #     JUGAR OTRA VEZ
    # -------------------------
    jugar_otra_vez = input("\n🔁 ¿Quieres jugar otra vez? (s/n): ")

print("\n👋 ¡Gracias por jugar!")
