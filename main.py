import random

print("🎯 Bienvenidos al juego: ¡Adivina el Número Secreto!")

numero_secreto = random.randint(1, 20)
print("He elegido un número entre 1 y 20. ¡Intenta adivinarlo!\n")

numero_usuario = None 

while numero_usuario != numero_secreto:

    try:
        numero_usuario = int(input("👉 Ingresa tu número: "))
    except:
        print("❌ Debes ingresar un número entero válido.\n")
        continue

    if numero_usuario < 1 or numero_usuario > 20:
        print("⚠️ El número debe estar entre 1 y 20.\n")
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