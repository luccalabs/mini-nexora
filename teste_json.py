import json

evento = [{
    'tipo':'academia',
    'prioridade':'alta',
    'descricao':'falha no equipamento'
},
{
    'tipo':'clinica',
    'prioridade':'media',
    'descricao':'relatorio'
}]

with open('evento.json', 'w') as arquivo:
    json.dump(evento, arquivo, indent=4)

with open('evento.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)
print(type(dados))

ref, posi = dados
print(posi['tipo'])
