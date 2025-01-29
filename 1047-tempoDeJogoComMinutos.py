aH, aM, cH, cM = map(int, input().split())

tMI = (aH * 60) + aM
tMF = (cH * 60) + cM

if tMF <= tMI:
    tMF += 24 * 60

dJ = tMF - tMI

horas = dJ // 60
minutos = dJ % 60


print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")