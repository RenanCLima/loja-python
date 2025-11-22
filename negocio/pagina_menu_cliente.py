from apresentacao import conteudo_menu_cliente
from dados import criar_cliente, buscar_cliente, atualizar_cliente, deletar_cliente

def pagina_menu_cliente():
    while True:
        conteudo_menu_cliente()
        try: 
            item_selecionado = int(input("Selecione uma opção: "))
            
            if item_selecionado == 1:
                buscar_cliente
                
            elif item_selecionado == 2:
                criar_cliente()
                
            elif item_selecionado == 3:
                atualizar_cliente
                
            elif item_selecionado == 4:
                deletar_cliente
                
            elif item_selecionado == 0:
                print("Execução Encerrada com Sucesso!")
                break
            else:
                raise ValueError("Opção inválida")
                
        except ValueError:
            print("Entrada inválida, Por favor tente novamente")