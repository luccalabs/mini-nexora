def cadastrar_eventos():
    events = []
    evento = int(input('Quantos eventos deseja cadastrar ? '))
    for _ in range(evento):
        tipo = input('tipo: ')
        while True:
            prioridade = input('prioridade: ')
            if prioridade in ['alta', 'media', 'baixa']:
                break
            print('opção invalida, digite alta, media ou baixa!')
        descricao = input('descricao: ')
        
        info = {
        'tipo': tipo,
        'prioridade': prioridade,
        'descricao': descricao,
        }
        events.append(info)
    return events

events = cadastrar_eventos()

    


def exibir_eventos(events):
    print("===Eventos===")
    for posicao, eventin in enumerate(events, 1):
        print('evento ', posicao)
        print('tipo: ', eventin['tipo'])
        print('prioridade: ', eventin['prioridade'])
        print('descricao: ', eventin['descricao'])
    
    
exibir_eventos(events)




def calcular_estatisticas(events):
    alta = 0
    media = 0
    baixa = 0
    
    for eventin in events:
        if eventin['prioridade'] == 'alta':
            alta += 1
        elif eventin['prioridade'] == 'media':
            media += 1
        elif eventin['prioridade'] == 'baixa':
            baixa += 1
    return alta, media, baixa
    
print()
alta, media, baixa = calcular_estatisticas(events)
print('===Resumo===')
print('alta: ', alta)
print('media: ', media)
print('baixa: ', baixa)
print()



def exibir_alertas(events):
    print('===Alertas===')
    for posicao, eventin in enumerate(events, 1):
        if eventin['prioridade'] == 'alta':
            print(posicao, ' - ', eventin['descricao'])
    

exibir_alertas(events)



print('Programa Encerrado!')
