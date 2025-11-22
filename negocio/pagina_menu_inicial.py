from apresentacao import conteudo_menu_inicial, conteudo_menu_cliente, conteudo_menu_produto, conteudo_menu_funcionario, conteudo_menu_venda
from negocio.pagina_menu_cliente import pagina_menu_cliente

def pagina_menu_inicial():
    while True:
        conteudo_menu_inicial()
        try: 
            item_selecionado = int(input("Selecione uma opção: "))
            
            if item_selecionado == 1:
                conteudo_menu_cliente()
                pagina_menu_cliente()
            elif item_selecionado == 2:
                conteudo_menu_produto()
            elif item_selecionado == 3:
                conteudo_menu_funcionario()
            elif item_selecionado == 4:
                conteudo_menu_venda()
            elif item_selecionado == 0:
                print("Execução Encerrada com Sucesso!")
                break
            else:
                raise ValueError("Opção inválida")
                
        except ValueError:
            print("Entrada inválida, Por favor tente novamente")
