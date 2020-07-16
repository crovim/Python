"""
Escreva um jogo de sobrevivência, no qual o player irá escolher entre
jogar, salvar e desistir.

JOGAR --> O jogo escolherá 1 entre 4 inimigos para lutar com o player,
SALVAR --> Salva o estado do player e o número de inimigos derrotados
DESISTIR --> Salva um arquivo de Score contendo o tanto de inimigos que o
player derrotou

O combate:
Existem as seguintes classes:
Arqueiro, Druida, Guerreiro e Mago

O jogador pode escolher entre os diversos ataques

Já os inimigos:
Ogro, Goblin, Esqueleto e Bruxo

A cada 10 inimigos derrotados o número de inimigos em uma batalha dobra, e o
player os enfrenta SIMULTANEAMENTE

"""

def main():
    while True:
        print("####### MENU #######")
        if (int(input("1-Jogar ou 2-Sair\nEscolha:"))) == 1:
            game()
        else:
            print("\nAté mais!!")
            break

def game():
    import random
    global classe, atributos, pot_HP, pot_MP, name, category

    option = int(input("""Bem vindo ao mundo RP2.0!
    Escolha uma das opções:
    (1) Começar um novo jogo
    (2) Continuar o game
    Sua opção: """))
    if option == 1:
        name = input("Nickname: ")
        atributos = []  # [HP,MP,ATK,ATKM,DEF]
        classe = str(input("""\nEscolha sua classe:
        (a) Arqueiro
        (d) Druida
        (g) Guerreiro
        (m) Mago
        Sua opção: """))
        print("#" * 50)
        atributos, category = choiseclass(name, classe)
        print("\nSeus atributos são:"
              f"\nHP:{atributos[0]}, MP:{atributos[1]}"
              f"\nATK:{atributos[2]}, ATK Mágico:{atributos[3]}"
              f"\nDefesa:{atributos[4]}")
        pot_HP = pot_MP = 5
        kill = 0
###################################################################
    # Arrumar a opção de Load no game ainda
    else:
        load = open("GameSaved.txt", 'r')
        atributos = []
        load.readline()
        load.readline()
        name = str(load.readline())
        classe = str(load.readline())
        for i in range(5):
            x = int(load.readline())
            atributos.append(x)
        #x = int(load.readline())
       # kill = x
        print("Seus dados:")
        print(f"\nNickname:{name} Classe:{classe}"
              f"HP:{atributos[0]} MP:{atributos[1]}"
              f"\nATK:{atributos[2]} ATK Mágico:{atributos[3]}"
              f"\nDefesa:{atributos[4]}")
