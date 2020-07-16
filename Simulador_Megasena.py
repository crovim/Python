import random
possiveis_valores = list(range(1, 61))

megasena = quina = quadra = bilhete = dinheiro = 0
for i in range(50063860):
    megasena += random.randrange(1500000, 70000000)
    quina += (random.randrange(1, 4)) / 10 * megasena
    quadra += 1 / (random.randrange(5000, 30000)) * megasena
    bilhete += 2.5
    sorteado = []
    meu_jogo = []
    cont_num_cert = 0
    print(i)
    lista_auxiliar = possiveis_valores.copy()
    for j in range(6):
        meu_jogo.append(random.choice(lista_auxiliar))
        lista_auxiliar.remove(meu_jogo[j])
    meu_jogo.sort()
    lista_auxiliar = possiveis_valores.copy()
    for y in range(6):
        sorteado.append(random.choice(lista_auxiliar))
        lista_auxiliar.remove(sorteado[y])
    sorteado.sort()
    if sorteado == meu_jogo:
        valor = random.randrange(1500000,70000000)
        dinheiro += valor
        megasena -= valor
    for k in range(6):
        for m in range(6):
            if sorteado[k] == meu_jogo[m]:
                cont_num_cert += 1
    if cont_num_cert == 5:
        valor = 0.94*(random.randrange(1,4))/10*megasena
        dinheiro += valor
        quina -= valor
    elif cont_num_cert == 4:
        valor = 1/(random.randrange(5000,30000))*megasena
        dinheiro += valor
        quadra -= valor

print("Valor total megasena: %i" %megasena)
print("Valor total quina: %i" %quina)
print("Valor total quadra: %i" %quadra)
print("Lucro do cliente: %i" %(dinheiro - bilhete))

