import random

print("Tente adivinhar o número que estou pensando!")
chutes = 1
lista = range(1,100)
secreto = random.choice(lista)
print(secreto)
while True:
    numero = int(input("Seu chute: "))
    if numero == secreto:
        break
    elif numero < secreto:
        print("Você deve chutar mais alto.")
    else:
        print("Você deve chutar mais baixo.")
    chutes += 1
print("Parabéns, você acertou!")
print(f"Número de chutes: {chutes}")