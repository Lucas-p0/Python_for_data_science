# Acessando Listas
dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro',
        'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital',
        'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS',
        'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
Acessorios = ['Rodas de liga',              
              'Travas elétricas',
              'Piloto automático',
              'Bancos de couro',
              'Ar condicionado',
              'Sensor de estacionamento',
              'Sensor crepuscular',
              'Sensor de chuva']

Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, [
    'Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, [
    'Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]

Lista_c = Acessorios[0:5]+Carro_1

# print(Lista_c)

'''for lista in dados:
    for item in lista:
        Acessorios.append(item)'''

list(set([item for lista in dados for item in lista]))

Acessorios.sort()


print(Acessorios)
