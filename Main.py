import random
qnt = 5
maximo = 250
cura = 50
class Persona:
  def __init__(self, nome, dano, vida, classe):
    self.nome = nome
    self.dano = dano
    self.vida = vida
    self.classe = classe
  def atk(self, alvo):
      if self.classe == "HomemBomba":
        if random.randint(1, 4) == 1:
          self.vida -= self.dano / 2
        alvo.vida -= self.dano
      else:
        alvo.vida -= self.dano
player = Persona("Bombinha", 100, 250, "HomemBomba")
rei = Persona("Rei esqueleto", 25, 500, None)
while True:
  try:
    print("=" * 50)
    print("1 - Atacar")
    print("2 - Curar-se")
    print("0 - Sair")
    op = int(input(">> "))
    if op == 1:
      player.atk(rei)
    elif op == 2:
      if qnt <= 0:
        print("Pocao insuficiente")
      else:
        qnt -= 1
        player.vida += cura
      if player.vida > maximo:
        player.vida = maximo
    elif op == 0:
        break
    rei.atk(player)
    print(f"Sua vida: {player.vida} | Monstro vida: {rei.vida}")
    if rei.vida <= 0:
      print("Voce ganhou!")
      break
    if player.vida <= 0:
      print("voce morreu.")
      break
  except ValueError:
    print("ERROR")
    continue