######################################################################
    print("#" * 50)
    print("\nVamos começar?")
    qtd_inimies = random.randrange(1, 3)
    print(f"Você irá batalhar contra {qtd_inimies} inimigo(s)")
    choises = random_inimies(qtd_inimies)
    # Inimigos: HP, MP, ATK, DEF, XP
    inimies = {'Ogro': [60, 5, 12, 4, 5], 'Goblin': [40, 10, 8, 2, 8],
               'Esqueleto': [80, 20, 15, 10, 20], 'Bruxo': [80, 20, 10, 15, 25]}
    atributes_ini = []
    print("\nOs dados do(s) seu(s) inimigo(s) são:")
    for i in range(qtd_inimies):
        atributes = inimies.get(choises[i])
        atributes_ini.append(atributes)
        print(f"{choises[i]} -> HP:{atributes_ini[i][0]}, MP:{atributes_ini[i][1]}")
    # FASE DE COMBATE!!!
    while True:
        input("------Pressione qualquer tecla para continuar-------")
        if atributos[0] > 0:
            if len(choises) > 0:
                print("#" * 50)
                opcao = int(input(
                    "\nVocê deseja fazer o que?\n(1) Atacar \n(2) Skill\n(3) Poção de HP\n(4) Poção de MP\n(5) Salvar game"
                    "\n(6) Sair do jogo"
                    "\nSua opção: "))
                # Ataques normais
                if opcao == 1:
                    for i in range(qtd_inimies):
                        print(f"{i}- {choises[i]}")
                    if qtd_inimies != 1:
                        number_ini = int(input("Qual inimigos você deseja atacar?"))
                    else:
                        number_ini = 0
                    atk = ATK_types(classe)
                    dano_total = (atributos[2] + atk) - atributes_ini[number_ini][3]
                    if dano_total > 0:
                        atributes_ini[number_ini][0] -= dano_total
                    else:
                        dano_total = 0
                    print(f"\nVocê tirou {dano_total} do inimigo.")
                    if atributes_ini[number_ini][0] > 0:
                        print(f"Agora o {choises[number_ini]} tem {atributes_ini[number_ini][0]} de HP")
                    else:
                        print(f"Você matou o {choises[number_ini]}!")
                        del (choises[number_ini])
                        kill += 1
                # Ataques mágicos
                elif opcao == 2:  ##Preciso colocar a análise de MP
                    atk, magic, mana = Skill_types(classe)
                    if magic == 2:
                        for i in range(qtd_inimies):
                            if atk > 0:
                                dano_total = (atributos[3] + atk) - atributes_ini[i][3]
                                if dano_total != 0:
                                    atributes_ini[i][0] -= dano_total
                                else:
                                    dano_total = 0
                                    print("A defesa desse inimigo é muito forte!")
                                if atributes_ini[i][0] > 0:
                                    print(f"\nVocê tirou {dano_total} do {choises[i]}.")
                                    print(f"Agora ele tem {atributes_ini[i][0]} de HP")
                                else:
                                    print(f"\nVocê tirou {dano_total} do {choises[i]}.")
                                    print(f"Você matou o {choises[i]}!")
                                    del (choises[i])
                                    kill += 1
                        atributos[1] -= mana
                    else:
                        for i in range(qtd_inimies):
                            print(f"{i}- {choises[i]}")
                        number_ini = 0
                        dano_total = (atributos[3] + atk) - atributes_ini[number_ini][3]
                        if dano_total > 0:
                            atributes_ini[number_ini][0] -= dano_total
                        else:
                            dano_total = 0
                            print("A defesa desse inimigo é muito forte!")
                        if atributes_ini[number_ini][0] > 0:
                            print(f"\nVocê tirou {dano_total} do inimigo.")
                            print(f"Agora o {choises[number_ini]} tem {atributes_ini[number_ini][0]} de HP")
                        else:
                            print(f"\nVocê tirou {dano_total} do inimigo.")
                            print(f"Você matou o {choises[number_ini]}!")
                            del (choises[number_ini])
                            kill += 1
                        atributos[1] -= mana
                # Usando poção de HP
                elif opcao == 3:
                    if pot_HP > 0:
                        pot_HP -= 1
                        print(f"\nVocê restaurou 10 de HP!\nAgora você tem somente {pot_HP} poções de HP")
                        atributos[0] += 10
                        print(f"E está com {atributos[0]} de HP")
                    else:
                        print("Você não tem poções de HP! E perdeu sua jogada procurando.")
                # Usando poção de MP
                elif opcao == 4:
                    if pot_MP > 0:
                        pot_MP -= 1
                        print(f"\nVocê restaurou 7 de MP!\nAgora você tem somente {pot_MP} poções de MP")
                        atributos[1] += 7
                        print(f"E está com {atributos[1]} de MP")
                    else:
                        print("Você não tem poções de HP! E perdeu sua jogada procurando.")
                elif opcao == 5:
                    game_save = open("GameSaved.txt", 'w')
                    game_save.write("Jogo Salvo!\n")
                    game_save.write("Dados do personagem:\n")
                    game_save.write(f"{name}\n")
                    game_save.write(f"{category}")
                    game_save.write(f"{atributos[0]}\n")
                    game_save.write(f"{atributos[1]}\n")
                    game_save.write(f"{atributos[2]}\n")
                    game_save.write(f"{atributos[3]}\n")
                    game_save.write(f"{atributos[4]}\n")
                    game_save.write(f"{kill}")
                    game_save.close()
                    break
                else:   
                    break

                if len(choises) > 0:
                    ###Fase de ataque dos inimigos
                    print("-" * 50)
                    for i in range(qtd_inimies):
                        if atributos[0] > 0:
                            golpe, dano = ATK_ini(choises[i])
                            atributos[0] -= (dano - atributos[4])
                            print(f"O {choises[i]} utilizou o golpe {golpe} "
                                  f"\ne te tirou {dano-atributos[4]} de HP.")
                else:
                    print("\nVocê matou todos os inimigos!")
                    break
        else:
            print(f"\n\nVocê morreu! E matou um total de {kill} inimigos.")
            print("Talvez dê certo na próxima")
            break
        print("#" * 50)
        if atributos[0] > 0:
            print("\nSeus atributos:"
                  f"\nHP:{atributos[0]} MP:{atributos[1]}")
        else:
            print("\nSeus atributos:"
                  f"\nHP: 0 MP: {atributos[1]}")
        print("\nOs dados do(s) seu(s) inimigo(s) são:")
        for i in range(qtd_inimies):
            atributes = inimies.get(choises[i])
            atributes_ini.append(atributes)
            print(f"{choises[i]} -> HP:{atributes_ini[i][0]}, MP:{atributes_ini[i][1]}")

