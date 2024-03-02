tarefas = {}
prioridades = {}
conclusao = []
categoria = {}
while True:
    print('Bem vindo ao Gerenciador de Tarefas Diárias!')
    print('-'*55)
    decisao = int(input('''
O que você deseja fazer?

1) Adicionar tarefas
2) Listar tarefas
3) Marcar tarefas como concluídas
4) Exibir tarefas concluídas
5) Exibir tarefas por prioridade ou tipo
6) Excluir tarefas
7) Fechar o programa 
               
'''))
    print('-'*55)
    def add_tar():
        nometarefa = input('Digite o nome da tarefa que você deseja registrar: ')
        idtarefa = int(input('Digite um número de registro para essa tarefa: '))
        categoriatarefa = input('Digite o tipo da tarefa: ')
        prioridadetarefa = input('Digite a prioridade da tarefa. Pode ser ''Alta'', ''Média'' ou ''Baixa'': ')
        tarefas[idtarefa] = nometarefa
        prioridades[nometarefa] = prioridadetarefa
        categoria[nometarefa] = categoriatarefa
        print('-'*55)
        
    if decisao == 1:
        add_tar()
        
    if decisao == 2:
        print('Essas são suas tarefas:')
        print(tarefas)
        print('-'*55)
        
    def marcartar():
        if tarefas == {}:
            print('Você não tem tarefas pendentes!')
            return
        print(tarefas)
        qualtarefa = int(input('Digite o número de registro da tarefa que você deseja marcar como concluída: '))
        conclusao.append(tarefas[qualtarefa])
        tarefas.pop(qualtarefa)
        print('Você marcou essa tarefa como concluída, ela será removida da sua lista de tarefas!')
        
    if decisao == 3:
        marcartar()
        print('-'*55)
    
    if decisao == 4:
        print(f'Essas são suas tarefas concluídas: {conclusao}.')
        print('-'*55)
        
    def exibir_tarefas_especificas():
        prioridadeoucategoria = int(input('''
O que você deseja fazer?

1) Exibir tarefas por prioridade
2) Exibir tarefas por tipo       
                                   
'''))
        print('-'*55)
        if prioridadeoucategoria == 1:
            print(prioridades)
            qualprioridade = input('Digite o nome da prioridade exatamente como você a registrou anteriormente: ')
            print(f'Aqui vai uma lista com todas as tarefas que possuem a prioridade {qualprioridade}:')
            for chaves, valores in prioridades.items():
                if valores == qualprioridade:
                    print(chaves)
                    
        if prioridadeoucategoria == 2:
            print(categoria)
            qualcategoria = input('Digite o nome do tipo exatamente como você a registrou anteriormente: ')
            print(f'Aqui vai uma lista com todas as tarefas que possuem o tipo {qualcategoria}:')
            for chaves, valores in categoria.items():
                if valores == qualcategoria:
                    print(chaves)
                    
                    
    if decisao == 5:
        exibir_tarefas_especificas()
        print('-'*55)
        
    def excluir_tarefas():
        print(tarefas)
        qualtarefa = int(input('Digite o número de registro da tarefa que você quer excluir: '))
        tarefas.pop(qualtarefa)
        print('Sua tarefa foi excluída!')
        
    if decisao == 6:
        excluir_tarefas()
        print('-'*55)
        
    if decisao == 7:
        print('Obrigado por usar meu programa!')
        break