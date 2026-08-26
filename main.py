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
    


print("===Eventos===")
print()
for posicao, eventin in enumerate(events, 1):
    
    print('evento ', posicao)
    print('tipo: ', eventin['tipo'])
    print('prioridade: ', eventin['prioridade'])
    print('descricao: ', eventin['descricao'])
    print()

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

print()

print('===Resumo===')
print('alta: ', alta)
print('media: ', media)
print('baixa: ', baixa)
print()

print('===Alertas===')

for posicao, eventin in enumerate(events, 1):
    if eventin['prioridade'] == 'alta':
        
        print(posicao, ' - ', eventin['descricao'])
        
print()

print('Programa Encerrado!')