def ATK_ini(inimigo):
    import random
    if inimigo == 'Ogro':
        list_atks = ['Bastão', 'Cabeçada', 'Quebra Ossos']
        atk = random.randrange(3)
        hit = list_atks[atk]
        if hit == 'Bastão':
            dano = random.randrange(8, 12)
        elif hit == 'Cabeçada':
            dano = random.randrange(4, 8)
        else:
            dano = random.randrange(12, 16)
    elif inimigo == 'Goblin':
        list_atks = ['Martelada', 'Impulso com Martelo', 'Batida Ecoante']
        atk = random.randrange(3)
        hit = list_atks[atk]
        if hit == 'Martelada':
            dano = random.randrange(3, 7)
        elif hit == 'Impulso com Martelo':
            dano = random.randrange(6, 12)
        else:
            dano = random.randrange(10, 15)
    elif inimigo == 'Esqueleto':
        list_atks = ['Tiro de Falanges', 'Cadeia Óssea', 'Membro Fantasma']
        atk = random.randrange(3)
        hit = list_atks[atk]
        if hit == 'Tiro de Falanges':
            dano = random.randrange(14, 19)
        elif hit == 'Cadeia óssea':
            dano = random.randrange(21, 27)
        else:
            dano = random.randrange(21, 30)
    else:
        list_atks = ['Aperto Demoníaco', 'Horda de Pestes', 'Grande Estrondo do Rei Demônio']
        atk = random.randrange(3)
        hit = list_atks[atk]
        if hit == 'Aperto Demoníaco':
            dano = random.randrange(21, 25)
        elif hit == 'Horda de Pestes':
            dano = (random.randrange(1, 4)) * (random.randrange(6, 8))
        else:
            dano = random.randrange(25, 40)
    return hit, dano

def Skill_types(classe):
    mana = 0
    print("\nSkills habilitadas:")
    dano = mag = 0
    if classe == 'a':
        mag = int(input("\n(1)Flecha Tripla: +15 Dano, MP: 15"
                          "\n(2)Chuva de Flechas: +10 Dano em todos inimigos, MP: 20"
                          "\nOpção: "))
        if mag == 1:
            dano = 8
            mana = 15
        else:
            dano = 15
            mana = 20
    elif classe == 'g':
        mag = int(input(
            "\n(1)Golpe Perfurante: +14 Dano, MP: 15"
            "\n(2)Giro com Espada: +8 Dano em todos inimigos, MP: 18"
            "\nOpção: "))
        if mag == 1:
            dano = 14
            mana = 15
        else:
            dano = 8
            mana = 18
    elif classe == 'd':
        mag = int(input(
            "\n(1)Arranhões Múltiplos: +12 Dano, MP: 8"
            "\n(2)Raiva da Natureza: +14 Dano em todos inimigos, MP: 14"
            "\nOpção: "))
        if mag == 1:
            dano = 12
            mana = 8
        else:
            dano = mana = 14
    elif classe == 'm':
        atack = int(input(
            "\n(1)Bola de fogo: +10 Dano, MP: 10"
            "\n(2)Tempestade de raios: +14 Dano em todos inimigos, MP: 14"
            "\nOpção: "))
        if atack == 1:
            dano = mana = 10
        else:
            dano = mana = 14
    return dano, mag, mana

def ATK_types(classe):
    dano = 0
    print("\nAtaques habilitados:")
    if classe == 'a':
        atack = int(input(
            "\n(1)Flechada: +5 Dano"
            "\n(2)Esfaquear: +2 Dano"
            "\nOpção: "))
        if atack == 1:
            dano = 5
        else:
            dano = 2
    elif classe == 'g':
        atack = int(input(
            "\n(1)Espadada: +7 Dano"
            "\n(2)Cabecear: +2 Dano"
            "\nOpção: "))
        if atack == 1:
            dano = 7
        else:
            dano = 2
    elif classe == 'd':
        atack = int(input(
            "\n(1)Arranhar: +3 Dano"
            "\n(2)Morder: +2 Dano"
            "\nOpção: "))
        if atack == 1:
            dano = 3
        else:
            dano = 2
    elif classe == 'm':
        atack = int(input(
            "\n(1)Bola de magia: +2 Dano"
            "\n(2)Bater com o bastão: +1 Dano"
            "\nOpção: "))
        if atack == 1:
            dano = 2
        else:
            dano = 1
    return dano

def random_inimies(n):
    import random
    list = []
    list_inimies = ['Ogro', 'Goblin', 'Esqueleto', 'Bruxo']
    for i in range(0, n, 1):
        number = random.randrange(4)
        name = list_inimies[number]
        list.append(name)
    return list

def choiseclass(name, classe):
    print(f"Bem Vindo(a), {name}!")
    global atributos, category
    if classe == 'a':
        category = 'Arqueiro'
        atributos = [60, 80, 3, 3, 1]
    elif classe == 'd':
        category = 'Druida'
        atributos = [80, 80, 2, 2, 2]
    elif classe == 'g':
        category = 'Guerreiro'
        atributos = [100, 40, 4, 1, 3]
    elif classe == 'm':
        category = 'Mago'
        atributos = [80, 100, 1, 4, 2]
    return (atributos, category)

main()
