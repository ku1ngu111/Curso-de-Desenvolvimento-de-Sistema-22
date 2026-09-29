partidas = int(input("digite a quantidade de partidas que voce ganhou"))

if partidas >= 100:
    print("otima temporada")
elif partidas >= 50:
    print("boa temporada")
else:
    print("temporada ruim")