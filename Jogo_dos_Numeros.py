import random

minha_matriz = []
matriz_venc = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
numeros = list(range(1, 17))
jogo = True

while jogo:
    def main():
        global jogo
        opcao = bool(int(input("Digite (1) Jogar ou (0) Desistir: ")))

        if opcao:
            geraMat()
            for i in range(4):
                print(minha_matriz[i])
            while True:
                print("""\nDigite:
                (1) Imprimir a sua matriz
                (2) Verificar se ganhou
                (3) Inserir posição
                (4) Desistir """)
                opcao1 = int(input("Sua opção: "))

                if opcao1 == 1:
                    imprimir_mat()
                elif opcao1 == 2:
                    verificar()
                elif opcao1 == 3:
                    inserir_pos()
                else:
                    imprimir_mat()
                    print("Putz, você desistiu, seu merdinha! Tudo bem, na próxima da bom.")
                    jogo = False
                    break
        else:
            print("Putz, você desistiu, seu merdinha! Tudo bem, na próxima da bom.")
            jogo = False


    def geraMat():
        global minha_matriz, numeros
        lista_num_aux = numeros.copy()
        for i in range(4):
            lista_aux = []
            for j in range(4):
                num = random.choice(lista_num_aux)
                lista_aux.append(num)
                lista_num_aux.remove(num)
            minha_matriz.append(lista_aux)

    def imprimir_mat():
        global minha_matriz
        for i in range(4):
            print(minha_matriz[i])

    def inserir_pos():
        global minha_matriz
        l_pos1 = int(input("\nDigite a linha da primeira posição: ")) - 1
        c_pos1 = int(input("Digite a colunha da primeira posição: ")) - 1
        l_pos2 = int(input("Digite a linha da segunda posição: ")) - 1
        c_pos2 = int(input("Digite a colunha da segunda posição: ")) - 1
        # Trocando as posições
        guardar_valor = minha_matriz[l_pos1][c_pos1]
        minha_matriz[l_pos1][c_pos1] = minha_matriz[l_pos2][c_pos2]
        minha_matriz[l_pos2][c_pos2] = guardar_valor


    def verificar():
        global  minha_matriz, matriz_venc, jogo
        if minha_matriz == matriz_venc:
            print("\nParabéns, você ganhou!")
            jogo = False
            break

        else:
            print("\nHm.. Não foi dessa vez!")
            jogo = False

    main()