import sys

def processar_texto(linha):
    resultado = []
    buffer = []
    cursor = resultado  # Lista onde os caracteres serão adicionados
    
    for char in linha:
        if char == '[':
            resultado.insert(0, [])  # Novo bloco no início
            cursor = resultado[0]  # Move o cursor para o novo bloco
        elif char == ']':
            cursor = resultado  # Retorna ao final da lista principal
        else:
            cursor.append(char)  # Adiciona caracteres na posição correta
    
    return "".join("".join(bloco) for bloco in resultado)

for linha in sys.stdin:
    print(processar_texto(linha.strip()))
