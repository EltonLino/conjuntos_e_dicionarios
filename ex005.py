equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

todas_tarefas = equipe_a | equipe_b

while True:
    print(todas_tarefas)
    resp = input('Deseja remover alguma tarefa da lista? [S/N]: ').strip().upper()
    if resp == 'N':
        break
    else:
        remover_tarefa = input('Digite a tarefa que deseja remover: ').strip().lower()
        todas_tarefas.remove(remover_tarefa)

print(f'Tarefas finais: {todas_tarefas}')