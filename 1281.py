nIdasFeira = int(input())

for _ in range(nIdasFeira):
    num_produtos_disponiveis = int(input())
    tabela_precos = {}
    
    for _ in range(num_produtos_disponiveis):
        dados = input().split()
        nome_produto = " ".join(dados[:-1])
        preco_unitario = float(dados[-1])
        tabela_precos[nome_produto] = preco_unitario
    
    num_itens_compra = int(input())
    total_compra = 0.0
    
    for _ in range(num_itens_compra):
        dados = input().split()
        nome_produto = " ".join(dados[:-1])
        quantidade = int(dados[-1])
        total_compra += tabela_precos[nome_produto] * quantidade
    
    print(f"R$ {total_compra:.2f}")
