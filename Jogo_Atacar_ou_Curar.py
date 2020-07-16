def main ():
    opcao = int(input('Digite "1"(novo jogo) ou "2"(carregar jogo):'))
    if opcao == 1:
        # Quantidade de inimigos:
        quantidade = int(input("Digite a quantidade de inimigos: "))
        vida_ini = 50

        # Gerando os inimigos com suas respectivas vidas:
        inimigos = []
        for i in range(quantidade):
            inimigos.append([i+1, vida_ini])

        # Dados do Player:
        vida_player = 500
        mana_player = 100
        print("""\nVida do Player: %i
        Mana do Player: %i"""%(vida_player, mana_player))
    elif opcao == 2:
        dados_salvos = open("Jogo_salvo.txt",'r')
        dados_salvos.seek(39)
        vida_player = dados_salvos[:42]
        dados_salvos.seek(46)
        mana_player = dados_salvos[:49]
        dados_Salvos.seek(58)
        inimigos = dados_salvos[59:]
    game(vida_player, mana_player, inimigos)

def game(vida_player, mana_player, inimigos):
    while True:
        import random
        # Analisando a ação do player
        acao = int(input("""\nDigite 1 para Atacar ou 2 para Curar
                        ou 3 para Salvar:"""))
        if acao == 1:
            ini_selecionado = random.choice(inimigos)
            dano = random.randrange(10, 16) # Selecionando dano aleatorio
            ini_selecionado[1] -= dano # Tira o dano na vida do inimigo
            if ini_selecionado[1] <= 0: # Removendo o inimigo que morreu
                print("Inimigo %i morreu!\n" %ini_selecionado[0])
                inimigos.remove(ini_selecionado)
            print("\nVocê causou %i de dano no inimigo %i!" %(dano, ini_selecionado[0]))
        elif acao == 2:
            if mana_player >= 10:
                cura = random.randrange(10, 16)
                print("Você curou %i de vida!\n" %cura)
                mana_player -= 10
                if vida_player < 491: # Garantindo que não vai passar de 500
                    vida_player += cura
                else:
                    vida_player = 500
        elif acao == 3:
            save(vida_player, mana_player, inimigos)
            break
        print("Vida dos inimigos: ")
        for i in range(len(inimigos)): # Printando a vida dos inimigos
            ini_selecionado = inimigos[i]
            print("Inimigo %i : Vida: %i" %(ini_selecionado[0], ini_selecionado[1]))
        soma = 0
        print("""\nVida do Player: %i
        Mana do Player: %i""" % (vida_player, mana_player))
        for i in range(len(inimigos)): # Vê se o inimigo vai acertar o ataque
            ini_selecionado = inimigos[i]
            chance = bool(random.choice([1, 1, 1, 0]))
            if chance: # Tira o dano do player
                dano = random.randrange(1, 10)
                soma += dano
                vida_player -= dano
                print("O inimigo %i lhe causou %i de dano" %(ini_selecionado[0], dano))
            else:
                print("O inimigo %i errou o ataque!" %ini_selecionado[0])
        if mana_player < 98:
            mana_player += 3
        else:
            mana_player = 100
        if vida_player <= 0:
            vida_player = 0
        print("Você levou %i de dano nessa rodada!" %soma)
        print("""\nVida do Player: %i
        Mana do Player: %i""" % (vida_player, mana_player))
        if vida_player <= 0:
            print("Fui derrotado, buceta!")
            break
        if (len(inimigos)) == 0:
            print("Você é o cara, matou tudo!")
            break

def save(vida_player, mana_player, inimigos):
    dados_salvos = open("Jogo_salvo.txt",'w')
    dados_salvos.write(f'Jogo salvo!')
    dados_salvos.write('\nProgresso em:\n')
    dados_salvos.write(f'HP:{vida_player}, MP:{mana_player}, Inimigos:{inimigos}')
    dados_salvos.close()

main()

