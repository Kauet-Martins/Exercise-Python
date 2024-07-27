
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

    if choice == 1:
        add_task()
    
    elif choice == 2:
        remove_task()

    elif choice == 3:
        print(exibir_lista(task))

    elif choice == 4:
        break
    else:
        print("Escolha invalida tenta novamente")