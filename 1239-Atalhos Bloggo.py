def substituir(texto, simbolo, abertura, fechamento):
    novo_texto = texto.replace(simbolo, abertura, 1)
    aberto = True
    while novo_texto != texto:
        texto = novo_texto
        novo_texto = texto.replace(simbolo, fechamento if aberto else abertura, 1)
        aberto = not aberto
    return texto

while True:
    try:
        linha = input()
        linha = substituir(linha, '_', '<i>', '</i>')
        linha = substituir(linha, '*', '<b>', '</b>')
        print(linha)
    except EOFError:
        break