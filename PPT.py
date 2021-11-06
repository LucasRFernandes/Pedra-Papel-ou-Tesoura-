import random
import time




def jogo():
    
    possible_computer_choices = [
        "Pedra",
        "Papel",
        "Tesoura"
    ]
    player_choice = int(input("Oque quer escolher?\n1) Pedra\n2) Papel\n3) Tesoura\n>"))
    computer_choice = random.choice(possible_computer_choices)
    
    # Aqui vou fazer 3 condicionais IF que checam se o jogo deu empate
    if player_choice == 1 and computer_choice == "Pedra":
        print("Você escolheu pedra\nO Computador também escolheu pedra\nEMPATE")
        time.sleep(1)
        jogo()
    elif player_choice == 2 and computer_choice == "Papel":
        print("Você escolheu Papel\nO Computador também escolheu Papel\nEMPATE")
        time.sleep(1)
        jogo()
    elif player_choice == 3 and computer_choice == "Tesoura":
        print("Você escolheu Tesoura\nO Computador também escolheu Tesoura\nEMPATE") # As checagens de empate terminam aqui
        time.sleep(1)
        jogo()
    elif player_choice == 1 and computer_choice == "Tesoura": 
        print("Você escolheu Pedra\nO Computador escolheu Tesoura\nVocê ganhou, parabéns")
        time.sleep(1)
        jogo()   
    elif player_choice == 2 and computer_choice == "Pedra": 
        print("Você escolheu Papel\nO Computador escolheu Pedra\nVocê ganhou, parabéns")
        time.sleep(1)
        jogo()
    elif player_choice == 3 and computer_choice == "Papel": 
        print("Você escolheu Tesoura\nO Computador escolheu Papel\nVocê ganhou, parabéns")
        time.sleep(1)
        jogo()
    elif player_choice == 1 and computer_choice == "Papel": 
        print("Você escolheu Pedra\nO Computador escolheu Papel\nVocê perdeu, sinto muito")
        time.sleep(1)
        jogo()
    elif player_choice == 2 and computer_choice == "Tesoura": 
        print("Você escolheu Papel\nO Computador escolheu Tesoura\nVocê perdeu, sinto muito")
        time.sleep(1)
        jogo()
    elif player_choice == 3 and computer_choice == "Pedra": 
        print("Você escolheu Tesoura\nO Computador escolheu pedra\nVocê perdeu, sinto muito")
        time.sleep(1)
        jogo()
    else:
        print("Não configurado")
        print(player_choice)
        print(computer_choice)
        time.sleep(10)
        jogo()

jogo()