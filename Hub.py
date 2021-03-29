import Forca
import Adivinhação

print("*********************************")
print("*********Escolha seu jogo********")
print("*********************************")

print("(1) Forca  (2) Adivinhação")

jogo= int(input("Qual jogo?:"))

if(jogo == 1):
    print("Jogo escolhido: forca")
    Forca.jogar

if(jogo == 2):
    print("Jogo escolhido: adivinhação")
    Adivinhação.jogar()