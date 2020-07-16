import random
sorteado = []
meu_numero = []
print("""
Bem Vindo ao Jogo Bagels!
Preparado pra perder? hahah
Sugiro que leia as instruções antes de jogar""")

def sorteia_num():
    global sorteado
    lista = list(range(0, 9))
    for i in range(4):
        numero_sorteado = random.choice(lista)
        sorteado.append(numero_sorteado)
        lista.remove(numero_sorteado)

game = True
while game:
    print("""
 JOGO BAGELS
(1) Jogar
(2) Instruções
(3) Sair do jogo""")
    opcao = int(input("Sua Opção: "))

    if opcao == 1:
        sorteado = []
        sorteia_num()
        vidas = 1
        print("""\nLembrando que o número certo tem 4 dígitos
        de 0 a 9 que não se repetem!""")
        while True:
            print(f"\nVidas: {vidas}/10")
            contador_bagels = 0
            vidas += 1
            while True:
                o_porra = int(input("Digite um número de 4 dígitos: "))
                x = 1000
                meu_numero = []
                dica = []
                for k in range(4):
                    meu_numero.append(int(o_porra//x))
                    o_porra -= meu_numero[k]*x
                    x //= 10
                if len(meu_numero) == 4:
                    break
                else:
                    print("Número inválido")
            if meu_numero != sorteado and vidas != 10:
                for i in range(4):
                        if meu_numero[i] == sorteado[i]:
                            #Fermi
                            dica.append('Fermi')
                            contador_bagels += 1
                        elif meu_numero[i] in sorteado:
                            #Pico
                            dica.append('Pico')
                            contador_bagels += 1
                print(dica)
                if len(dica) == 0:
                    print("Bagels!")
            elif meu_numero == sorteado:
                print("Parabéns, você ganhou!")
                break
            if vidas == 10:
                print("\nVidas: 10/10 ")
                print(sorteado)
                print("Puts, você perdeu coleguinha")
                break



    elif opcao == 2:
        print("""
    INSTRUÇÕES:
O jogo sorteia um número de quatro dígitos
O jogador deve tentar acertar que número é este
Para isso, ele pode chutar um valor qualquer,
e então o programa colocará mensagens 
de acordo com os dígitos escolhidos:

Pico: Significa que um digíto está correto, 
      mas na posição errada
Fermi: Significa que um dígito está correto 
      e na posição correta
Bagels: Significa que nenhum dígito está certo
        """)
    elif opcao == 3:
        print("\nAté a próxima!!!")
        game = False

