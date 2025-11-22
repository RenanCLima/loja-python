from apresentacao import conteudo_menu_inicial, conteudo_menu_cliente, conteudo_menu_produto, conteudo_menu_funcionario, conteudo_menu_venda

def pagina_inicial():
    conteudo_menu_inicial()
    try: 
        item_selecionado = int(input("Selecione uma opção: "))
    except:
        print("Entrada inválida, Por favor tente novamente")
        pagina_inicial()
    if item_selecionado == 1:
        conteudo_menu_cliente()
    if item_selecionado == 2:
        conteudo_menu_produto()
    if item_selecionado == 3:
        conteudo_menu_funcionario()
    if item_selecionado == 4:
        conteudo_menu_venda()
    if item_selecionado == 0:
        return
    
