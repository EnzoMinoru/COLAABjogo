import random
cor_secreta = random.choice(['R','G','B'])
palpite = input("Adivinhe a cor (R, G, B): ").upper()
if palpite not in ['R','G','B']:
  print("Entrada inválida. Escolha R, G ou B.")
elif palpite == cor_secreta:
  print("Parabens! voce acertou!")
else:
  print('voce errou')