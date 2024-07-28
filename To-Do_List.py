
task = []

def exibir_lista(task):
    return task

def add_task():
    task.append(input("Adicionar Tarefa: "))

def remove_task():
    print(exibir_lista(task))
    task.remove(input("Escolha a tarefa que deseja remover: "))
    print("Tarefa Removida com sucesso")

while True:

    print("""

    1 - Adicionar Tarefa
    2 - Remover Tarefa
    3 - Exibir Lista
    4 - Sair


    """)
    
    choice = int(input("O que deseja fazer? "))

    match choice:
        case 1:
            add_task()
    
        case 2:
            remove_task()

        case 3:
            print(exibir_lista(task))

        case 4:
            break
        
        case _:
            print("Escolha invalida, tenta novamente")